# Sign Language Detection Using YOLOv5
This project aims to build a Sign Language Detection model using the YOLOv5 architecture. The model is trained to detect and classify sign language gestures from images or videos.

1. constants
2. entity
3. components
4. pipelines
5. app.py

## How to Run
1. Clone the repo to locals

```bash
conda create -n nenv python=3.7 -y
```

```bash
conda activate nenv
```

```bash
pip install -r requirements.txt
```

```bash
python app.py
```
- open in browser: http://localhost:8080/train (for training the model) or skip this if you want to use trained model because its gonna takes time.
- For Prediction: http://localhost:8080/ (For Uploding the data)
- For Live Prediction: http://localhost:8080/ (For live Prediction)
