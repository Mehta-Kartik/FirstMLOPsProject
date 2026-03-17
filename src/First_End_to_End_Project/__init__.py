import os
import sys
import logging

# Define log message format: time, level, module, and message
loggin_str = "[%(asctime)s:%(levelname)s:%(module)s:%(message)s]"

# Folder name where log file will be stored
log_dir = "logs"
# Full path of the log file inside the logs directory
log_filepath = os.path.join(log_dir, "logging.log")

# Create logs directory if it does not already exist
os.makedirs(log_dir, exist_ok=True)

# Configure the root logger: level, format, and output handlers
logging.basicConfig(
    level=logging.INFO,          # Set minimum log level to INFO
    format=loggin_str,           # Use the format defined above
    handlers=[
        logging.FileHandler(log_filepath),   # Write logs to file
        logging.StreamHandler(sys.stdout)    # Also print logs to console
    ]
)


logger=logging.getLogger('First_End_to_End_Project')