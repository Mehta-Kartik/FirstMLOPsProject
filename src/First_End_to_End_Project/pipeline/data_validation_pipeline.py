from src.First_End_to_End_Project.config.configuration import ConfigurationManager
from src.First_End_to_End_Project.components.data_validation import DataValidation
from src.First_End_to_End_Project import logger

STAGE_NAME= "DATA VALIDATION stage"

class DataValidationTrainingPipeline:
    def __init__(self):
        pass
    
    def initiate_data_validation(self):
        config=ConfigurationManager()
        data_validation_config=config.getdatavalidationconfig()
        data_validation=DataValidation(config=data_validation_config)
        data_validation.validate_all_columns()

if __name__=="__main__":
     try:
          logger.info(f">>> Stage {STAGE_NAME} Started<<<")
          obj=DataValidationTrainingPipeline()
          obj.initiate_data_validation()
          logger.info(f">>> Stage {STAGE_NAME} Ended<<<")
     except Exception as e:
          logger.exception(e)
          raise e