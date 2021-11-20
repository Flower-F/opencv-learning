import cv2
import numpy as np


cv2.namedWindow('trackbar', cv2.WINDOW_NORMAL)


def callback():
    pass


# 创建 trackbar
cv2.createTrackbar('R', 'trackbar', 0, 255, callback)
cv2.createTrackbar('G', 'trackbar', 0, 255, callback)
cv2.createTrackbar('B', 'trackbar', 0, 255, callback)

# 设置纯黑图片
img = np.zeros((480, 640, 3), np.uint8)

while True:
    cv2.imshow('trackbar', img)

    r = cv2.getTrackbarPos('R', 'trackbar')
    g = cv2.getTrackbarPos('G', 'trackbar')
    b = cv2.getTrackbarPos('B', 'trackbar')

    img[:] = [b, g, r]

    key = cv2.waitKey(10)
    if(key & 0xFF == ord('q')):
        break

cv2.destroyAllWindows()
