import os
import pandas as pd
from sklearn.metrics import mean_squared_error,mean_absolute_error,r2_score
from urllib.parse import urlparse
import mlflow
import mlflow.sklearn
import numpy as np
import joblib
from pathlib import Path
from src.First_End_to_End_Project.config.configuration import ModelEvaluationConfig
from src.First_End_to_End_Project.constants import *
from src.First_End_to_End_Project.utils.common import read_yaml,create_directories,save_json

from dotenv import load_dotenv
load_dotenv()

class ModelEvaluation:
    def __init__(self,config:ModelEvaluationConfig):
        self.config=config
    
    def eval_metrics(self,actual,predict):
        rmse=np.sqrt(mean_squared_error(actual,predict))
        mae=mean_absolute_error(actual,predict)
        r2=r2_score(actual,predict)
        return rmse,mae,r2
    
    def log_into_mlflow(self):
        test_data=pd.read_csv(self.config.test_data_path)
        model=joblib.load(self.config.model_path)

        test_x=test_data.drop([self.config.target_column],axis=1)
        test_y=test_data[[self.config.target_column]]

        mlflow.set_registry_uri(self.config.mlflow_uri)
        tracking_url_type_store=urlparse(mlflow.get_tracking_uri()).scheme

        with mlflow.start_run():
            predicted_qualities=model.predict(test_x)
            (rmse,mae,r2)=self.eval_metrics(actual=test_y,predict=predicted_qualities)

            #Save the metrics as local
            score={"rmse":rmse,"mae":mae,"r2":r2}
            save_json(path=Path(self.config.metric_file_name),data=score)

            mlflow.log_params(self.config.all_params)

            mlflow.log_metric("rmse",rmse)
            mlflow.log_metric("mae",mae)
            mlflow.log_metric("r2",r2)


            #If model Registry does not work with file store
            if tracking_url_type_store!="file":
                mlflow.sklearn.log_model(model,"Model",registered_model_name="ElasticNetModel")
            else:
                mlflow.sklearn.log_model(model,"Model")
        