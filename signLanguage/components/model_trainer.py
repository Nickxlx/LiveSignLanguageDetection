import os, sys 
import zipfile
import shutil
import yaml
from signLanguage.utils.main_utils import read_yaml_file
from signLanguage.logger import logging
from signLanguage.exception import SignException
from signLanguage.entity.config_entity import ModelTrainerConfig
from signLanguage.entity.config_entity import DataIngestionConfig
from signLanguage.entity.artifacts_entity import ModelTrainerArtifact

class ModelTrainer:
    def __init__(self,
                model_trainer_config: ModelTrainerConfig
                ):
        self.model_trainer_config = model_trainer_config   # to store train model inside artifacts folder 
        self.data_ingestion_config = DataIngestionConfig()

    def initiate_model_trainer(self)-> ModelTrainerArtifact:
        logging.info("Entered initiate_model_trainer method of ModelTrainer class")
        try:
            logging.info("Unzipping data")
            
            with zipfile.ZipFile("Sign_language_data.zip", "r") as zip_ref:
                zip_ref.extractall()

            # Remove Sign_language_data.zip
            os.remove("Sign_language_data.zip")
            
            # opening the yaml file to collect the no of classes 
            with open(f"{self.data_ingestion_config.feature_store_file_path}/data.yaml", "r") as stream:
                num_classes = str(yaml.safe_load(stream)["nc"])

            model_config_file_name = self.model_trainer_config.weight_name.split(".")[0]
            print(model_config_file_name)

            config = read_yaml_file(f"yolov5/models/{model_config_file_name}.yaml")
            config['nc'] = int(num_classes)

            # creating the custmize yaml file with the same no of classes 
            with open(f"yolov5/models/custom_{model_config_file_name}.yaml", 'w') as f:
                yaml.dump(config, f)

            os.system(f"cd yolov5/ && python train.py --img 416 --batch {self.model_trainer_config.batch_size} --epochs {self.model_trainer_config.no_epochs} --data ../data.yaml --cfg ./models/custom_yolov5s.yaml --weights {self.model_trainer_config.weight_name} --name yolov5s_results  --cache")

            shutil.copy("yolov5/runs/train/yolov5s_results/weights/best.pt", "yolov5/")
            os.makedirs(self.model_trainer_config.model_trainer_dir, exist_ok=True)
            shutil.copy("yolov5/runs/train/yolov5s_results/weights/best.pt", self.model_trainer_config.model_trainer_dir)

            logging.info(f"Save the best model at path = {self.model_trainer_config.model_trainer_dir}")

            shutil.rmtree("yolov5/runs")
            shutil.rmtree("train")
            shutil.rmtree("test")
            
            os.remove("data.yaml")

            model_trainer_artifact = ModelTrainerArtifact(
                trained_model_file_path= "yolov5/best.pt"
            )

            logging.info("Exited initiate_model_trainer method of ModelTrainer class")
            logging.info(f"Model trainer artifact: {model_trainer_artifact}")

            return model_trainer_artifact

        except Exception as e:
            raise SignException(e, sys)