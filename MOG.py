import cv2
import numpy as np

capture = cv2.VideoCapture('opencv\\vtest.avi')
# MOG2 相比于 MOG 的优点：可以计算出阴影部分
# 缺点：会产生很多噪点
# mog = cv2.createBackgroundSubtractorMOG2()
mog = cv2.createBackgroundSubtractorKNN()

while(True):
    result, frame = capture.read()
    fgmask = mog.apply(frame)
    cv2.imshow('img', fgmask)

    key = cv2.waitKey(10)

    if(key == 27):
        break

capture.release()
cv2.destroyAllWindows()