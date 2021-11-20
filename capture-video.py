# 通过摄像头读取

import cv2

fourcc = cv2.VideoWriter_fourcc(*'MJPG')
vw = cv2.VideoWriter('./out.mp4', fourcc, 25, (1280, 720))

# 创建窗口
cv2.namedWindow('video', cv2.WINDOW_NORMAL)
cv2.resizeWindow('video', 640, 480)

# 获取视频设备
# capture = cv2.VideoCapture("opencv\\video.mp4")
capture = cv2.VideoCapture(0)

while capture.isOpened():
    result, frame = capture.read()
    if(result == True):
        cv2.imshow('video', frame)
        cv2.resizeWindow('video', 640, 480)
        vw.write(frame)
        key = cv2.waitKey(40)
        if(key & 0xFF == ord('q')):
            break
    else:
        break

# 释放资源
capture.release()
vw.release()
cv2.destroyAllWindows()
