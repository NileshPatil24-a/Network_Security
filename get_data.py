import sys
import os 
import sys
import json 
import pandas as pd 
import numpy as np 
import pymongo
import certifi

from dotenv import load_dotenv
MONGO_DB_URL = os.getenv("MONGO_DB_URL")

ca = certifi.where()

from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.logger.logger import logging


class NetworkDataExtraction():
    def __int__(self):
        try:
            pass
        except Exception as e :
            raise NetworkSecurityException(e,sys)


    def csv_tojson_convertor(self):
        try:
            pass
        except Exception as e:
            raise NetworkSecurityException(e,sys)
    
    def pushing_data_to_mongodb(self):
        try:
            pass
        except Exception as e:
            raise NetworkSecurityException(e,sys)
        
if __name__ == "__main__":
    pass