import sys 
import pandas as pd 
from src.exception import CustomException 
from src.utils import load_object 

class PredictPipeline :
    def __init__(self):
        pass 
    def predict(self,features):
        try :
            model_path = 'D:\\ML\\artifacts\\model.pkl'
            preprocessor_path = 'D:\\ML\\artifacts\\proprocessor.pkl'
            model = load_object(file_path = model_path)
            preprocessor = load_object(file_path=preprocessor_path)
            data_scaled = preprocessor.transform(features)
            prediction = model.predict(data_scaled)
            return prediction
        except Exception as e :
            raise CustomException(e,sys)

class CustomData:
    def __init__(self,
                 TP2 : float ,
                 TP3 : float ,
                 H1 : float,
                 DV_pressure :float ,
                 Reservoirs : float ,
                 Oil_temperature : float,
                 Motor_current : float ,
                 COMP : float,
                 DV_eletric : float,
                 Towers : float,
                 MPG : float,
                 LPS : float, 
                 Pressure_switch : float ,
                 Oil_level : float,
                 Caudal_impulses : float
                 ):
        self.TP2 = TP2
        self.TP3 = TP3
        self.H1 = H1
        self.DV_pressure = DV_pressure
        self.Reservoirs = Reservoirs
        self.Oil_temperature = Oil_temperature
        self.Motor_current = Motor_current 
        self.COMP = COMP 
        self.DV_electric = DV_eletric 
        self.Towers = Towers 
        self.MPG = MPG 
        self.LPS = LPS 
        self.Pressure_switch = Pressure_switch 
        self.Oil_level = Oil_level 
        self.caudal_impulses = Caudal_impulses 
    def get_data_as_frame(self):
        try :
            custom_data_input = {
                'TP2':self.TP2, 
                'TP3':self.TP3,
                'H1':self.H1,
                'DV_pressure':self.DV_pressure,
                'Reservoirs':self.Reservoirs,
                'Oil_temperature':self.Oil_temperature, 
                'Motor_current':self.Motor_current,
                'COMP':self.COMP,
                'DV_eletric':self.DV_electric,
                'Towers':self.Towers,
                'MPG':self.MPG,
                'LPS':self.LPS,
                'Pressure_switch':self.Pressure_switch,
                'Oil_level':self.Oil_level,
                'Caudal_impulses':self.caudal_impulses
            } 
            return pd.DataFrame(custom_data_input,index=[0])
        except Exception as e :
            raise CustomException(e,sys)