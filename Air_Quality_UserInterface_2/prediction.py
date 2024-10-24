import pickle
import numpy as np
from lib_file import lib_path
import pandas as pd


with open(file='models/RandomForest_model.pkl', mode='rb') as file:
    model = pickle.load(file=file)


class_labels = ['Good', 'Moderate', 'Poor',
                'Satisfactory', 'Severe', 'Very Poor']


def AirQualityPrediction(input_data):

    # input_data = [PM_value, NO_value, NH3_value, NOx_value, CO_value,
    #               SO2_value, O3_value, Benzene_value, Toluene_value, AQI_value]

    input_data = np.array(input_data)

    prediction = model.predict_proba(input_data)
    class_label = class_labels[np.argmax(prediction[0])]
    probability = prediction[0][np.argmax(prediction[0])]*100.0

    print(f'class label: {class_label}')
    print(f'probability: {probability}')

    return class_label, probability
