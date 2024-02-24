import os
import urllib.request as request  # Module for working with URLs
import zipfile  # Module for working with ZIP archives
from src.textSummarizer.logging import logger  # Importing logger for logging messages
from src.textSummarizer.utils.common import get_size  # Importing a function for getting file size
from pathlib import Path  # Module for working with file paths
from src.textSummarizer.entity import DataIngestionConfig  # Importing DataIngestionConfig class


class DataIngestion:
    def __init__(self, config: DataIngestionConfig):
        self.config = config

    def download_file(self):
        # Check if the local data file already exists
        if not os.path.exists(self.config.local_data_file):
            # If not, download the file from the source URL
            filename, headers = request.urlretrieve(
                url=self.config.source_URL,
                filename=self.config.local_data_file
            )
            # Log a message indicating successful download
            logger.info(f"{filename} downloaded! with following info: \n{headers}")
        else:
            # If the file already exists, log its size
            logger.info(f"File already exists of size: {get_size(Path(self.config.local_data_file))}")

    def extract_zip_file(self):
        """
        Extracts the contents of a ZIP file into the specified directory.
        """
        # Create the directory for extraction if it doesn't exist
        unzip_path = self.config.unzip_dir
        os.makedirs(unzip_path, exist_ok=True)
        
        # Open the ZIP file and extract its contents to the specified directory
        with zipfile.ZipFile(self.config.local_data_file, 'r') as zip_ref:
            zip_ref.extractall(unzip_path)
