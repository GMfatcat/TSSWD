<!-- ABOUT THE PROJECT -->
## TSSWD :ship:
Taiwan SAR-based Ship and Weather Dataset (TSSWD) is the latest SAR ship dataset combined with weather data. [Link]() to the research paper.

Here's why you should use our dataset:
* Dataset build up with buoy weather data, i.e. every image has various weather data including **wave height**, **wind speed** ... etc. So not only the dataset can be use in Ship detection, it also got the potential to do sea weather prediction through SAR images!
* We only use **Sentinel-1** as our image source, no mixed-source satellite, which is more common practice in Remote Sensing Field.
* The ship size in our dataset is smaller than previous dataset, which means it's more challenging :smile:

### Dataset Details :green_book:

We now only provide **Mask-RCNN-X152** and **YOLOV5** model's weight due to the storage limitation.\
If you need other model weight, please contact us.

|          Satellite          |   Mode   |   Images   |  Ships  |     Size    | Resolution |
|:---------------------------:|:--------:|:----------:|:-------:|:-----------:|:----------:|
|          Sentinel-1         |    IW    |    2904    |   8255  |   800x800   |    10 m    |
|       Annotation Type       | Training | Validation | Testing | Weights |  Dataset |
| COCO / VOC / YOLOV4 / YOLOV5 |   2324   |     290    |   290   | [Click Me](https://drive.google.com/drive/folders/187sgcSEF8eRBL3AuWnMjG7rLgs_O4XIr?usp=sharing)            |   [Click Me](https://drive.google.com/drive/folders/1iJI775r_iQzYK1Po1Hgu_cIgTiuqzVdW?usp=sharing)         |

### Training & Testing Details :muscle:

The Object Detection / Instance Segmentation Models are list bellow. **Bold** represent Instance Segmentation.\
Training and testing params set in log file.\
Mask R-CNN use [Detectron2 platform](https://github.com/facebookresearch/detectron2).\
YOLOV5 and CenterMask use their official github repo.\
All model trained by GTX 1060 use the [ppdet platform](https://github.com/PaddlePaddle/PaddleDetection)
| Models | GPU | Notes |
|---|---|---|
| Mask R-CNN, YOLOV5, CenterMask | Nvidia Tesla V100 32G, Nvida RTX 2080Ti 12G | Provide by [NTUCE-NCREE AI Research Center](http://www.aiengineer.tw/) |
| Rest of them | Nvidia GTX 1060 6G | Home PC |

* **Mask R-CNN-X152** -- [log](/logfile/x152)
* **Mask R-CNN-X101** -- [log](/logfile/x101)
* **Mask R-CNN-101** -- [log](/logfile/r101)
* **CenterMask-V99** -- [log](/logfile/v99)
* **CenterMask-V57** -- [log](/logfile/v57)
* YOLOV5-l -- [log](/logfile/yolov5-l)
* YOLOV5-l6 -- [log](/logfile/yolov5-l6)
* YOLOV5-x -- [log](/logfile/yolov5-x)
* YOLOV5-x6 -- [log](/logfile/yolov5-x6)
* PPYOLO -- [log](/logfile/ppyolo)
* HRNET -- [log](/logfile/hrnet)
* TOOD -- [log](/logfile/tood)
* Cascade R-CNN -- [log](/logfile/cascade-rcnn)
* Sparse R-CNN -- [log](/logfile/sparse-rcnn)
* Res2Net -- [log](/logfile/res2net)
* FCOS -- [log](/logfile/fcos)

|      Model      | Bbox mAP | Bbox mAP50 | Seg mAP | Seg mAP50 |
|:---------------:|:--------:|:----------:|:-------:|:---------:|
| Mask R-CNN-r101 |  49.475  |   90.672   |  43.753 |   90.581  |
| Mask R-CNN-x101 |  48.732  |   90.835   |  45.247 |   92.047  |
| Mask R-CNN-x152 |  51.211  |   93.061   |  46.512 |   93.04   |
|  CenterMask-V99 |  47.024  |    86.21   |  43.726 |   87.736  |
|  CenterMask-V57 |  47.168  |   85.929   |  43.468 |   86.861  |
|    YOLO V5-l    |   54.8   |    94.9    |    x    |     x     |
|    YOLO V5-l6   |   55.4   |    93.7    |    x    |     x     |
|    YOLO V5-x    |   55.5   |    94.8    |    x    |     x     |
|    YOLO V5-x6   |   52.9   |    95.1    |    x    |     x     |
|      PPYOLO     |    49    |    91.9    |    x    |     x     |
|      HRNET      |    49    |     91     |    x    |     x     |
|       TOOD      |   42.9   |    79.3    |    x    |     x     |
|  Cascade R-CNN  |    50    |    90.5    |    x    |     x     |
|   Sparse R-CNN  |   44.9   |    86.3    |    x    |     x     |
|     Res2Net     |   49.6   |    91.1    |    x    |     x     |
|       FCOS      |   43.6   |    80.3    |    x    |     x     |

![Prediction Examples](/img/Model Predict Example.jpg)

<!-- LICENSE -->
## License & Citations

Distributed under the MIT License. See `LICENSE` for more information.    

If our work is helpful to your research, use this bibtex to cite this repository:
```
@misc{TSSWD,
  title={TSSWD: Taiwan SAR-based Ship Detection and Weather Dataset},
  author={Shang-Fong, Yang and YaLun, Tsai},
  year={2023},
  publisher={Github},
  journal={GitHub repository},
  howpublished={\url{https://github.com/GMfatcat/TSSWD}}
}
```

use this citation if the article is published (not yet):
```
@article{TSSWD,
  title={TSSWD: Taiwan SAR-based Ship Detection and Weather Dataset},
  author={Shang-Fong, Yang and YaLun, Tsai},
  keywords={SAR,Ship Detection,Object Detection,Instance Segmentation,Buoy}
  year={2023},
  publisher={},
  journal={},
  volume={},
  number={},
  pages={},
}
```

<!-- CONTACT -->
## Contact

Email - r10521801@ntu.edu.tw   

Email - yalunstsai@ntu.edu.tw  

LAB Website: [EORSLAB](https://yalunstsai.wixsite.com/eorslab-ntu)
