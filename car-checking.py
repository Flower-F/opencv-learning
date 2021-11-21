#coding=utf-8

import cv2
import numpy as np

# 引入 tesseract 库
import pytesseract

# 创建 Haar 级联器
plate = cv2.CascadeClassifier(
    'opencv\\haarcascades\\haarcascade_russian_plate_number.xml')

# 导入车牌识别图片 并进行灰度化
img = cv2.imread('opencv\\chinacar.jpeg')
# img = cv2.imread('opencv\\id_card0.jpg')

gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# 检测车牌位置
plates = plate.detectMultiScale(gray_img, 1.1, 5)
for(x, y, w, h) in plates:
    cv2.rectangle(img, (x, y), (x+w, y+h), (0, 0, 255), 2)

# 对获取的车牌进行预处理
roi = gray_img[y:y+h, x:x+w]
# 二值化
_, binary_roi = cv2.threshold(roi, 0, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)

text = pytesseract.image_to_string(binary_roi, lang="chi_sim+eng", config='--psm 7 --oem 3')
#  -psm 7 nobatch
print(text)
# print(text.encode('GBK','ignore').decode('GBK'))
# print('你好').decode('UTF-8').encode('GBK')

cv2.imshow('img', img)
cv2.imshow('binary_roi', binary_roi)
cv2.waitKey(0)
