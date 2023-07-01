import os
import sys
from src.exception import CustomException
from src.logger import logging
import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split
from dataclasses import dataclass

from src.components.data_transformation import DataTransformation 

@dataclass
class DataIngestionConfig:
    train_data_path: str=os.path.join('artifacts',"train.csv")
    test_data_path: str=os.path.join('artifacts',"test.csv")
    failure_data_path: str=os.path.join('artifacts',"failure_datapoints.csv")

class DataIngestion:
    def __init__(self):
        self.ingestion_config=DataIngestionConfig()

    def initiate_data_ingestion(self):
        logging.info("Entered the data ingestion method or component")
        try:
            df=pd.read_csv("D:\\Railway Dataset\\MetroPT3(AirCompressor).csv")
            logging.info('Read the dataset as dataframe')

            os.makedirs(os.path.dirname(self.ingestion_config.train_data_path),exist_ok=True)

            logging.info('Extracting failure data points from the given data with the provided information in the file provided in notebooks')

            failure1_dates = "2020-04-18 0:00 to 2020-04-18 23:59"
            failure2_dates = "2020-05-29 23:30 to 2020-05-30 6:00"
            failure3_dates = "2020-06-05 10:00 to 2020-06-07 14:30"
            failure4_dates = "2020-07-15 14:30 to 2020-07-15 19:00"

            df['timestamp'] = pd.to_datetime(df['timestamp'])

            condition1 = (df['timestamp'] >= pd.to_datetime(failure1_dates.split('to')[0])) & (df['timestamp'] <= pd.to_datetime(failure1_dates.split('to')[1]))
            condition2 = (df['timestamp'] >= pd.to_datetime(failure2_dates.split('to')[0])) & (df['timestamp'] <= pd.to_datetime(failure2_dates.split('to')[1]))
            condition3 = (df['timestamp'] >= pd.to_datetime(failure3_dates.split('to')[0])) & (df['timestamp'] <= pd.to_datetime(failure3_dates.split('to')[1]))
            condition4 = (df['timestamp'] >= pd.to_datetime(failure4_dates.split('to')[0])) & (df['timestamp'] <= pd.to_datetime(failure4_dates.split('to')[1]))

            condition = (condition1|condition2|condition3|condition4)

            failure_data_points = df[condition] 

            logging.info("Labelling of the dataset started")

            df['Failure'] = np.where(condition == True , 1 , 0)
            logging.info("Labelling of the dataset Completed")

            failure_data_points.to_csv(self.ingestion_config.failure_data_path)        



            logging.info("Train test split initiated")
            train_set,test_set=train_test_split(df,test_size=0.5,random_state=42)
            train_set = train_set.iloc[:,:]

            train_set.to_csv(self.ingestion_config.train_data_path,index=False,header=True)

            test_set.to_csv(self.ingestion_config.test_data_path,index=False,header=True)

            logging.info("Inmgestion of the data iss completed")

            return(
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path

            )
        except Exception as e:
            raise CustomException(e,sys)
        
if __name__ == '__main__':
    obj = DataIngestion()
    train_p ,test_p  = obj.initiate_data_ingestion()
    train = pd.read_csv(train_p)
    test = pd.read_csv(test_p)

    print(train.columns , test.shape)

    obj1 = DataTransformation() 
    train_array , test_array , _  = obj1.initiate_data_transformation(train_path=train_p,test_path=test_p)

    print(train_array[0],test_array[0])

