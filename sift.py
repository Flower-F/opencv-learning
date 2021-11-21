import cv2
import numpy as np

img = cv2.imread('opencv\\chess.png')
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# 创建 SIFT 对象
# sift = cv2.SIFT_create()
# 进行检测 得到 key points
# kp = sift.detect(gray_img, None)

# 创建 ORB 对象
orb = cv2.ORB_create()

# 同时进行检测和计算描述子
# kp, des = sift.detectAndCompute(gray_img, None)
kp, des = orb.detectAndCompute(gray_img, None)

# 绘制 key points
cv2.drawKeypoints(gray_img, kp, img)

cv2.imshow('img', img)
cv2.waitKey(0)
