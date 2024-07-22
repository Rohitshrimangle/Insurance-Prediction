import os
import pandas as pd
import sys
from src.InsurancePrediction.exception import customexception
from  src.InsurancePrediction.logger import logging
from src.InsurancePrediction.utils.utils import load_object


class PredictPipeline:
    def __init__(self):
        pass

    def predict(self,features):
        try:
            preprocessor_path=os.path.join('artifacts','preprocessor.pk1')
            model_path=os.path.join('artifacts','model.pk1')

            preprocessor=load_object(preprocessor_path)
            model=load_object(model_path)

            scaled_data=preprocessor.trasnform(features)

            pred=model.predict(scaled_data)

            return pred

        except Exception as e:
            raise customexception(e,sys)