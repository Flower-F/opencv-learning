import cv2
import numpy as np

back = cv2.imread('opencv\\back.jpeg')
smallcat = cv2.imread('opencv\\smallcat1.jpeg')

result = cv2.addWeighted(back, 0.3, smallcat, 0.7, 0)

cv2.imshow('add_weight', result)
cv2.waitKey(0)
