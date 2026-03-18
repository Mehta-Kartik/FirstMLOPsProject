from src.First_End_to_End_Project import logger
from src.First_End_to_End_Project.pipeline.data_ingestion_pipeline import DataIngestionTrainingPipeline
from src.First_End_to_End_Project.pipeline.data_validation_pipeline import DataValidationTrainingPipeline
from src.First_End_to_End_Project.pipeline.data_transformation_pipeline import DataTransformationPipeline
from src.First_End_to_End_Project.pipeline.model_trainer_pipeline import ModelTrainingPipeline


STAGE_NAME="Data Ingestion Stage"
try:
    logger.info(f">>> Stage {STAGE_NAME} Started<<<")
    obj=DataIngestionTrainingPipeline()
    obj.initiatedataingestion()
    logger.info(f">>> Stage {STAGE_NAME} Ended<<<")
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME="Data Validation Stage"
try:
    logger.info(f">>> Stage {STAGE_NAME} Started<<<")
    obj=DataValidationTrainingPipeline()
    obj.initiate_data_validation()
    logger.info(f">>> Stage {STAGE_NAME} Ended<<<")
except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME="Data Transformation Stage"
try:
    logger.info(f">>> Stage {STAGE_NAME} Started<<<")
    obj=DataTransformationPipeline()
    obj.initiate_data_transformation()
    logger.info(f">>> Stage {STAGE_NAME} Ended<<<")
except Exception as e:
    logger.exception(e)
    raise e





STAGE_NAME="Model Training Stage"
try:
    logger.info(f">>> Stage {STAGE_NAME} Started<<<")
    obj=ModelTrainingPipeline()
    obj.initiate_model_training()
    logger.info(f">>> Stage {STAGE_NAME} Ended<<<")
except Exception as e:
    logger.exception(e)
    raise e
