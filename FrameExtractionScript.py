# -*- coding: utf-8 -*-
"""

"""

import cv2
import requests
import time
import datetime
import main
import numberPlateExtraction

def extractFramesFromVideo():
    #Give the path of the video to be evaluated
    video = cv2.VideoCapture('sample1.mp4')
    framesTrue = 1
    recordInserted = 0
    frameNo = 0
    while framesTrue:
        framesTrue, frame = video.read()
        if(framesTrue):
            cv2.imwrite('***.jpg', frame)
            cv2.imwrite('***.jpg', frame)
            for i in range(20):
                framesTrue, frame = video.read()
            print(frameNo)
            #Call to the detection function in main.py
            value = main.accidentDetection()
            print(value)
            if(value == "Car Road Accident" or value == "Car Fire"):
                listNP = []
                for j in range(5):
                    if(framesTrue):
                        cv2.imwrite('***.jpg', frame)
                        numberPlate = numberPlateExtraction.getNumberPlate()
                        if(numberPlate != "None"):
                            print("Number Plate:",numberPlate)
                            print(value)
                            listNP.append(numberPlate)
                            
                        else:
                            print("No number plate detected")
                        framesTrue, frame = video.read()
                        frameNo += 1
                        for k in range(5):
                            framesTrue, frame = video.read()
                            frameNo += 1
                main.insertRecord(value, listNP)
                print(listNP)
                recordInserted = 1
        if(recordInserted == 1):
            break
        frameNo += 1
        print(frameNo)
    
extractFramesFromVideo()
