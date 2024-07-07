from src.InsurancePrediction.components.data_ingestion import DataIngestion
import os
import sys
from src.InsurancePrediction.logger import logging
from src.InsurancePrediction.exception import customexception
import pandas as pd



obj=DataIngestion()

obj.initiate_data_ingestion()