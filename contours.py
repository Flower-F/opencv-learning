import cv2
import numpy as np


def drawShape(src, points):
    i = 0
    while i < len(points):
        if(i == len(points) - 1):
            x, y = points[i][0]
            x1, y1 = points[0][0]
            cv2.line(src, (x, y), (x1, y1), (0, 0, 255), 1)
        else:
            x, y = points[i][0]
            x1, y1 = points[i+1][0]
            cv2.line(src, (x, y), (x1, y1), (0, 0, 255), 1)
        i = i + 1


# img = cv2.imread('opencv\\contours1.jpeg')
# img = cv2.imread('opencv\\hand.png')
img = cv2.imread('opencv\\hello.jpeg')
# print(img.shape)
# 单通道
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# 二值化
result, binary_img = cv2.threshold(gray_img, 150, 255, cv2.THRESH_BINARY)

# 轮廓查找
contours, hierarchy = cv2.findContours(
    binary_img, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

# 绘制轮廓
# cv2.drawContours(img, contours, 0, (0, 0, 255), 1)

# 计算轮廓面积
# area = cv2.contourArea(contours[0])

# 计算轮廓周长
# True False表示是否闭合
# len = cv2.arcLength(contours[0], False)

# print(contours)
# print(area)
# print(len)

# # 多边形逼近
# apprpx = cv2.approxPolyDP(contours[0], 5, True)
# drawShape(img, apprpx)

# 凸包
# hull = cv2.convexHull(contours[0])
# drawShape(img, hull)

# 最小外接矩形
min_rect = cv2.minAreaRect(contours[1])
# 因为 r 中包含有坐标和角度 但是绘制只需要角度 这里要过滤掉角度
box = cv2.boxPoints(min_rect)
# 类型转换
box = np.int0(box)
cv2.drawContours(img, [box], 0, (0, 0, 255), 2)

# 最大外接矩形
x, y, w, h = cv2.boundingRect(contours[1])

cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)

cv2.imshow('img', img)
# cv2.imshow('binary_img', binary_img)
cv2.waitKey(0)
