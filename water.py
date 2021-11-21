# 分水岭法
import cv2
import numpy as np
from matplotlib import pyplot as plt

# 获取背景
# 二值化得到黑白图片
# 通过形态学获取背景
img = cv2.imread('opencv\\water_coins.jpeg')
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

_, thresh = cv2.threshold(
    gray_img, 100, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)

# 开运算
kernel = np.ones((3, 3), np.int8)
open_result = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel, iterations=2)

# 膨胀
bg = cv2.dilate(open_result, kernel, iterations=1)

# 获取前景
dist = cv2.distanceTransform(open_result, cv2.DIST_L2, 5)
_, fg = cv2.threshold(dist, 0.7*dist.max(), 255, cv2.THRESH_BINARY)

# 获取未知区域
fg = np.uint8(fg)
unknown = cv2.subtract(bg, fg)

# 创建连通域
_, marker = cv2.connectedComponents(fg)
marker = marker + 1
marker[unknown == 255] = 0

# 进行图形分割
result = cv2.watershed(img, marker)
# 将对应部分设置为红色
img[result == -1] = [0, 0, 255]

cv2.imshow('fg', fg)
cv2.imshow('bg', bg)
cv2.imshow('unknown', unknown)
cv2.imshow('result', img)
cv2.waitKey(0)
