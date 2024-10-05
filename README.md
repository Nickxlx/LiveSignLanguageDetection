# Sign Language Detection Using YOLOv5

This project focuses on detecting and classifying sign language gestures using **YOLOv5**, a state-of-the-art object detection algorithm. The model is trained on a custom dataset of hand signs representing different letters or words in sign language and can accurately identify and interpret these gestures in real time (live mode).

## Project Overview

Sign language is a vital form of communication for the hearing impaired, and automating its recognition can bridge communication gaps. This project uses **YOLOv5** to detect hand gestures from images and videos, which are then classified into the corresponding sign language gestures.

### Key Components:
- **YOLOv5 Architecture**: Leveraging the speed and accuracy of YOLOv5 to perform gesture detection.
- **Custom Dataset**: A dataset containing images of various sign language gestures, with corresponding labels.
- **Training**: The model was trained on this dataset to detect and classify gestures with high precision.
- **Inference**: The model can be deployed to detect hand signs in real time from video feeds or images using Flask.

## Features

- **Fast and Accurate Detection**: Using YOLOv5 for efficient real-time gesture detection.
- **Customizable**: The model can be retrained on new sign language gestures if needed.
- **End-to-End Pipeline**: Includes data preprocessing, model training, evaluation, and deployment.

## Setup Instructions

### 1. Clone the Repository
```bash
git clone https://github.com/Nickxlx/SignLanguageDetection.git
cd SignLanguageDetection
```

### 2. Set Up Environment
Create and activate a new Python environment using `conda`:
```bash
conda create -n nenv python=3.7 -y
conda activate nenv
```

### 3. Install Dependencies
Install the necessary dependencies:
```bash
pip install -r requirements.txt
```

### 4. Download the Dataset
Ensure you have the dataset stored in the correct directory structure(With the image dim 416*530).

### 4. Run Application
```bash
python app.py
```
- open in browser: http://localhost:8080/train (for training the model) or skip this if you want to use trained model because its gonna takes time.
- For Prediction: http://localhost:8080/ (For Uploding the data)
- For Live Prediction: http://localhost:8080/ (For live Prediction)


## Contributions

Feel free to contribute to this project by:
- Adding new sign language gestures
- Improving model accuracy
- Implementing new features for real-time detection

## Contact

For questions or feedback regarding the project, you can reach out to the project owner at [nikhilsinghxlx@gmail.com](mailto:nikhilsinghxlx@gmail.com).


