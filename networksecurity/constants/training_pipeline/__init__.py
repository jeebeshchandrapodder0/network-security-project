import os
import sys
import numpy as np
import pandas as pd

"""
defining common constant variable for training pipeline
"""
TARGET_COLUMN = "Result"
PIPELINE_NAME: str = "NetworkSecurity" #This gives a name to your project or training pipeline.
ARTIFACT_DIR: str = "Artifacts" #An "artifact" is any file the training process creates — models, processed data, logs, etc. 
                                    #This constant defines the folder where all those files will be saved.
FILE_NAME: str = "phisingData.csv" #This constant defines the name of the dataset file.

TRAIN_FILE_NAME: str = "train.csv" #This constant defines the name of the training dataset file.
TEST_FILE_NAME: str = "test.csv" #This constant defines the name of the testing dataset file.

SCHEMA_FILE_PATH = os.path.join("data_schema", "schema.yaml") #This constant defines the path to the schema file.

SAVED_MODEL_DIR =os.path.join("saved_models") #This constant defines the path to the directory where the trained model will be saved.
MODEL_FILE_NAME = "model.pkl" #This constant defines the name of the trained model file.

"""
Data Ingestion related constant start with DATA_INGESTION VAR NAME
"""
DATA_INGESTION_COLLECTION_NAME: str = "NetworkData" # collection name
DATA_INGESTION_DATABASE_NAME: str = "JeebeshAI_reboot" # database name
DATA_INGESTION_DIR_NAME: str = "data_ingestion" # directory name
DATA_INGESTION_FEATURE_STORE_DIR: str = "feature_store" # feature store directory
DATA_INGESTION_INGESTED_DIR: str = "ingested" # ingested directory
DATA_INGESTION_TRAIN_TEST_SPLIT_RATION: float = 0.2 # train test split ratio

"""
Data Validation related constant start with DATA_VALIDATION VAR NAME
"""
DATA_VALIDATION_DIR_NAME: str = "data_validation"
DATA_VALIDATION_VALID_DIR: str = "validated"
DATA_VALIDATION_INVALID_DIR: str = "invalid"
DATA_VALIDATION_DRIFT_REPORT_DIR: str = "drift_report"
DATA_VALIDATION_DRIFT_REPORT_FILE_NAME: str = "report.yaml"
PREPROCESSING_OBJECT_FILE_NAME = "preprocessing.pkl"


