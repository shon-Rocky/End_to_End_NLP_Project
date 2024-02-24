# Import necessary modules and classes
from src.textSummarizer.config.configuration import ConfigurationManager  # Importing ConfigurationManager class
from src.textSummarizer.conponents.data_ingestion import DataIngestion  # Importing DataIngestion class
from src.textSummarizer.logging import logger  # Importing logger for logging messages


class DataIngestionTrainingPipeline:
    def __init__(self):
        pass  # Constructor does nothing in this case

    def main(self):
        # Initialize ConfigurationManager to manage configurations
        config = ConfigurationManager()
        
        # Get data ingestion configuration from ConfigurationManager
        data_ingestion_config = config.get_data_ingestion_config()
        
        # Instantiate DataIngestion object with the obtained configuration
        data_ingestion = DataIngestion(config=data_ingestion_config)
        
        # Perform data ingestion steps: download file and extract ZIP file
        data_ingestion.download_file()
        data_ingestion.extract_zip_file()
