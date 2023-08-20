import base64
import glob
import os
import pickle

import cv2
import numpy as np
import requests
from sklearn.metrics import accuracy_score, confusion_matrix
from sklearn.tree import DecisionTreeClassifier

# อ่านไฟล์
test_part = 'D:\AI66\\teaincarmodel\\test' 
part = 'D:\AI66\\teaincarmodel\\train'
# print(part)

test_list = os.listdir(test_part)  # รายการของไฟล์ทั้งหมดในโฟลเดอร์
train_list = os.listdir(part)
# print(test_list)


def setBrandNumber(brand):
    index = test_list.index(brand)  
    return index
# print(setBrandNumber('Audi'))

url = "http://localhost:5000/api/gethog"
def imgCarbase64(img):
    v, buffer = cv2.imencode(".jpg", img)
    img_str = base64.b64encode(buffer)
    data = "image data,"+str.split(str(img_str),"'")[1]
    response = requests.get(url, json={"img":data})
    return response.json()  

# img = cv2.imread('D:\AI66\\teaincarmodel\\train\Audi\\1.jpg')
# print(imgCarbase64(img))

#อ่านข้อมูลภาพมาไว้ใน list (X)
def readData(part):
    response = []
    
    for folder in os.listdir(part):
        for img_name in os.listdir(part+'\\'+folder):
            if(img_name==""):
                break
            img_path = part+'\\'+folder+'\\'+img_name
            print(img_name+"   --")
            break
            # img = cv2.imread(img_path) # การแปลงรูปภาพเป็นตัวเลข
            # res = imgCarbase64(img) #การเรียนใช้ Methot api เพื่อทำการแปลง img เป็น hog vector
            # hog = list(res["hog"])
            # hog.append(train_list.index(folder)) #การนำตัวเลขมาต่อกัน
            # response.append(hog)  # ค่าทีได้จะถูกเก็บไว้ใน list
    return   response        
# testData =  readData(part)
# print (testData)



 
    