# Gastrointestinal Disease Detection using Endoscopic Imaging

This repository aims to contribute to the field of healthcare by developing and evaluating models for the detection of gastrointestinal diseases using endoscopic imaging.  

## Dataset Overview

The dataset used in this project is collected through endoscopic equipment at Vestre Viken Health Trust (VV) in Norway. VV, consisting of four hospitals, serves approximately 470,000 people. The  dataset consists of 4,000 annotated images of the gastrointestinal tract in 8 different classes (different anomalies), each class has 500 images.

The 8 classes of anomalies:

* dyed-lifted-polyps
* normal-cecum
* normal-pylorus
* normal-z-line
* esophagitis
* polyps
* ulcerative colitis
* dyed-resection-margins

**Explore the Dataset:** [Kvasir Gastrointestinal Disease Dataset](https://www.kaggle.com/datasets/meetnagadia/kvasir-dataset/data)

For more details on the dataset and its applications, refer to the Jupyter Notebooks provided in the repository.

---

*Disclaimer: This project is intended for research purposes and should not replace professional medical advice or diagnosis.*

## Repository Contents

This repository includes Jupyter Notebooks to guide users through the process:

**Module 1: Data Loading and Preprocessing**
   - Loading data from Kaggle.
   - Preprocessing steps.

**Module 2: Model Development and Evaluation**
   - Building and evaluating VGG16, ResNet50, and MobileNetV2 models.
   - Using the best-performing model (ResNet50 with an accuracy of 84.5%) to make predictions on random pictures from the dataset and comparing predicted vs. actual labels.
