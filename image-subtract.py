# 降低曝光度的例子
import cv2
import numpy as np

# 图的加法运算就是矩阵的加法运算
# 因此加法运算的两张图必须相等
dog = cv2.imread('opencv\\dog.jpeg')

# print(dog.shape)
# (1200, 1920, 3)

img = np.ones((1200, 1920, 3), np.uint8) * 50

result = cv2.add(dog, img)
origin = cv2.subtract(result, img)
subtract_result = cv2.subtract(dog, img)

cv2.imshow("origin", origin)
cv2.imshow("subtract_result", subtract_result)
cv2.waitKey(0)
