#!/usr/bin/env python
#coding:utf-8
# -*- coding: utf-8 -*-
from PIL import Image	

# def logo_watermark(img, logo_path):  
#     ''''' 
#     添加一个图片水印,原理就是合并图层，用png比较好 
#     '''  
#     baseim = img  
#     logoim = Image.open(logo_path)  
#     bw, bh = baseim.size  
#     lw, lh = logoim.size  
#     baseim.paste(logoim, (bw-lw, bh-lh))  
#     baseim.save('test3.jpg', 'JPEG')  
#     print u'logo水印组合成功'  

# img = Image.open('drag.jpeg')  #image 对象  
# # logo_watermark(im, 'code.jpg')
# img = img.convert("L")
# img.show()


import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import scipy.signal as signal


import cv2    
import numpy as np   
  






#------------------------------------------ 边缘 检测 ----------------------------------------------

# # 生成高斯算子的函数
# def func(x,y,sigma=1):
#     return 100*(1/(2*np.pi*sigma))*np.exp(-((x-2)**2+(y-2)**2)/(2.0*sigma**2))

# # 生成标准差为5的5*5高斯算子
# suanzi1 = np.fromfunction(func,(3,3),sigma=2)

# # Laplace扩展算子
# suanzi2 = np.array([[1, 1, 1],
#                     [1,-8, 1],
#                     [1, 1, 1]])

# # 打开图像并转化成灰度图像
# image = Image.open("drag.jpeg").convert("L")
# image_array = np.array(image)

# # 利用生成的高斯算子与原图像进行卷积对图像进行平滑处理
# image_blur = signal.convolve2d(image_array, suanzi1, mode="same")
# # image_blur = signal.convolve2d(image_blur, suanzi1, mode="same")

# # 对平滑后的图像进行边缘检测
# image2 = signal.convolve2d(image_blur, suanzi2, mode="same")

# # 结果转化到0-255
# image2 = (image2/float(image2.max()))*255

# # 将大于灰度平均值的灰度值变成255（白色），便于观察边缘
# image2[image2>image2.mean()] = 255

# # 显示图像
# plt.subplot(2,1,1)
# plt.imshow(image_array,cmap=cm.gray)
# plt.axis("off")
# plt.subplot(2,1,2)
# plt.imshow(image2,cmap=cm.gray)
# plt.axis("off")
# plt.show()





# image = cv2.imread("drag.jpeg")
# gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# gradX = cv2.Sobel(gray, ddepth=cv2.cv.CV_32F, dx=1, dy=0, ksize=-1)
# gradY = cv2.Sobel(gray, ddepth=cv2.cv.CV_32F, dx=0, dy=1, ksize=-1)
# # subtract the y-gradient from the x-gradient
# gradient = cv2.subtract(gradX, gradY)
# gradient = cv2.convertScaleAbs(gradient)



# # blur and threshold the image
# blurred = cv2.blur(gradient, (9, 9))
# (_, thresh) = cv2.threshold(blurred, 90, 255, cv2.THRESH_BINARY)



# kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (25, 25))
# closed = cv2.morphologyEx(thresh, cv2.MORPH_CLOSE, kernel)

# # perform a series of erosions and dilations
# closed = cv2.erode(closed, None, iterations=4)
# closed = cv2.dilate(closed, None, iterations=4)


# (cnts, _) = cv2.findContours(closed.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
# c = sorted(cnts, key=cv2.contourArea, reverse=True)[0]

# # compute the rotated bounding box of the largest contour
# rect = cv2.minAreaRect(c)
# box = np.int0(cv2.cv.BoxPoints(rect))

# # draw a bounding box arounded the detected barcode and display the image
# cv2.drawContours(image, [box], -1, (0, 255, 0), 3)
# cv2.imshow("Image", image)
# cv2.imwrite("contoursImage2.jpg", image)
# cv2.waitKey(0)




#coding=utf-8 
import cv2 
import numpy as np
 
img = cv2.imread("contour.png")    #载入图像
h, w = img.shape[:2]      #获取图像的高和宽 
cv2.imshow("Origin", img)     #显示原始图像
 
blured = cv2.blur(img,(5,5))    #进行滤波去掉噪声
cv2.imshow("Blur", blured)     #显示低通滤波后的图像
 
mask = np.zeros((h+2, w+2), np.uint8)  #掩码长和宽都比输入图像多两个像素点，满水填充不会超出掩码的非零边缘 
#进行泛洪填充
cv2.floodFill(blured, mask, (w-1,h-1), (255,255,255), (2,2,2),(3,3,3),8)
cv2.imshow("floodfill", blured) 
 
#得到灰度图
gray = cv2.cvtColor(blured,cv2.COLOR_BGR2GRAY) 
cv2.imshow("gray", gray) 
 
 
#定义结构元素 
kernel = cv2.getStructuringElement(cv2.MORPH_RECT,(50, 50))
#开闭运算，先开运算去除背景噪声，再继续闭运算填充目标内的孔洞
opened = cv2.morphologyEx(gray, cv2.MORPH_OPEN, kernel) 
closed = cv2.morphologyEx(opened, cv2.MORPH_CLOSE, kernel) 
cv2.imshow("closed", closed) 
 
#求二值图
ret, binary = cv2.threshold(closed,250,255,cv2.THRESH_BINARY) 
cv2.imshow("binary", binary) 
 
#找到轮廓
_,contours, hierarchy = cv2.findContours(binary,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE) 
#绘制轮廓
 
cv2.drawContours(img,contours,-1,(0,0,255),3) 
#绘制结果
cv2.imshow("result", img)
 
cv2.waitKey(0) 
cv2.destroyAllWindows()



#-------------------------------------------------------轮廓 识别 --------------------------------------

    


# sourceimg = cv2.imread('contour.png')
# hongqiimgray = cv2.cvtColor(sourceimg,cv2.COLOR_BGR2GRAY)
# ret,hongqithresh = cv2.threshold(hongqiimgray,127,255,0)

# im2, contours, hierarchy = cv2.findContours(hongqithresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

# print(contours)
# cv2.drawContours(sourceimg, contours, -1, (0,255,0), 3)

# cv2.imshow("img", sourceimg)    
# cv2.waitKey(0) 