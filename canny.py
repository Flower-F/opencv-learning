# 边缘检测
import cv2
import numpy as np

img = cv2.imread('opencv\\lena.png')

dst = cv2.Canny(img, 100, 200)

cv2.imshow('img', img)
cv2.imshow('dstt', dst)
cv2.waitKey(0)
