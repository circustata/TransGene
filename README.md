# An end-to-end architecture of Transformer-based method for identifying cell type specific Alzheimer disease related genes from single-cell RNA-sequencing data  

This is the source code for the method as described in our paper:
**An end-to-end architecture of Transformer-based method for identifying cell type specific Alzheimer disease related genes from single-cell RNA-sequencing data**. 

<div align=center><img width="1000" height="280" src="https://github.com/circustata/TransGene/blob/main/figure/model_framework_wholestructure.jpg"/></div>
<p align="left">
The framework of our method. Our method mainly contains two parts, one is the data processing part and the other is the model part. 
</p>

<div align=center><img width="600" height="800" src="https://github.com/circustata/TransGene/blob/main/figure/model_framework_attention.jpg"/></div>
<p align="left"> 
The framework of our method. (a) Calculate the Across Feature Map Attention. The inputs are the initial image and i-th layer feature maps of the encoder. (b) Output Modification. The generated AFMA in (a) is used to modify the output of the decoder’s predicted masks. (c) The process of generating gold AFMA.
</p>

As shown in above framework figure. Our approache mainly consists of three parts:
* The lines **23-176** of encoder_channelatt_img.py are used for calculating AFMA between original image and any layer of feature map (for part (a) in above figure). 
* The files with **\_decoder.py** suffix in the deeplabv3, fpn, linknet, manet, pan, pspnet, unet, unetplusplus folders are the steps to combine AFMA to the existing model (for part (b) in above figure). AFMA approach is adaptable to different types of architectures of various semantic segmentation models and can work on different layers of the encoder’s feature maps. 
* The **MyLoss_correction.py** in utils is for calculating the gold standard AFMA and training loss (for part(c) in above figure).

<div align=center><img width="1000" height="300" src="https://github.com/circustata/TransGene/blob/main/figure/patient_level_score.jpg"/></div>
<p align="left"> 
The framework of our method. (a) Calculate the Across Feature Map Attention. The inputs are the initial image and i-th layer feature maps of the encoder. (b) Output Modification. The generated AFMA in (a) is used to modify the output of the decoder’s predicted masks. (c) The process of generating gold AFMA.
</p>

## Requirements
* inplace_abn==1.1.0
* numpy==1.22.2
* pandas==1.2.4
* pretrainedmodels==0.7.4
* scikit_learn==1.0.2
* torch==1.8.0
* torchvision==0.9.0

## Data
* [CamViD](http://mi.eng.cam.ac.uk/research/projects/VideoRec/CamVid/) The Cambridge-driving Labeled Video Database (CamVid) is the first collection of videos with object class semantic labels, complete with metadata.. 
* [CityScapes](https://www.cityscapes-dataset.com/dataset-overview/) CityScapes is a new large-scale dataset that contains a diverse set of stereo video sequences recorded in street scenes from 50 different cities. 
* [Caltech-UCSD Birds](http://www.vision.caltech.edu/visipedia/CUB-200.html) Caltech-UCSD Birds 200 (CUB-200) is an image dataset with photos of 200 bird species (mostly North American). 
* [LiTS](https://www.kaggle.com/andrewmvd/liver-tumor-segmentation) 130 CT scans for segmentation of the liver as well as tumor lesions.
* [SkinLesion](https://challenge2018.isic-archive.com/) Skin Lesion Analysis towards Melanoma Detection Challenge Part I.

In order to make it easier for the readers to reproduce and understand the code, I have provided a small amount of example data used in our experiment under the **dataset** folder, where provides six training, validation and test images for the CamVid.

## File declaration
**models/attonimage**：contains the codes for calculating AFMA.

**models/manet**：the decoder and segmentation part of the manet_afma model.

**models/unet**： the decoder and segmentation part of the unet_afma model.

**models/unetplusplus**：the decoder and segmentation part of the unet\+\+_afma model.

**models/deeplabv3**：the decoder and segmentation part of the deeplabv3_afma model.

**models/fpn**：the decoder and segmentation part of the fpn_afma model.  

**models/pan**：the decoder and segmentation part of the pan_afma model.

**models/linknet**：the decoder and segmentation part of the linknet_afma model.

**models/pspnet**：the decoder and segmentation part of the pspnet_afma model.

**main.py**: The codes for training, validating and testing.

## Run the codes
Install the environment.
```bash
pip install -r requirements.txt
```
Train and test the model.
```bash
python main.py
```
