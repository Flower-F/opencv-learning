import cv2
import numpy as np

img1 = cv2.imread('opencv\\opencv_search.png')
img2 = cv2.imread('opencv\\opencv_logo.png')
gray_img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
gray_img2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)

# 创建 SIFT 对象
sift = cv2.SIFT_create()

# 计算特征点和描述子
kp1, des1 = sift.detectAndCompute(gray_img1, None)
kp2, des2 = sift.detectAndCompute(gray_img2, None)

# 特征匹配
bf = cv2.BFMatcher(cv2.NORM_L1)
match = bf.match(des1, des2)

result = cv2.drawMatches(img1, kp1, img2, kp2, match, None)

cv2.imshow('result', result)
cv2.waitKey(0)
