from src.First_End_to_End_Project.config.configuration import ConfigurationManager
from src.First_End_to_End_Project.components.model_trainer import ModelTrainer
from src.First_End_to_End_Project import logger

STAGE_NAME= "Model Traning Stage"

class ModelTrainingPipeline:
    def __init__(self):
        pass
    
    def initiate_model_training(self):
        config=ConfigurationManager()
        model_train_config=config.get_model_trainer_config()
        model_train=ModelTrainer(config=model_train_config)
        model_train.train()

if __name__=="__main__":
     try:
          logger.info(f">>> Stage {STAGE_NAME} Started<<<")
          obj=ModelTrainingPipeline()
          obj.initiate_data_validation()
          logger.info(f">>> Stage {STAGE_NAME} Ended<<<")
     except Exception as e:
          logger.exception(e)
          raise e