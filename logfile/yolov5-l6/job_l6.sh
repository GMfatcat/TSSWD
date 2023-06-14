#!/bin/bash
#SBATCH --job-name="yolov5l6_tsswd"
#SBATCH --partition=v100-32g
#SBATCH --ntasks=4
#SBATCH --gres=gpu:1
#SBATCH --time=10-00:00:00
#SBATCH --output=cout_yolov5l6.txt
#SBATCH --error=cerr_yolov5l6.txt
#SBATCH --chdir=.
###SBATCH --test-only

sbatch_pre.sh
module load opt gcc python/3.8.10-gpu
python3 train.py --img 800 --batch 16 --epochs 300 --data ship.yaml --weights yolov5l6.pt --save-period 100

sbatch_post.sh

