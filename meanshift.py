import cv2
import numpy as np

img = cv2.imread('opencv\\flower.png')
mean_img = cv2.pyrMeanShiftFiltering(img, sp=20, sr=30)

img_canny = cv2.Canny(mean_img, 150, 300)
contours, _ = cv2.findContours(
    img_canny, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

cv2.drawContours(img, contours, -1, (0, 0, 255), 2)

cv2.imshow('img', img)
cv2.imshow('mean_img', mean_img)
cv2.waitKey(0)
