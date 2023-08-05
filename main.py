import numpy as np
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Activation , Dense ,Flatten ,BatchNormalization,Conv2D,MaxPool2D,Dropout
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.metrics import categorical_crossentropy
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from sklearn.metrics import confusion_matrix
import itertools
import os
import shutil
from keras.preprocessing import image
import random
from tensorflow.keras.layers import MaxPooling2D
from tensorflow.keras.layers import Dense, Dropout, Flatten
import glob
from IPython.display import display
from PIL import Image
import numberPlateExtraction
import warnings
from keras import backend as K
import cv2
import requests
import time
import datetime


gpu_options = tf.GPUOptions(per_process_gpu_memory_fraction=0.333) 
sess = tf.Session(config=tf.ConfigProto(log_device_placement=True, gpu_options=gpu_options))
#Insert the accident details into the database
def insertRecord(severity, listnp):
    ts = time.time()
    date = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
    location = 'Camera Location 1'

    URL = "http://localhost:3000/records/insert"

    req_params = {
        'date': date,
        'severity': severity,
        'location': location,
        'numberplates': listnp,
        'authorityDetails': '8380989839'
    }
    response = requests.post(url = URL, json = req_params)


#Send alert to the contact number
def sendAlert():
    url = "https://www.fast2sms.com/dev/bulk"
    payload = "sender_id=FSTSMS&message=https://www.google.co.in/maps/place/McDonald's/@18.6363705,73.7943848,17z/data=!3m1!4b1!4m5!3m4!1s0x3bc2b84b10bf9457:0x3a3edd5ea8386546!8m2!3d18.6363763!4d73.7965809?hl=en&authuser=0&language=english&route=p&numbers=8380989839"
    headers = {
        'authorization': "5J0mFQR26AS3YpcjIb4XNioxGw9vUK8enWyOf7PMaEDdukBtTrq97JYCic8jwhmDzaZQLugXs6KyUNI0",
        'Content-Type': "application/x-www-form-urlencoded",
        'Cache-Control': "no-cache",
    }
    response = requests.request("POST", url, data=payload, headers=headers)
    print(response.text)


def accidentDetection():
    alertFlag = False
    new_model = tf.keras.models.load_model('model3.h5')
    loc = 'H:/Modifications_SS/frames/frame.jpg'
    img_pred = image.load_img(loc,target_size=(276,183))
    img_pred = image.img_to_array(img_pred)
    img_pred = np.expand_dims(img_pred,axis =0)
    print("------------------------------------")
    result = (new_model.predict(img_pred))
    print(result)
    if(result[0][0] == 1.0):
        severity = "Car Road Accident"
        alertFlag = True
    elif(result[0][1] == 1.0):
        severity = "Car Fire"
        alertFlag = True
    else:
        print("No anomaly detected")
    
    '''The below functions are commented so that the database is not flooded while testing
        and alerts are not generated '''
        
    if(alertFlag):
            #sendAlert()
            return severity


