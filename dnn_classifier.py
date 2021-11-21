import cv2
import numpy as np
from cv2 import dnn

# 导入模型 创建神经网络
config = 'opencv\\model\\bvlc_googlenet.prototxt'
model = 'opencv\\model\\bvlc_googlenet.caffemodel'
net = dnn.readNetFromCaffe(config, model)

# 读取图片 转成张量
img = cv2.imread('opencv\\smallcat.jpeg')
# img = cv2.imread('opencv\\card.jpg')

blob = dnn.blobFromImage(img, 1.0, (224, 224), (104, 117, 123))

# 将张量输入到网络 并进行预测
net.setInput(blob)
r = net.forward()

# 读入类目
classes = []
path = 'opencv\\model\\synset_words.txt'
with open(path, 'rt') as f:
    classes = [x[x.find(' ') + 1:]for x in f]

order = sorted(r[0],reverse=True)
z = list(range(3))

for i in range(0,3):
    z[i] = np.where(r[0] == order[i])[0][0]
    print('第',i+1,'项',classes[z[i]],end='')
    print('类所在行',z[i] + 1, '可能性',order)