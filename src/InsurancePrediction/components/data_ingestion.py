import pandas as pd
import numpy as np
import os
from src.InsurancePrediction.logger import logging
from sklearn.model_selection import train_test_split

from src.InsurancePrediction.exception import customexception
from pathlib import Path


class DataIngestionConfig:
    raw_data_path:str=os.path.join("artifacts","raw.csv")
    train_data_path:str=os.path.join("artifacts","train.csv")
    test_data_path:str=os.path.join("artifacts","test.csv")


class DataIngestion:
    def __init__(self):
        self.ingestion_configDataIngestionConfig()

    def initiate_data_ingestion(self):
        logging.info("data ingestion started")

        try:
            data=pd.read_csv(Path(os.path.join("notebook/data",'insurance.csv')))
            logging.info('i have performed train test split')

            os.makedirs(os.path.join(self.ingestion_config.raw_data_path),exists=True)
            data.to_csv(self.ingestion_config.raw_data_path,index=False)
            logging.info('i have saved the raw data in artifact folder')


            
            train_data,test_data=train_test_split(data,test_size=0.25)
            logging.info("train test split completed")





        except Exception as e:
            pass