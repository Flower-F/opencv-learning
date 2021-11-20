import cv2
import numpy as np

img = cv2.imread('opencv\\dog.jpeg')

kernal = np.ones((5, 5), np.float32)/25

# dst = cv2.filter2D(img, -1, kernel=kernal)
# dst = cv2.blur(img, (5, 5))
dst = cv2.GaussianBlur(img, (5, 5), sigmaX=1)

cv2.imshow('origin', img)
cv2.imshow('dst', dst)
cv2.waitKey(0)
