from src.InsurancePrediction.components.data_ingestion import DataIngestion
import os
import sys
import pandas as pd
from src.InsurancePrediction.logger import logging
from src.InsurancePrediction.exception import customexception
import pandas as pd
from src.InsurancePrediction.components.data_transformation import DataTransformation
from src.InsurancePrediction.components import data_transformation
from src.InsurancePrediction.components.model_trainer import ModelTrainer
from src.InsurancePrediction.components import model_trainer

obj=DataIngestion()

train_data_path,test_data_path = obj.initiate_data_ingestion()

data_transformation = DataTransformation()

train_arr,test_arr = data_transformation.initialize_data_transformation(train_data_path,test_data_path)


model_trainer_obj=ModelTrainer()
model_trainer.initiate_model_training(train_arr,test_arr)



