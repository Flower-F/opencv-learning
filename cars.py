import cv2
import numpy as np

# 车辆最小宽高
min_width = 90
min_height = 90

# 检测线高度
line_height = 550

# 存放有效车辆的数组
cars = []

# 线的偏移
offset = 7

# 统计车的数量
car_total = 0

# 求解轮廓中心点函数


def center(x, y, w, h):
    x1 = int(w/2)
    y1 = int(h/2)
    cx = x + x1
    cy = y + y1

    return cx, cy


capture = cv2.VideoCapture('opencv\\video.mp4')

sub_mog = cv2.createBackgroundSubtractorMOG2()

# 形态学 kernel
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5))

while True:
    result, frame = capture.read()
    if(result == True):
        # 灰度化
        gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        # 高斯去噪
        blur = cv2.GaussianBlur(gray_frame, (3, 3), 5)
        # 去除背景
        mask = sub_mog.apply(blur)
        # 腐蚀：去除噪声
        erode_frame = cv2.erode(mask, kernel)
        # 膨胀：还原物体
        dilate_frame = cv2.dilate(erode_frame, kernel, iterations=3)
        # 闭操作：去除内部残缺
        close_frame = cv2.morphologyEx(dilate_frame, cv2.MORPH_CLOSE, kernel)
        # 查找轮廓
        contours, h = cv2.findContours(
            close_frame, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        # 画检测边界线
        cv2.line(frame, (10, line_height),
                 (1200, line_height), (255, 255, 0), 3)

        # 遍历轮廓
        for (_, contour) in enumerate(contours):
            x, y, w, h = cv2.boundingRect(contour)
            # 判断是否为有效车辆
            isValid = (w >= min_width) and (h >= min_height)
            if(not isValid):
                continue
            # 绘制矩形框
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2)
            # 存取车辆中心点
            center_point = center(x, y, w, h)
            cars.append(center_point)

            # 检测车辆是否落入线内范围
            for(x, y) in cars:
                if((y > line_height - offset) and (y < line_height + offset)):
                    car_total += 1
                    cars.remove((x, y))
                    print(car_total)

        cv2.putText(frame, "Cars: "+str(car_total),
                    (500, 60), cv2.FONT_HERSHEY_COMPLEX, 2, (255, 0, 0))
        cv2.imshow('video', frame)
    key = cv2.waitKey(30)
    # 若按下 ESC 键
    if(key == 27):
        break
    # 释放资源
capture.release()
cv2.destroyAllWindows()
