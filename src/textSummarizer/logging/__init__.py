import sys  # Importing the sys module for system-specific parameters and functions
import logging  # Importing the logging module for logging functionality
import os

# Defining the logging format string
logging_str = "[%(asctime)s: %(levelname)s: %(module)s: %(message)s]"

# Defining the directory for log files
log_dir = 'logs'

# Joining the log directory with the log file name
log_filepath = os.path.join(log_dir, "running_logs.log")

# Creating the log directory if it doesn't exist
os.makedirs(log_dir, exist_ok=True)

# Configuring the logging module
logging.basicConfig(
    level=logging.INFO,  # Setting the logging level to INFO
    format=logging_str,  # Setting the logging format to the defined format string
    
    # Defining handlers for logging output
    handlers=[
        logging.FileHandler(log_filepath),  # Adding a file handler for writing logs to a file
        logging.StreamHandler(sys.stdout)   # Adding a stream handler for printing logs to the console
    ]
)

# Creating a logger object
logger = logging.getLogger("textSummarizerLogger")
