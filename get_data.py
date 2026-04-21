import pymongo
import sys
import os 
import sys
import json 
import pandas as pd 
import numpy as np 
import pymongo
import certifi

from dotenv import load_dotenv
load_dotenv()
MONGO_DB_URL = os.getenv("MONGO_DB_URL")
print(MONGO_DB_URL)
ca = certifi.where()

from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.logger.logger import logging


class NetworkDataExtraction():
    def __int__(self):
        try:
            pass
        except Exception as e :
            raise NetworkSecurityException(e,sys)


    def csv_tojson_convertor(self,file_path):
        try:
            data = pd.read_csv(file_path)
            data.reset_index(drop=True, inplace=True)
            records=list(json.loads(data.T.to_json()).values())
            return records
        except Exception as e:
            raise NetworkSecurityException(e,sys)
    
    def pushing_data_to_mongodb(self,records,database, collection):
        try:
            self.records = records
            self.database = database
            self.collection = collection
            self.mongo_client = pymongo.MongoClient(MONGO_DB_URL)

            self.database = self.mongo_client[self.database]
            self.collection = self.database[self.collection]

            self.collection.insert_many(self.records)
            return len(self.records)


        except Exception as e:
            raise NetworkSecurityException(e,sys)
        
if __name__ == "__main__":
    FILE_PATH = "Network_data/NetworkData.csv"
    DATABASE = "projectdata"
    COLLECTION = "NetworkData"
    newtworkObj = NetworkDataExtraction()
    records = newtworkObj.csv_tojson_convertor(FILE_PATH)
    print(newtworkObj.pushing_data_to_mongodb(records,DATABASE,COLLECTION))
