import cv2
import numpy as np

dog = cv2.imread('opencv\\dog.jpeg')

# 创建 logo
logo = np.zeros((200, 200, 3), np.uint8)
mask = np.zeros((200, 200), np.uint8)

# 绘制 logo
logo[20:120, 20:120] = [0, 0, 255]
logo[80:180, 80:180] = [0, 255, 0]

# 设置掩码
mask[20:120, 20:120] = 255
mask[80:180, 80:180] = 255

# 掩码求反
mask_not = cv2.bitwise_not(mask)

# 选择添加 logo 的位置
roi = dog[0:200, 0:200]
# 抠出原图此部分
tmp = cv2.bitwise_and(roi, roi, mask=mask_not)

dst = cv2.add(tmp, logo)

dog[0:200, 0:200] = dst

cv2.imshow('dog', dog)
cv2.waitKey(0)
