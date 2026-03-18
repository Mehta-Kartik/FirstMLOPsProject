import os
from urllib import request
from src.First_End_to_End_Project import logger
import zipfile
from src.First_End_to_End_Project.entity.config_entity import (DataIngestionconfig)

class DataIngestion:
    def __init__(self, config: DataIngestionconfig):
        self.config = config

    def download_file(self):
        if not os.path.exists(self.config.local_data_file):
            filename, headers = request.urlretrieve(
                url=self.config.source_URL,
                filename=self.config.local_data_file
            )
            logger.info(f"✅ {filename} downloaded!")
        else:
            logger.info(f"📁 File exists: {self.config.local_data_file}")

    def get_data(self):  # New method for CSV
        """Load CSV data for validation/next steps"""
        import pandas as pd
        return pd.read_csv(self.config.local_data_file)
    
    # Keep extract_zip_file but make optional
    # def extract_zip_file(self):
    #     if self.config.get('unzip_dir'):  # Check if ZIP config exists
    #         unzip_path = self.config.unzip_dir
    #         os.makedirs(unzip_path, exist_ok=True)
    #         with zipfile.ZipFile(self.config.local_data_file, 'r') as zipref:
    #             zipref.extractall(unzip_path)
    #             logger.info(f"✅ ZIP extracted to {unzip_path}")
    #     else:
    #         logger.info("ℹ️ No ZIP extraction needed (CSV data)")

# Usage:
def initiate_data_ingestion(self):
    self.download_file()
    self.extract_zip_file()  # Safe now - skips for CSV
