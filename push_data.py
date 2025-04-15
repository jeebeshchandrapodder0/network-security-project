import os
from dotenv import load_dotenv
import sys
import json

load_dotenv()

MONGO_DB_URL = os.getenv("MONGO_DB_URL") 
print(MONGO_DB_URL)

import certifi
ca = certifi.where() 

import pandas as pd 
import numpy as np 
import pymongo
from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.logging.logger import logging

class NetworkDataExtract():
    def __init__(self):
        try:
            pass
        except Exception as e:
            raise NetworkSecurityException(e, sys)

    def csv_to_json_convertor(self, file_path):
        try:
            data=pd.read_csv(file_path)
            data.reset_index(drop=True,inplace=True)
            records=list(json.loads(data.T.to_json()).values())
            return records
        except Exception as e:
            raise NetworkSecurityException(e,sys)
        
    def insert_data_mongodb(self, records,database, collection):
        try:
            self.database = database # database name
            self.collection = collection # collection name
            self.records = records # records
            
            self.mongo_client = pymongo.MongoClient(MONGO_DB_URL) # connecting to the mongodb
            self.database = self.mongo_client[self.database] # database name

            self.collection = self.database[self.collection] # collection name
            self.collection.insert_many(self.records) # inserting the records into the collection
            print("Pinged your deployment. You successfully connected to MongoDB! Hurray!")
            return len(self.records)
        except Exception as e:
            raise NetworkSecurityException(e, sys)
        
if __name__ == "__main__":
    FILE_PATH="Network_Data\phisingData.csv"
    DATABASE = "JeebeshAI_reboot"
    COLLECTION = "NetworkData"
    networkobj = NetworkDataExtract()
    records = networkobj.csv_to_json_convertor(file_path=FILE_PATH)
    no_of_records = networkobj.insert_data_mongodb(records, DATABASE, COLLECTION)
    print(f"No of records inserted: {no_of_records}")