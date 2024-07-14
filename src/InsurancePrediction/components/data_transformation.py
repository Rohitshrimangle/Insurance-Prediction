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

@dataclass
class DataTransformationConfig:
    preprocessor_obj_file_path = os.path.join('artifacts', 'preprocessor.pkl')

class DataTransformation:
    def __init__(self):
        self.data_transformation_config = DataTransformationConfig()

    def get_data_transformation(self):
        try:
            logging.info('Data Transformation initiated')
            
            # Define which columns should be ordinal-encoded and which should be scaled
            categorical_cols = ['sex', 'smoker', 'region']
            numerical_cols = ['age', 'bmi', 'children']
            
            # Define the custom ranking for each ordinal variable
            sex_categories = ['male', 'female']
            smoker_categories = ['no', 'yes']
            region_categories = ['southeast', 'southwest', 'northwest', 'northeast']
            
            logging.info('Pipeline Initiated')
            
            ## Numerical Pipeline
            num_pipeline = Pipeline(
                steps=[
                    ('imputer', SimpleImputer(strategy='median')),
                    ('scaler', StandardScaler())
                ]
            )
            
            # Categorical Pipeline
            cat_pipeline = Pipeline(
                steps=[
                    ('imputer', SimpleImputer(strategy='most_frequent')),
                    ('ordinalencoder', OrdinalEncoder(categories=[sex_categories, smoker_categories, region_categories])),
                    ('scaler', StandardScaler())
                ]
            )
            
            preprocessor = ColumnTransformer(
                transformers=[
                    ('num_pipeline', num_pipeline, numerical_cols),
                    ('cat_pipeline', cat_pipeline, categorical_cols)
                ]
            )
            
            return preprocessor
        
        except Exception as e:
            logging.info("Exception occurred in get_data_transformation")
            raise customexception(e, sys)

    def initialize_data_transformation(self, train_path, test_path):
        try:
            train_df = pd.read_csv(train_path)
            test_df = pd.read_csv(test_path)
            
            logging.info("Read train and test data complete")
            logging.info(f'Train Dataframe Columns: {train_df.columns}')    #imp role played to remove a hectic error
            logging.info(f'Test Dataframe Columns: {test_df.columns}')      #imp role played to remove a hectic error
            logging.info(f'Train Dataframe Head: \n{train_df.head().to_string()}')
            logging.info(f'Test Dataframe Head: \n{test_df.head().to_string()}')
            
            preprocessing_obj = self.get_data_transformation()
            
            target_column_name = 'expenses'
            drop_columns = [target_column_name]
            
            logging.info(f'Dropping columns: {drop_columns}')
            
            # Ensure target column exists (#imp role played to remove a hectic error)
            if target_column_name not in train_df.columns:
                logging.error(f"Target column '{target_column_name}' not found in train_df")
                raise ValueError(f"Target column '{target_column_name}' not found in train_df")
            
            if target_column_name not in test_df.columns:
                logging.error(f"Target column '{target_column_name}' not found in test_df")
                raise ValueError(f"Target column '{target_column_name}' not found in test_df")
            
            input_feature_train_df = train_df.drop(columns=drop_columns, axis=1)
            target_feature_train_df = train_df[target_column_name]
            
            input_feature_test_df = test_df.drop(columns=drop_columns, axis=1)
            target_feature_test_df = test_df[target_column_name]
            
            logging.info(f'Input Feature Train DataFrame Columns: {input_feature_train_df.columns}')
            logging.info(f'Input Feature Test DataFrame Columns: {input_feature_test_df.columns}')
            
            # Ensure columns match expected columns in preprocessing (#imp role played to remove a hectic error)
            expected_columns = preprocessing_obj.transformers[0][2] + preprocessing_obj.transformers[1][2]
            missing_columns_train = set(expected_columns) - set(input_feature_train_df.columns)
            missing_columns_test = set(expected_columns) - set(input_feature_test_df.columns)
            
            #imp role played to remove a hectic error
            if missing_columns_train:
                logging.error(f"Missing columns in train_df: {missing_columns_train}")
                raise ValueError(f"Missing columns in train_df: {missing_columns_train}")
            
            if missing_columns_test:
                logging.error(f"Missing columns in test_df: {missing_columns_test}")
                raise ValueError(f"Missing columns in test_df: {missing_columns_test}")
            
            input_feature_train_arr = preprocessing_obj.fit_transform(input_feature_train_df)
            input_feature_test_arr = preprocessing_obj.transform(input_feature_test_df)
            
            logging.info("Applying preprocessing object on training and testing datasets.")
            
            train_arr = np.c_[input_feature_train_arr, np.array(target_feature_train_df)]
            test_arr = np.c_[input_feature_test_arr, np.array(target_feature_test_df)]

            save_object(
                file_path=self.data_transformation_config.preprocessor_obj_file_path,
                obj=preprocessing_obj
            )
            
            logging.info("Preprocessing pickle file saved")
            
            return (
                train_arr,
                test_arr
            )
        
        except Exception as e:
            logging.info("Exception occurred in initialize_data_transformation")
            raise customexception(e, sys)
