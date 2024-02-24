# Import necessary modules and classes
from src.textSummarizer.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from src.textSummarizer.pipeline.stage_02_data_validation import DataValidationTrainingPipeline
from src.textSummarizer.pipeline.stage_03_data_transformation import DataTransformationTrainingPipeline
from src.textSummarizer.pipeline.stage_04_model_trainer import ModelTrainerTrainingPipeline
from src.textSummarizer.logging import logger

# Define the stage name for the first stage
STAGE_NAME = "Data Ingestion stage"

try:
    # Log a message indicating the start of the stage
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<") 
    # Instantiate the DataIngestionTrainingPipeline class
    data_ingestion = DataIngestionTrainingPipeline()
    # Call the main method of the DataIngestionTrainingPipeline class
    data_ingestion.main()
    # Log a message indicating the completion of the stage
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
    # If an exception occurs, log the exception and raise it
    logger.exception(e)
    raise e

# Define the stage name for the second stage
STAGE_NAME = "Data Validation stage"

try:
    # Log a message indicating the start of the stage
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<") 
    # Instantiate the DataValidationTrainingPipeline class
    data_validation = DataValidationTrainingPipeline()
    # Call the main method of the DataValidationTrainingPipeline class
    data_validation.main()
    # Log a message indicating the completion of the stage
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
    # If an exception occurs, log the exception and raise it
    logger.exception(e)
    raise e


STAGE_NAME = "Data Transformation stage"

try:
    # Log a message indicating the start of the stage
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<") 
    # Instantiate the DataValidationTrainingPipeline class
    data_transformation = DataTransformationTrainingPipeline()
    # Call the main method of the DataValidationTrainingPipeline class
    data_transformation.main()
    # Log a message indicating the completion of the stage
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
    # If an exception occurs, log the exception and raise it
    logger.exception(e)
    raise e


STAGE_NAME = "Model Trainer stage"

try:
    # Log a message indicating the start of the stage
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<") 
    # Instantiate the DataValidationTrainingPipeline class
    model_trainer = ModelTrainerTrainingPipeline()
    # Call the main method of the DataValidationTrainingPipeline class
    model_trainer.main()
    # Log a message indicating the completion of the stage
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
    # If an exception occurs, log the exception and raise it
    logger.exception(e)
    raise e
