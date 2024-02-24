# Import necessary modules and classes
from src.textSummarizer.constants import *  # Importing constants from the constants module
from src.textSummarizer.utils.common import read_yaml, create_directories  # Importing utility functions
from src.textSummarizer.entity import (DataIngestionConfig,
                                       DataValidationConfig,
                                       DataTransformationConfig,
                                       ModelTrainerConfig)  # Importing entity classes


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
    
    
    
        
    def get_data_transformation_config(self) -> DataTransformationConfig:
        config = self.config.data_transformation

        create_directories([config.root_dir])

        data_transformation_config = DataTransformationConfig(
            root_dir=config.root_dir,
            data_path=config.data_path,
            tokenizer_name = config.tokenizer_name
        )

        return data_transformation_config
    
    
    
    def get_model_trainer_config(self) -> ModelTrainerConfig:
        config = self.config.model_trainer
        params = self.params.TrainingArguments

        create_directories([config.root_dir])

        model_trainer_config = ModelTrainerConfig(
            root_dir=config.root_dir,
            data_path=config.data_path,
            model_ckpt = config.model_ckpt,
            num_train_epochs = params.num_train_epochs,
            warmup_steps = params.warmup_steps,
            per_device_train_batch_size = params.per_device_train_batch_size,
            weight_decay = params.weight_decay,
            logging_steps = params.logging_steps,
            evaluation_strategy = params.evaluation_strategy,
            eval_steps = params.evaluation_strategy,
            save_steps = params.save_steps,
            gradient_accumulation_steps = params.gradient_accumulation_steps
        )

        return model_trainer_config
