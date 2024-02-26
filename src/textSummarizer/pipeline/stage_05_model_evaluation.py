from src.textSummarizer.config.configuration import ConfigurationManager  # Importing ConfigurationManager class
from src.textSummarizer.conponents.model_evaluation import ModelEvaluation  #
from src.textSummarizer.logging import logger  # Importing logger for logging messages


class ModelEvaluationTrainingPipeline:
    def __init__(self):
        pass  # Constructor does nothing in this case

    def main(self):
        config = ConfigurationManager()
        model_evaluation_config = config.get_model_evaluation_config()
        model_evaluation_config = ModelEvaluation(config=model_evaluation_config)
        model_evaluation_config.evaluate()

    