import os
import sys
import pandas as pd
import numpy as np
from dataclasses import dataclass
from src.InsurancePrediction.exception import customexception
from src.InsurancePrediction.logger import logging

from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OrdinalEncoder, StandardScaler

from src.InsurancePrediction.utils.utils import save_object

class DataTransformationConfig:
    preproccessor_obj_file_path=os.path.join("artifacts","preprocessor.pk1")

class DataTransformation:
    def __init__(self):
        self.data_transformation_config=DataTransformationConfig()



    def get_data_transformation(self):
        
        try:

            logging.info("Data Transformation initiated")

            categorical_cols = ['sex','smoker','region']
            numerical_cols = ['age','bmi','children','expenses']

            sex_categories = ['male', 'female']
            smoker_categories = ['no', 'yes']
            region_categories = ['southwest','southeast','northeast','northwest']

            logging.info('Pipeline initiated')

            num_pipeline=Pipeline(
                steps=[
                    ('imputer',SimpleImputer(strategy='median')),
                    ('scaler', StandardScaler())
                ]
            )

            cat_pipeline=Pipeline(
                steps=[
                    ('imputer',SimpleImputer(strategy='most_frequent')),
                    ('ordinalencoder',OrdinalEncoder(categories=['sex_categories','smoker_categories','region_categories'])),
                    ('scaler',StandardScaler())
                ]
            )

            Preprocessor=ColumnTransformer([
                ('num_pipeline',num_pipeline,numerical_cols),
                ('cat_pipeline',cat_pipeline,categorical_cols)
            ])

            return Preprocessor

        except Exception as e:
            logging.info("Exception occcured in the initiate_datatransformation")

            raise customexception(e,sys)

    def initialize_data_transformation(self,train_path,test_path):

        try:
            train_df=pd.read_csv(train_path)
            test_df=pd.read_csv(test_path)

            logging.info("read train and test data completly")
            logging.info(f"Train Dataframe Head:\n{train_df.head().to.string()}")
            logging.info(f"Test Dataframe Head:\n{test_df.head().to.string()}")

            preprocessor_obj = self.get_data_transformation()

            target_column_name = 'expense'
            drop_columns = [target_column_name,'id']

            input_feature_train_df = train_df.drop(columns=drop_columns,axis=1)
            target_feature_train_df=train_df[target_column_name]


            input_feature_test_df = test_df.drop(columns=drop_columns,axis=1)
            target_feature_test_df=test_df[target_column_name]

            input_feature_train_arr= preprocessor_obj.fit_transform(input_feature_train_df)

            input_feature_test_arr= preprocessor_obj.transform(input_feature_test_df)

            logging.info("Applying preprocessing object on training ans testing datasets.")


            train_arr = np.c_[input_feature_train_arr,np.arry(target_feature_train_df)]
            test_arr = np.c_[input_feature_test_arr,np.arry(target_feature_test_df)]

            save_object(
                file_path=self.data_transformation_config.preproccessor_obj_file_path,
                obj=preprocessor_obj
            )

            logging.info('Preprocessor pickle file saved')


            return(
                train_arr,
                test_arr
            )


        except Exception as e:
            logging.info("Exception occcured in the initiate_datatransformation")

            raise customexception(e,sys)