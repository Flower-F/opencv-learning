import cv2

cv2.namedWindow('color', cv2.WINDOW_NORMAL)

img = cv2.imread('opencv\\RMB.jpeg')
colorspaces = [cv2.COLOR_BGR2RGBA, cv2.COLOR_BGR2BGRA,
               cv2.COLOR_BGR2GRAY, cv2.COLOR_BGR2HSV_FULL,
               cv2.COLOR_BGR2YUV]


def callback():
    pass


cv2.createTrackbar('current_color', 'color', 0, len(colorspaces), callback)


while True:
    index = cv2.getTrackbarPos('current_color', 'color')
    # 颜色空间转换
    cvt_img = cv2.cvtColor(img, colorspaces[index])
    cv2.imshow('color', cvt_img)
    key = cv2.waitKey(10)
    if(key & 0xFF == ord('q')):
        break

cv2.destroyAllWindows()

