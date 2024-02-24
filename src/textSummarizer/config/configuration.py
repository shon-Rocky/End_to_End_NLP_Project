# Import necessary modules and classes
from src.textSummarizer.constants import *  # Importing constants from the constants module
from src.textSummarizer.utils.common import read_yaml, create_directories  # Importing utility functions
from src.textSummarizer.entity import (DataIngestionConfig, DataValidationConfig)  # Importing entity classes


class ConfigurationManager:
    def __init__(
        self,
        config_filepath=CONFIG_FILE_PATH,  # Default path to the configuration file
        params_filepath=PARAMS_FILE_PATH  # Default path to the parameters file
    ):

        # Read configuration and parameters from YAML files
        self.config = read_yaml(config_filepath)
        self.params = read_yaml(params_filepath)

        # Create necessary directories specified in the configuration
        create_directories([self.config.artifacts_root])

    # Method to get data ingestion configuration
    def get_data_ingestion_config(self) -> DataIngestionConfig:
        # Extract data ingestion configuration from the overall configuration
        config = self.config.data_ingestion

        # Create necessary directories specified in the data ingestion configuration
        create_directories([config.root_dir])

        # Create DataIngestionConfig object with the extracted configuration
        data_ingestion_config = DataIngestionConfig(
            root_dir=config.root_dir,
            source_URL=config.source_URL,
            local_data_file=config.local_data_file,
            unzip_dir=config.unzip_dir
        )

        return data_ingestion_config  # Return the DataIngestionConfig object

    # Method to get data validation configuration
    def get_data_validation_config(self) -> DataValidationConfig:
        # Extract data validation configuration from the overall configuration
        config = self.config.data_validation

        # Create necessary directories specified in the data validation configuration
        create_directories([config.root_dir])

        # Create DataValidationConfig object with the extracted configuration
        data_validation_config = DataValidationConfig(
            root_dir=config.root_dir,
            STATUS_FILE=config.STATUS_FILE,
            ALL_REQUIRED_FILES=config.ALL_REQUIRED_FILES,
        )

        return data_validation_config  # Return the DataValidationConfig object
