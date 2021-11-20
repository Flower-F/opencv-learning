# 基本的窗口创建

import cv2

cv2.namedWindow('img', cv2.WINDOW_NORMAL)

img = cv2.imread(
    'opencv\\123.png')

while True:
    cv2.imshow('img', img)
    key = cv2.waitKey(0)
    if(key & 0xFF == ord('q')):
        break
    elif(key & 0xFF == ord('s')):
        cv2.imwrite("opencv\\imwrite\\hello.png", img)

cv2.destroyAllWindows()