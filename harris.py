import cv2
import numpy as np

# harris
# blockSize = 2
# ksize = 3
# k = 0.04

# shi-Tomasi
maxCorners = 1000
ql = 0.01
minDistance = 10

img = cv2.imread('opencv\\chess.png')
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Harris
# dst = cv2.cornerHarris(gray_img, blockSize, ksize, k)
# img[dst > 0.01 * dst.max()] = [0, 0, 255]

# shi-Tomasi
corners = cv2.goodFeaturesToTrack(gray_img, maxCorners,
                                  qualityLevel=ql, minDistance=minDistance)
corners = np.int0(corners)
for i in corners:
    x, y = i.ravel()
    cv2.circle(img, (x, y), 3, (255, 0, 0), -1)


cv2.imshow('harris', img)
cv2.waitKey(0)
