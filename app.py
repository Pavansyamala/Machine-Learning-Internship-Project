from flask import Flask,request,render_template
import numpy as np
import pandas as pd

from sklearn.preprocessing import StandardScaler
from src.pipeline.prediction_pipeline import CustomData,PredictPipeline

application=Flask(__name__)

app=application

## Route for a home page

@app.route('/')
def index():
    return render_template('index.html') 

@app.route('/predictdata',methods=['GET','POST'])
def predict_datapoint():
    if request.method=='GET':
        return render_template('home.html')
    else:
        data=CustomData(
            TP2= np.float32(request.form.get('TP2')) ,
            TP3 = np.float32(request.form.get('TP3')),
            H1 = np.float32(request.form.get('H1')),
            DV_pressure = np.float32(request.form.get('DV_pressure')) ,
            Reservoirs = np.float32(request.form.get('Reservoirs')) ,
            Oil_temperature = np.float32(request.form.get('Oil_temperature')),
            Motor_current = np.float32(request.form.get('Motor_current')) ,
            COMP =  np.float32(request.form.get('COMP')),
            DV_eletric = np.float32(request.form.get('DV_eletric')),
            Towers = np.float32(request.form.get('Towers')),
            MPG = np.float32(request.form.get('MPG')),
            LPS = np.float32(request.form.get('LPS')), 
            Pressure_switch = np.float32(request.form.get('Pressure_switch')),
            Oil_level = np.float32(request.form.get('Oil_level')),
            Caudal_impulses = np.float32(request.form.get('Caudal_impulses'))
        )
        pred_df=data.get_data_as_frame()
        print(pred_df)
        print("Before Prediction")

        predict_pipeline=PredictPipeline()
        print("Mid Prediction")
        results=predict_pipeline.predict(pred_df)
        print("after Prediction")
        if results[0] == 0 :
             return render_template('home.html',results= 'Non-Failure')
        else :
            return render_template('home.html',results= 'Failure')
    

if __name__=="__main__":
    app.run(host="0.0.0.0",debug = True) 