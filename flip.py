import cv2
import numpy as np

dog = cv2.imread('opencv\\dog.jpeg')
new = cv2.flip(dog, 0)

cv2.imshow('new', new)
cv2.waitKey(0)