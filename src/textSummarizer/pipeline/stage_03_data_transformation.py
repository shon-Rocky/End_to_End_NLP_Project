# Import necessary modules and classes
from src.textSummarizer.config.configuration import ConfigurationManager  # Importing ConfigurationManager class
from src.textSummarizer.conponents.data_transformation import DataTransformation  # Importing DataVa class
from src.textSummarizer.logging import logger  # Importing logger for logging messages


class DataTransformationTrainingPipeline:
    def __init__(self):
        pass  # Constructor does nothing in this case

    def main(self):
        config = ConfigurationManager()
        data_transformation_config = config.get_data_transformation_config()
        data_transformation = DataTransformation(config=data_transformation_config)
        data_transformation.convert()
