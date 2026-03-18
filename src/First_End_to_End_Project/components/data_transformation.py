## Component works
import os
from src.First_End_to_End_Project import logger
from sklearn.model_selection import train_test_split
from src.First_End_to_End_Project.config.configuration import DataTransformationConfig
import pandas as pd
class DataTransformation:
    def __init__(self,config:DataTransformationConfig):
        self.config=config
    
    def train_test_splitting(self):
        data=pd.read_csv(self.config.data_dir)
        train,test=train_test_split(data)
        train.to_csv(os.path.join(self.config.root_dir,"train.csv"),index=False)
        test.to_csv(os.path.join(self.config.root_dir,"test.csv"),index=False)

        logger.info("Splitted data into training and test sets")
        logger.info(train.shape)
        logger.info(test.shape)

        print(train.shape)
        print(test.shape)