# 通过鼠标进行基本绘制
# 包括画线：用户按下 L 键 shape = 0
# 画矩形：用户按下 R 键 shape = 1
# 画圆：用户按下 C 键 shape = 2
import cv2
import numpy as np

current_shape = 0
startpos = (0, 0)
img = np.zeros((480, 640, 3), np.uint8)

cv2.namedWindow('drawshape', cv2.WINDOW_NORMAL)


def mouse_callback(event, x, y, flags, userdata):
    global startpos, current_shape
    if(event & cv2.EVENT_LBUTTONDOWN == cv2.EVENT_LBUTTONDOWN):
        startpos = (x, y)
    elif(event & cv2.EVENT_LBUTTONUP == cv2.EVENT_LBUTTONUP):
        if(current_shape == 0):
            cv2.line(img, startpos, (x, y), (0, 0, 255))
        elif(current_shape == 1):
            cv2.rectangle(img, startpos, (x, y), (0, 0, 255))
        elif(current_shape == 2):
            a = (x - startpos[0])
            b = (y - startpos[1])
            r = int((a**2+b**2)**0.5)
            cv2.circle(img, startpos, r, (0, 0, 255))
        else:
            print('error!')


cv2.setMouseCallback('drawshape', mouse_callback, "123")


while True:
    cv2.imshow('drawshape', img)
    key = cv2.waitKey(1)
    if(key & 0xFF == ord('q')):
        break
    elif(key & 0xFF == ord('l')):
        current_shape = 0
    elif(key & 0xFF == ord('c')):
        current_shape = 2
    elif(key & 0xFF == ord('r')):
        current_shape = 1
    elif(key & 0xFF == ord('c')):
        current_shape = 2

cv2.destroyAllWindows()
