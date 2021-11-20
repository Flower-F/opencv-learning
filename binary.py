import cv2
import numpy as np

img = cv2.imread('opencv\\math.png')
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
result, dst = cv2.threshold(gray_img, 180, 255, cv2.THRESH_BINARY)

new_pic = cv2.resize(dst, None, fx=0.2, fy=0.2, interpolation=cv2.INTER_AREA)

# cv2.imshow('img', img)
# cv2.imshow('gray', gray_img)
cv2.imshow('dst', new_pic)
cv2.waitKey(0)
