<!-- ABOUT THE PROJECT -->
## TSSWD
Taiwan SAR-based Ship and Weather Dataset (TSSWD) is the latest SAR ship dataset combined with weather data. [Link]() to the research paper.

Here's why you should use our dataset:
* Dataset build up with buoy weather data, i.e. every image has various weather data including **wave height**, **wind speed** ... etc. So not only the dataset can be use in Ship detection, it also got the potential to do sea weather prediction through SAR images!
* We only use **Sentinel-1** as our image source, no mixed-source satellite, which is more common practice in Remote Sensing Field.
* The ship size in our dataset is smaller than previous dataset, which means it's more challenging :smile:

### Training & Testing Details

The Object Detection / Instance Segmentation Models are list bellow. **Bold** represent Instance Segmentation. The training and testing logs are all in log folder.    
| Models | GPU | Notes |
|---|---|---|
| Mask R-CNN, YOLOV5, CenterMask | Nvidia Tesla V100 32G, Nvida RTX 2080Ti 12G | Provide by [NTUCE-NCREE AI Research Center](http://www.aiengineer.tw/) |
| Rest of them | Nvidia GTX 1060 6G | Home PC |

* **Mask R-CNN-X152**
* **Mask R-CNN-X101**
* **Mask R-CNN-101**
* **CenterMask-V99**
* **CenterMask-V57**
* YOLOV5-l
* YOLOV5-l6
* YOLOV5-x
* YOLOV5-x6
* PPYOLO
* Mask R-CNN-X152
* HRNET
* TOOD
* Cascade R-CNN
* Sparse R-CNN
* Res2Net
* FCOS

<!-- LICENSE -->
## License & Citation

Distributed under the MIT License. See `LICENSE` for more information.    

If our work is helpful to your research, please cite us    

`cite = {}`


<!-- CONTACT -->
## Contact

Email - r10521801@ntu.edu.tw   

Email - yalunstsai@ntu.edu.tw  

LAB Website: [EORSLAB](https://yalunstsai.wixsite.com/eorslab-ntu)
