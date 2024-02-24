# Import necessary modules and classes
from src.textSummarizer.config.configuration import ConfigurationManager  # Importing ConfigurationManager class
from src.textSummarizer.conponents.data_validation import DataValidation  # Importing DataValidation class
from src.textSummarizer.logging import logger  # Importing logger for logging messages


class DataValidationTrainingPipeline:
    def __init__(self):
        pass  # Constructor does nothing in this case

    def main(self):
        # Initialize ConfigurationManager to manage configurations
        config = ConfigurationManager()
        
        # Get data validation configuration from ConfigurationManager
        data_validation_config = config.get_data_validation_config()
        
        # Instantiate DataValidation object with the obtained configuration
        data_validation = DataValidation(config=data_validation_config)
        
        # Perform data validation: check if all required files exist
        data_validation.validate_all_files_exist()
