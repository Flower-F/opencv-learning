import cv2
import numpy as np

img = np.zeros((480, 640, 3), np.uint8)

b, g, r = cv2.split(img)

# 分离图层
b[10:100, 10:100] = 255
g[10:100, 10:100] = 255

# 合并图层
img2 = cv2.merge((b, g, r))

cv2.imshow('img', img)
cv2.imshow('b', b)
cv2.imshow('g', g)
cv2.imshow('img2', img2)
cv2.waitKey(0)
