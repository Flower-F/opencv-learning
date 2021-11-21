import cv2
import numpy as np

# 创建 Haar 级联器
facer = cv2.CascadeClassifier(
    'opencv\\haarcascades\\haarcascade_frontalface_default.xml')

# 导入人脸识别图片 并进行灰度化
img = cv2.imread('opencv\\p3.png')
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# 进行人脸识别
faces = facer.detectMultiScale(gray_img, 1.1, 5)

for(x, y, w, h) in faces:
    cv2.rectangle(img, (x, y), (x+w, y+h), (0, 0, 255), 2)

# 识别器官
eye = cv2.CascadeClassifier(
    'opencv\\haarcascades\\haarcascade_eye.xml')
eyes = eye.detectMultiScale(gray_img, 1.1, 5)
for(x, y, w, h) in eyes:
    cv2.rectangle(img, (x, y), (x+w, y+h), (0, 0, 255), 2)

cv2.imshow('img', img)
cv2.waitKey(0)
