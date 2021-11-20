import cv2
import numpy as np

# 非
# img = np.zeros((200, 200), np.uint8)
# img[50:150, 50:150] = 255
# img_not = cv2.bitwise_not(img)
# cv2.imshow('img', img)
# cv2.imshow('img_not', img_not)

# 与 即显示交叉部分
# img = np.zeros((200, 200), np.uint8)
# img2 = np.zeros((200, 200), np.uint8)
# img[20:120, 20:120] = 255
# img2[80:180, 80:180] = 255
# img_and = cv2.bitwise_and(img, img2)
# cv2.imshow('img', img)
# cv2.imshow('img2', img2)
# cv2.imshow('img_and', img_and)

# 或
# 与 即显示交叉部分
# img = np.zeros((200, 200), np.uint8)
# img2 = np.zeros((200, 200), np.uint8)
# img[20:120, 20:120] = 255
# img2[80:180, 80:180] = 255
# img_or = cv2.bitwise_or(img, img2)
# cv2.imshow('img', img)
# cv2.imshow('img2', img2)
# cv2.imshow('img_and', img_or)

# 异或
img = np.zeros((200, 200), np.uint8)
img2 = np.zeros((200, 200), np.uint8)
img[20:120, 20:120] = 255
img2[80:180, 80:180] = 255
img_xor = cv2.bitwise_xor(img, img2)
cv2.imshow('img', img)
cv2.imshow('img2', img2)
cv2.imshow('img_and', img_xor)

cv2.waitKey(0)
