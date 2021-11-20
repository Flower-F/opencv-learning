import cv2
import numpy as np

pic = cv2.imread('opencv\\123.png')

# 注意这里宽高相反
# new_pic = cv2.resize(pic, (300, 400))
# new_pic = cv2.resize(pic, None, fx=0.3, fy=0.3)
new_pic = cv2.resize(pic, None, fx=0.3, fy=0.3, interpolation=cv2.INTER_AREA)

# print(pic.shape)

cv2.imshow('pic', pic)
cv2.imshow('new_pic', new_pic)
cv2.waitKey(0)
