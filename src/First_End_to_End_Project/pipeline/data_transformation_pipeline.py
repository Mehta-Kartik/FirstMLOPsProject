from src.First_End_to_End_Project.config.configuration import ConfigurationManager
from src.First_End_to_End_Project.components.data_transformation import DataTransformation
from src.First_End_to_End_Project import logger

STAGE_NAME="DATA TRANSFORMATION stage"

class DataTransformationPipeline:
    def __init__(self):
        pass
    
    def initiate_data_transformation(self):
        config=ConfigurationManager()
        data_transformation_config=config.get_data_transformation_config()
        data_transformation=DataTransformation(config=data_transformation_config)
        data_transformation.train_test_splitting()


if __name__=="__main__":
     try:
          logger.info(f">>> Stage {STAGE_NAME} Started<<<")
          obj=DataTransformationPipeline()
          obj.initiate_data_transformation()
          logger.info(f">>> Stage {STAGE_NAME} Ended<<<")
     except Exception as e:
          logger.exception(e)
          raise e