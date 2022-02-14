# An end-to-end architecture of Transformer-based method for identifying cell type specific Alzheimer disease related genes from single-cell RNA-sequencing data  

**Alzheimer's disease** (AD) is a severe neuron disease that damages brain cells, resulting in permanent memory loss. It affects over 35 million people worldwide and is currently the sixth leading cause of death in the United States. AD-related brain pathology begins almost 10–20 years before the onset of dementia symptoms. Although no disease-modifying treatments are currently available for AD, early diagnosis could lead to early therapeutic interventions to delay the disease progression over time and could help tailor disease management and plan future care and improve the quality of AD patient’s life. Here, we're the first to propose an interpretable end-to-end Transformer based architecture for dianosing AD and explaining AD-related important genes.  This is the source code for the method as described in our paper:
**An end-to-end architecture of Transformer-based method for identifying cell type specific Alzheimer disease related genes from single-cell RNA-sequencing data**. 

<div align=center><img width="1000" height="300" src="https://github.com/circustata/TransGene/blob/main/figure/model_framework_wholestructure.jpg"/></div>
<p align="left">
The framework of our end-to-end Transformer based method. In the data processing component, the single-cell RNA expression profiles of AD patients and control individuals are obtained and shuffled. In the Transformer component, a linear layer converts the processed data into lower-dimensional representations. After that, the Transformer encoder learns the relationships between each cell. Finally, the model can be trained to identify the source for the cells through the loss function.
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
The scRNA-seq data of 95,186 single-nucleus transcriptomes from 17 hippocampus (8 controls and 9 AD cases), stratified by 14 cell types, were used to evaluate the performance of our model. In order to make it easier for the readers to reproduce and understand the code, we have provided a small amount of synthesized Arterial cell type related data under the **dataset** folder, where provides 20 synthesized scRNA-seq data for each patient.

## Cell Types
"Veinous", "T cell", "SMC", "Pericyte", "Capillary", "Arterial", "Oligo", "P. Fibro", "Ependymal", "Microglia", "Astrocyte", "OPC", "M. Fibro", "Neuron"


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
<div align=center><img width="1000" height="300" src="https://github.com/circustata/TransGene/blob/main/figure/patient_level_score.jpg"/></div>
<p align="left"> 
The framework of our method. (a) Calculate the Across Feature Map Attention. The inputs are the initial image and i-th layer feature maps of the encoder. (b) Output Modification. The generated AFMA in (a) is used to modify the output of the decoder’s predicted masks. (c) The process of generating gold AFMA.
</p>
