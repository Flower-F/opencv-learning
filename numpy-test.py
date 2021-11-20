import numpy as np
import cv2


# 通过 array 定义矩阵
# a = np.array([1, 2, 3])
# b = np.array([[1, 2, 3], [4, 5, 6]])
# print(b)


# 定义 zeros 矩阵
# 3 指的是 rgb 的三个通道
# c = np.zeros((8, 8, 3), np.uint8)
# print(c)

# 定义 ones 矩阵
# 3 指的是 rgb 的三个通道
# d = np.ones((8, 8, 3), np.uint8)
# print(d)

# 定义 full 矩阵
# e = np.full((8, 8), 255, np.uint8)
# print(e)

# 定义单位矩阵
# f = np.identity(8)
# print(f)

# 增广矩阵
# g = np.eye(5, 7, 3)
# print(g)

img = np.zeros((480, 640, 3), np.uint8)

count = 0
while(count < 200):
    # 第一层 B 所有颜色为蓝色
    img[count, 100, 0] = 255
    count = count + 1

cv2.imshow('img', img)
key = cv2.waitKey(0)
if(key & 0xFF == ord('q')):
    cv2.destroyAllWindows()
