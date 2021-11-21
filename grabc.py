import cv2
import numpy as np


class App:
    flag = False
    rect = (0, 0, 0, 0)
    startX = 0
    startY = 0

    def onmouse(self, event, x, y, flags, param):
        if(event == cv2.EVENT_LBUTTONDOWN):
            self.flag = True
            self.startX = x
            self.startY = y
        elif(event == cv2.EVENT_LBUTTONUP):
            self.flag = False
            cv2.rectangle(self.img,
                          (self.startX, self.startY),
                          (x, y),
                          (0, 0, 255),
                          3)
            self.rect = (min(self.startX, x),
                      min(self.startY, y),
                      abs(self.startX - x),
                      abs(self.startY - y))
        elif(event == cv2.EVENT_MOUSEMOVE):
            if(self.flag):
                self.img = self.img2.copy()
                cv2.rectangle(self.img,
                              (self.startX, self.startY),
                              (x, y),
                              (255, 0, 0),
                              3)

    def run(self):
        print('run')
        cv2.namedWindow('input')
        cv2.setMouseCallback('input', self.onmouse)

        self.img = cv2.imread('opencv\\lena.png')
        self.img2 = self.img.copy()
        self.mask = np.zeros(self.img.shape[:2], dtype=np.uint8)
        self.output = np.zeros(self.img.shape, np.uint8)

        while(True):
            cv2.imshow('input', self.img)
            cv2.imshow('output', self.output)
            key = cv2.waitKey(30)
            if(key == 27):
                break
            elif(key == ord('g')):
                bgd_model = np.zeros((1, 65), np.float64)
                fgd_model = np.zeros((1, 65), np.float64)
                cv2.grabCut(self.img2, self.mask, self.rect,
                            bgd_model, fgd_model, 1, cv2.GC_INIT_WITH_RECT)
            mask2 = np.where((self.mask == 1) | (
                self.mask == 3), 255, 0).astype('uint8')
            self.output = cv2.bitwise_and(self.img2, self.img2, mask=mask2)


App().run()
