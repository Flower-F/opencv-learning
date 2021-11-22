import cv2
import pytesseract

# img = cv2.imread('opencv\\id_card0.jpg')
# img = cv2.imread('opencv\\id_card1.jpg')
# img = cv2.imread('opencv\\id_card2.png')
# img = cv2.imread('opencv\\id_card3.jpg')
# img = cv2.imread('opencv\\id_card4.jpg')
# img = cv2.imread('opencv\\id_card5.jpg')
img = cv2.imread('opencv\\id_card6.png')
# print(img.shape)

_, w, _ = img.shape
if w > 800:
    print('The picture is too large, you had better to find another one!')
    img = cv2.resize(img, None, fx=0.6, fy=0.6, interpolation=cv2.INTER_AREA)
    print(img.shape)

# 形态学 kernel
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))

# 失败 速度太慢
# mean_img = cv2.pyrMeanShiftFiltering(img, sp=20, sr=30)
# img_canny = cv2.Canny(mean_img, 150, 300)

# 灰度化
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# 二值化
_, binary_img = cv2.threshold(gray_img, 150, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
# binary_img = cv2.adaptiveThreshold(gray_img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 155, 1)

# 腐蚀 待调参
erode_img = cv2.erode(binary_img, kernel, iterations=6)

# 闭操作 待调参
close_img = cv2.morphologyEx(erode_img, cv2.MORPH_CLOSE, kernel,iterations=2)

# 轮廓查找
contours, _ = cv2.findContours(close_img, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

# 记录所有符合条件的矩形
rects = []

# 遍历轮廓
for (_, contour) in enumerate(contours):
    # 求出宽高
    x, y, w, h = cv2.boundingRect(contour)
    # 在符合条件的基础上 进行矩形框绘制
    if (w > h * 6) and (w < h * 18) and (w * h >= 3000):
        # 绘制红框
        rect = cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 2)
        # 把矩形添加到数组中
        rects.append({'x': x, 'y': y, 'w': w, 'h': h})

if rects.__len__() < 1:
    print('You input is not standard')
    exit()

# 继续查找坐标最低的矩形区域
final_rect = rects[0]
for (_, rect) in enumerate(rects):
    if rect['y'] + rect['h'] > final_rect['y'] + final_rect['h']:
        final_rect = rect.copy()

# 膨胀
# dilate_img = cv2.dilate(binary_img, kernel, iterations=1)

# 截取区域
dst = img[final_rect['y']:(final_rect['y']+final_rect['h']), final_rect['x']:(final_rect['x']+final_rect['w'])]

# 获取文本
# 待调参
# text = pytesseract.image_to_string(dst, lang="chi_sim+eng", config='--psm 7 --oem 3')
# text = pytesseract.image_to_string(dst, lang="eng", config='--psm 8')
text = pytesseract.image_to_string(dst, lang="eng", config='--psm 7 --oem 3')

print(text.replace(' ', ''))
print('识别结果未必精确，请再仔细确认号码是否无误')
cv2.imshow('img', img)
cv2.imshow('dst', dst)
cv2.waitKey(0)
cv2.destroyAllWindows()
