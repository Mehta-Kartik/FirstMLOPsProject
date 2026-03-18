from src.First_End_to_End_Project import logger
from src.First_End_to_End_Project.pipeline.data_ingestion_pipeline import DataIngestionTrainingPipeline
from src.First_End_to_End_Project.pipeline.data_validation_pipeline import DataValidationTrainingPipeline



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

