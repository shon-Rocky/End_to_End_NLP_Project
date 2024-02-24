# Import necessary modules and classes
from src.textSummarizer.config.configuration import ConfigurationManager  # Importing ConfigurationManager class
from src.textSummarizer.conponents.model_trainer import ModelTrainer  # Importing modeltrainerconfig class
from src.textSummarizer.logging import logger  # Importing logger for logging messages


class ModelTrainerTrainingPipeline:
    def __init__(self):
        pass  # Constructor does nothing in this case

    def main(self):
        config = ConfigurationManager()
        model_trainer_config = config.get_model_trainer_config()
        model_trainer_config = ModelTrainer(config=model_trainer_config)
        model_trainer_config.train()
