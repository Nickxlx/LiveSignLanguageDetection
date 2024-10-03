import os
import sys
import shutil

from signLanguage.pipeline.training_pipeline import TrainPipeline 
from signLanguage.exception import SignException
from signLanguage.utils.main_utils import decodeImage, encodeImageIntoBase64

from flask import Flask, request, render_template, Response,jsonify
from flask_cors import CORS, cross_origin  # for security (allow multipal machine to share the resources)

app = Flask(__name__)
CORS(app)

class ClientApp:
    def __init__(self):
        self.filename = "inputImage.jpg"

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/train")
def train():
    obj = TrainPipeline()
    obj.run_pipeline()
    return "Training Successfull!!"

# route for the detection
@app.route("/predict", methods=['POST'])
@cross_origin()
def predict():
    try:
        image = request.json['image']
        
        # collecting the decoded img (in binary)
        decodeImage(image, clApp.filename)

        #  run detection on the img
        os.system("cd yolov5/ && python detect.py --weights best.pt --img 416 --conf 0.5 --source ../data/inputImage.jpg")

        # decoding the img 
        opencodedbase64 = encodeImageIntoBase64("yolov5/runs/detect/exp/inputImage.jpg")

        # storing the decoded img 
        result = {"image": opencodedbase64.decode('utf-8')}

        shutil.rmtree("yolov5/runs")

    except ValueError as val:
        print(val)
        return Response("Value not Found inside Json Data")
    except KeyError:
        return Response("Key value error incorrect key passed")
    except Exception as e:
        print(e)
        result = "Invalid Input"

    return jsonify(result)


# route for live detection 
@app.route("/live", methods=['GET'])
@cross_origin()
def predictLive():
    try:
        os.system("cd yolov5/ && python detect.py --weights best.pt --img 416 --conf 0.5 --source 0")
        shutil.rmtree("yolov5/runs")
        return "Camera starting!!" 
    except ValueError as val:
        print(val)
        return Response("Value not found inside  json data")
    
if __name__ == "__main__":
    clApp = ClientApp()
    app.run(host="0.0.0.0", port = 8080)