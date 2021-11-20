import cv2
import numpy as np

# 第一项 y 第二项 x
img = np.zeros((480, 640, 3), np.uint8)

# 画线
# # 第一项 x 第二项 y
# cv2.line(img, (10, 20), (300, 400), (0, 0, 255), 5)

# 画矩形
cv2.rectangle(img, (10, 10), (100, 100), (0, 0, 255))

# 画圆
cv2.circle(img, (320, 240), 100, (0, 0, 255))
cv2.circle(img, (320, 240), 5, (0, 0, 255), -1)

# 画椭圆
# 注意度数是顺时针计算的
cv2.ellipse(img, (320, 240), (100, 50), 0, 0, 360, (0, 0, 255))

pts = np.array([(300, 10), (150, 100), (450, 100)], np.int32)

# 画多边形
# 填充函数 fillPoly
cv2.polylines(img, [pts], True, (0, 0, 255), 1)

# 绘制文本
cv2.putText(img, "hello world", (10, 400),
            cv2.FONT_HERSHEY_COMPLEX, 1, (255, 0, 0))

cv2.imshow('draw', img)
cv2.waitKey(0)
