from src.First_End_to_End_Project.config.configuration import ConfigurationManager
from src.First_End_to_End_Project.components.model_evaluator import ModelEvaluation
from src.First_End_to_End_Project import logger

STAGE_NAME= "Model Evaluation Stage"

class ModelEvaluationPipeline:
    def __init__(self):
        pass
    
    def initiate_model_evaluations(self):
        config=ConfigurationManager()
        model_eval_config=config.get_model_evaluation_config()
        model_eval_config=ModelEvaluation(config=model_eval_config)
        model_eval_config.log_into_mlflow()

if __name__=="__main__":
     try:
          logger.info(f">>> Stage {STAGE_NAME} Started<<<")
          obj=ModelEvaluationPipeline()
          obj.initiate_model_evaluations()
          logger.info(f">>> Stage {STAGE_NAME} Ended<<<")
     except Exception as e:
          logger.exception(e)
          raise e
