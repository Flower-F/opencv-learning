import cv2
import numpy as np

img = cv2.imread('opencv\\RMB.jpeg')

# shape
# 高度 宽度 通道数
print(img.shape)

# 图形含用的空间
# 高度 * 宽度 * 通道数
print(img.size)

# 图像中每个元素的位深
print(img.dtype)