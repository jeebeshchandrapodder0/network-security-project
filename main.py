import sys
import os
from dotenv import load_dotenv

from networksecurity.components.data_ingestion import DataIngestion
from networksecurity.entity.config_entity import DataIngestionConfig, TrainingPipelineConfig
from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.logging.logger import logging

# Load environment variables
load_dotenv()

def main():
    try:
        logging.info("Starting data ingestion pipeline")
        
        # Initialize configuration
        trainingpipelineconfig = TrainingPipelineConfig()
        dataingestionconfig = DataIngestionConfig(trainingpipelineconfig)
        
        # Create data ingestion instance
        data_ingestion = DataIngestion(dataingestionconfig)
        logging.info("Data ingestion component initialized")
        
        # Start data ingestion
        logging.info("Starting data ingestion process")
        dataingestionartifact = data_ingestion.initiate_data_ingestion()
        
        # Log results
        logging.info(f"Data ingestion completed successfully")
        logging.info(f"Training file path: {dataingestionartifact.trained_file_path}")
        logging.info(f"Test file path: {dataingestionartifact.test_file_path}")
        
        return dataingestionartifact
        
    except Exception as e:
        logging.error(f"Error in data ingestion pipeline: {str(e)}")
        raise NetworkSecurityException(e, sys)

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        logging.error(f"Pipeline failed: {str(e)}")
        sys.exit(1)
