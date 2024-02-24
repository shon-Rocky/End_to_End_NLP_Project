import os  # Module for interacting with the operating system
from src.textSummarizer.logging import logger  # Importing logger for logging messages
from src.textSummarizer.entity import DataValidationConfig  # Importing DataValidationConfig class


class DataValidation:
    def __init__(self, config: DataValidationConfig):
        self.config = config

    def validate_all_files_exist(self) -> bool:
        try:
            validation_status = None  # Initialize validation status
            
            # Get a list of all files in the specified directory
            all_files = os.listdir(os.path.join("artifacts", "data_ingestion", "samsum_dataset"))

            # Iterate through each file
            for file in all_files:
                # Check if the file is not in the list of required files
                if file not in self.config.ALL_REQUIRED_FILES:
                    validation_status = False  # Set validation status to False
                    with open(self.config.STATUS_FILE, 'w') as f:
                        f.write(f"Validation status: {validation_status}")  # Write validation status to file
                else:
                    validation_status = True  # Set validation status to True
                    with open(self.config.STATUS_FILE, 'w') as f:
                        f.write(f"Validation status: {validation_status}")  # Write validation status to file

            return validation_status  # Return the final validation status

        except Exception as e:
            raise e  # Re-raise any exceptions that occur
