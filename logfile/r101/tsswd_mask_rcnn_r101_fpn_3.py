# -*- coding: utf-8 -*-
"""
Created on Wed Apr  6 11:54:01 2022

@author: user
"""

# Some basic setup:
# Setup detectron2 logger
import detectron2
from detectron2.utils.logger import setup_logger
setup_logger()

# import some common libraries
import numpy as np
import os, json, cv2, random

# import some common detectron2 utilities
from detectron2 import model_zoo
from detectron2.engine import DefaultPredictor
from detectron2.config import get_cfg
from detectron2.utils.visualizer import Visualizer
from detectron2.data import MetadataCatalog, DatasetCatalog

# Define path of annotation file and train/val data
ann_file_train='/<your path>/annotation/train/coco/annotation/train.json'
ann_file_val='/<your path>/annotation/val/coco/annotation/val.json'
ann_file_test='/<your path>/annotation/test/coco/annotation/test.json'
img_prefix='/<your path>/JPEG_Images'

# Set up dataset
from detectron2.data.datasets import register_coco_instances
print("==== Registering DataSet ====")
register_coco_instances("ship_train", {}, ann_file_train, img_prefix)
register_coco_instances("ship_val", {}, ann_file_val, img_prefix)
register_coco_instances("ship_test", {}, ann_file_test, img_prefix)
print("==== Finish Registering ====")
ship_metadata_train = MetadataCatalog.get("ship_train")
ship_metadata_test = MetadataCatalog.get("ship_val")

# Training Config
from detectron2.engine import DefaultTrainer
print("==== Modifying Config ====")
cfg = get_cfg()
cfg.merge_from_file(model_zoo.get_config_file("COCO-InstanceSegmentation/mask_rcnn_R_101_FPN_3x.yaml"))
cfg.DATASETS.TRAIN = ("ship_train",)
cfg.DATASETS.TEST = ("ship_val",)
cfg.DATALOADER.NUM_WORKERS = 4   # CPU : Number of data loading threads
cfg.MODEL.WEIGHTS = model_zoo.get_checkpoint_url("COCO-InstanceSegmentation/mask_rcnn_R_101_FPN_3x.yaml")  # Let training initialize from model zoo
# Disable data augmentation
cfg.INPUT.RANDOM_FLIP = "none"
# Solver Parm
cfg.SOLVER.IMS_PER_BATCH = 16
cfg.SOLVER.BASE_LR = 0.0005  # pick a good LR
cfg.SOLVER.MAX_ITER = 50000    # max iterations
cfg.SOLVER.STEPS = (30000,)        # do not decay learning rate until 30000 steps
cfg.MODEL.ROI_HEADS.BATCH_SIZE_PER_IMAGE = 256   # faster, and good enough for this toy dataset (default: 512)
cfg.MODEL.ROI_HEADS.NUM_CLASSES = 1  # only has one class (ship). (see https://detectron2.readthedocs.io/tutorials/datasets.html#update-the-config-for-new-datasets)
# NOTE: this config means the number of classes, but a few popular unofficial tutorials incorrect uses num_classes+1 here.
cfg.MODEL.FPN.NORM = "GN" # Group Normalization
cfg.SOLVER.CHECKPOINT_PERIOD = 25000 # Save a checkpoint after every this number of iterations
# Test Parm
cfg.TEST.EVAL_PERIOD = 1000 # test at every 1000 iter
# Output path
cfg.OUTPUT_DIR = "./checkpoints_r101"
os.makedirs(cfg.OUTPUT_DIR, exist_ok=True)
print("==== Config been Modified ====")

# Training
print("==== Start Training ====")
trainer = DefaultTrainer(cfg) 
trainer.resume_or_load(resume=False) # Resume training from last training ---> resume = True
trainer.train()

# validate the training
# Inference should use the config with parameters that are used in training
# cfg now already contains everything we've set previously. We changed it a little bit for inference:
print("====Start Evaluation on Test Set====")
cfg.MODEL.WEIGHTS = os.path.join(cfg.OUTPUT_DIR, "model_final.pth")  # path to the model we just trained
cfg.MODEL.ROI_HEADS.SCORE_THRESH_TEST = 0.7   # set a custom testing threshold
predictor = DefaultPredictor(cfg)

from detectron2.evaluation import COCOEvaluator, inference_on_dataset
from detectron2.data import build_detection_test_loader
evaluator = COCOEvaluator("ship_test", output_dir="./evaluation_output_r101")
val_loader = build_detection_test_loader(cfg, "ship_test")
print(inference_on_dataset(predictor.model, val_loader, evaluator))


print("====Start Evaluation on Val Set====")
evaluator2 = COCOEvaluator("ship_val", output_dir="./evaluation_output_r101")
val_loader2 = build_detection_test_loader(cfg, "ship_val")
print(inference_on_dataset(predictor.model, val_loader2, evaluator2))






