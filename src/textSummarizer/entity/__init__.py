from dataclasses import dataclass  # Importing dataclass decorator
from pathlib import Path  # Importing Path class for working with file paths


@dataclass(frozen=True)  # Using dataclass decorator with frozen=True for immutability
class DataIngestionConfig:
    root_dir: Path  # Root directory for data ingestion
    source_URL: str  # URL from which data is ingested
    local_data_file: Path  # Local path where the data file is stored
    unzip_dir: Path  # Directory where the data file will be extracted (if applicable)


@dataclass(frozen=True)  # Using dataclass decorator with frozen=True for immutability
class DataValidationConfig:
    root_dir: Path  # Root directory for data validation
    STATUS_FILE: str  # File path for storing validation status
    ALL_REQUIRED_FILES: list  # List of all required files for validation


@dataclass(frozen=True)
class DataTransformationConfig:
    root_dir: Path            # Root directory for data transformation
    data_path: Path           # Path to the data directory
    tokenizer_name: Path      # Path to the tokenizer
    

@dataclass(frozen=True)
class ModelTrainerConfig:
    root_dir: Path
    data_path: Path
    model_ckpt: Path
    num_train_epochs: int
    warmup_steps: int
    per_device_train_batch_size: int
    weight_decay: float
    logging_steps: int
    evaluation_strategy: str
    eval_steps: int
    save_steps: float
    gradient_accumulation_steps: int
    
    
@dataclass(frozen=True)
class ModelEvaluationConfig:
    root_dir: Path
    data_path: Path
    model_path: Path
    tokenizer_path: Path
    metric_file_name: Path
