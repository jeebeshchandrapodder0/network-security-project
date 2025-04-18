from datetime import datetime
import os
from networksecurity.constants import training_pipeline

print(training_pipeline.PIPELINE_NAME)
print(training_pipeline.ARTIFACT_DIR)

class TrainingPipelineConfig: ## This class is used to configure the training pipeline. Generic Code
    def __init__(self, timestamp=datetime.now()):
        timestamp=timestamp.strftime("%m_%d_%Y_%H_%M_%S") # This is the timestamp of the training pipeline.
        self.pipeline_name = training_pipeline.PIPELINE_NAME # This is the name of the training pipeline.
        self.artifact_dir = os.path.join(training_pipeline.ARTIFACT_DIR, timestamp) # This is the directory of the training pipeline.
        self.timestamp = timestamp # This is the timestamp of the training pipeline.

class DataIngestionConfig: ## This class is used to configure the data ingestion. Generic Code
    def __init__(self, training_pipeline_config: TrainingPipelineConfig): 
        self.database_name = training_pipeline.DATA_INGESTION_DATABASE_NAME # This is the name of the database.
        self.collection_name = training_pipeline.DATA_INGESTION_COLLECTION_NAME # This is the name of the collection.
        self.data_ingestion_dir:str = os.path.join(training_pipeline_config.artifact_dir, 
                                                   training_pipeline.DATA_INGESTION_DIR_NAME) # This is the directory of the data ingestion.
        self.feature_store_file_path:str = os.path.join(self.data_ingestion_dir, 
                                                        training_pipeline.DATA_INGESTION_FEATURE_STORE_DIR, 
                                                        training_pipeline.FILE_NAME) # This is the path of the feature store file.
        self.training_file_path:str = os.path.join(self.data_ingestion_dir, 
                                                   training_pipeline.DATA_INGESTION_INGESTED_DIR, 
                                                   training_pipeline.TRAIN_FILE_NAME) # This is the path of the training file.
        self.testing_file_path:str = os.path.join(self.data_ingestion_dir, 
                                                  training_pipeline.DATA_INGESTION_INGESTED_DIR, 
                                                  training_pipeline.TEST_FILE_NAME) # This is the path of the testing file.
        self.train_test_split_ratio:float = training_pipeline.DATA_INGESTION_TRAIN_TEST_SPLIT_RATION # This is the ratio of the train test split.

class DataValidationConfig:
    def __init__(self,training_pipeline_config:TrainingPipelineConfig):
        self.data_validation_dir: str = os.path.join( training_pipeline_config.artifact_dir, training_pipeline.DATA_VALIDATION_DIR_NAME)
        self.valid_data_dir: str = os.path.join(self.data_validation_dir, training_pipeline.DATA_VALIDATION_VALID_DIR)
        self.invalid_data_dir: str = os.path.join(self.data_validation_dir, training_pipeline.DATA_VALIDATION_INVALID_DIR)
        self.valid_train_file_path: str = os.path.join(self.valid_data_dir, training_pipeline.TRAIN_FILE_NAME)
        self.valid_test_file_path: str = os.path.join(self.valid_data_dir, training_pipeline.TEST_FILE_NAME)
        self.invalid_train_file_path: str = os.path.join(self.invalid_data_dir, training_pipeline.TRAIN_FILE_NAME)
        self.invalid_test_file_path: str = os.path.join(self.invalid_data_dir, training_pipeline.TEST_FILE_NAME)
        self.drift_report_file_path: str = os.path.join(
            self.data_validation_dir,
            training_pipeline.DATA_VALIDATION_DRIFT_REPORT_DIR,
            training_pipeline.DATA_VALIDATION_DRIFT_REPORT_FILE_NAME,
        )