import os 
import sys 

from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.logger.logger import logging
from networksecurity.pipelines.traininig_pipeline import TrainingPipeline


def start_trainig():
    try:
        pass
    except Exception as e:
        raise NetworkSecurityException(e, sys)
if __name__ == "__main__":
    start_trainig()
