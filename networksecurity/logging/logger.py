import logging
import os
from datetime import datetime

LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"

logs_path = os.path.join(os.getcwd(), "logs", LOG_FILE) #get current working directory
os.makedirs(logs_path, exist_ok=True) #create logs directory if it doesn't exist

LOG_FILE_PATH = os.path.join(logs_path, LOG_FILE) #join logs path and log file

logging.basicConfig(
    filename=LOG_FILE_PATH, #log file path
    format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s", #log format
    level=logging.INFO, #log level
)

if __name__ == "__main__":
    logging.info("Logging has started")
