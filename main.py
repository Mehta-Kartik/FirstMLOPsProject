from src.First_End_to_End_Project import logger
from src.First_End_to_End_Project.pipeline.data_ingestion_pipeline import DataIngestionTrainingPipeline



STAGE_NAME="Data Ingestion Stage"
try:
    logger.info(f">>> Stage {STAGE_NAME} Started<<<")
    obj=DataIngestionTrainingPipeline()
    obj.initiatedataingestion()
    logger.info(f">>> Stage {STAGE_NAME} Ended<<<")
except Exception as e:
    logger.exception(e)
    raise e