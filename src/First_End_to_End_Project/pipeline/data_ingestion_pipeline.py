from src.First_End_to_End_Project.config.configuration import ConfigurationManager
from src.First_End_to_End_Project.components.data_ingestion import DataIngestion
from src.First_End_to_End_Project import logger

STAGE_NAME="Data Ingestion Stage"

class DataIngestionTrainingPipeline:
    def __init__(self):
        pass
    
    def initiatedataingestion(self):
            
            config=ConfigurationManager()
            data_ingest_config=config.get_data_ingest_config()
            data_ingestion=DataIngestion(config=data_ingest_config)
            data_ingestion.download_file()
            # data_ingestion.extract_zip_file()
            

if __name__=="__main__":
     try:
          logger.info(f">>> Stage {STAGE_NAME} Started<<<")
          obj=DataIngestionTrainingPipeline()
          obj.initiatedataingestion()
          logger.info(f">>> Stage {STAGE_NAME} Ended<<<")
     except Exception as e:
          logger.exception(e)
          raise e