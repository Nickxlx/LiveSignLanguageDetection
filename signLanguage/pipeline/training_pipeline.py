import sys, os
from signLanguage import logger
from signLanguage.exception import SignException
from signLanguage.components.data_ingestion import DataIngestion
from signLanguage.components.data_validation import DataValidation
from signLanguage.components.model_trainer import ModelTrainer


from signLanguage.entity.config_entity import (DataIngestionConfig, 
                                                DataValidationConfig,
                                                ModelTrainerConfig)

from signLanguage.entity.artifacts_entity import (DataIngestionArtifact,
                                                DataValidationArtifact,
                                                ModelTrainerArtifact)

class TrainPipeline:
    def __init__(self):
        self.data_ingestion_config = DataIngestionConfig()
        self.data_validation_config = DataValidationConfig()
        self.model_trainer_config = ModelTrainerConfig()
        
    def start_data_ingestion(self)->DataIngestionArtifact:
        try:
            logger.logging.info("Entered to the start_data_ingestion method of TrainPipeline class")
            logger.logging.info("Getting the data from the URL")

            data_ingestion =  DataIngestion(
                data_ingestion_config = self.data_ingestion_config
            )
            data_ingestion_artifact = data_ingestion.initiate_data_ingestion()

            logger.logging.info("Got the data from URL")
            logger.logging.info("Exited the start_data_ingestion method of TrainPipeline Class")

            return data_ingestion_artifact

        except Exception as e:
            raise SignException(e, sys)
    
    def start_data_validation(
    self, data_ingestion_artifact: DataIngestionArtifact) -> DataValidationArtifact:
        
        logger.logging.info("Entered the start_data_validation method of TrainPipeline class")

        try:
            data_validation = DataValidation(
                data_ingestion_artifact=data_ingestion_artifact,
                data_validation_config=self.data_validation_config,
            )
            val_status = data_validation.initiate_data_validation()

            logger.logging.info("Performed the data validation operation")
            logger.logging.info(
                "Exited the start_data_validation method of TrainPipeline class"
            )

            return val_status
        except Exception as e:
            raise SignException(e, sys) from e
        

    def start_model_trainer(self):
        try: 
            model_trainer = ModelTrainer(model_trainer_config=self.model_trainer_config)
            model_trainer_artifacts = model_trainer.initiate_model_trainer()
            return model_trainer_artifacts
        except Exception as e:
            raise SignException(e, sys)

    def run_pipeline(self):
        try:
            # Initialize data ingestion
            data_ingestion_artifact = self.start_data_ingestion()
            data_validation_artifact = self.start_data_validation(data_ingestion_artifact=data_ingestion_artifact)
            if data_validation_artifact:
                model_trainer_artifact = self.start_model_trainer()
            else:
                raise Exception("Your data is not in correct format")
            
        except Exception as e:
            raise SignException(e,sys)


# to check trainig pipeline

# if __name__ == "__main__":
#     obj = TrainPipeline()
#     art = obj.run_pipeline()
#     print(art)