import cv2
import numpy as np

dog = cv2.imread('opencv\\dog.jpeg')
h, w, ch = dog.shape
# M = np.float32([[1, 0, 100], [0, 1, 0]])
# M = cv2.getRotationMatrix2D((w/2, h/2), 15, 0.5)
src = np.float32([[400, 300], [800, 300], [400, 1000]])
dst = np.float32([[200, 400], [600, 500], [150, 1100]])

M = cv2.getAffineTransform(src, dst)

new = cv2.warpAffine(dog, M, (w, h))
cv2.imshow('new', new)
cv2.waitKey(0)
