import cv2
import numpy as np

# 读取图像
image = cv2.imread('bridge.JPG')

# 应用均值滤波
# (5, 5)表示滤波器的大小，即一个5x5的邻域
blurred_image = cv2.blur(image, (5, 5))
sharpening_kernel = np.array([
    [0, -1, 0],
    [-1, 5,-1],
    [0, -1, 0]
])
sharpened_image = cv2.filter2D(blurred_image, -1, sharpening_kernel)
# 显示原图和处理后的图像
cv2.imshow('Original Image', image)
cv2.imshow('Blurred Image', blurred_image)
cv2.imshow('blurred and shapen Image',sharpened_image)

# 等待按键并关闭窗口
cv2.waitKey(0)
cv2.destroyAllWindows()


# import cv2
# import numpy as np
#
# # 读取图像
# image = cv2.imread('bridge.JPG')
#
# # 定义锐化卷积核
# sharpening_kernel = np.array([
#     [0, -1, 0],
#     [-1, 5,-1],
#     [0, -1, 0]
# ])
#
# # 应用锐化滤波
# sharpened_image = cv2.filter2D(image, -1, sharpening_kernel)
#
# # 显示原图和锐化后的图像
# cv2.imshow('Original Image', image)
# cv2.imshow('Sharpened Image', sharpened_image)
#
# # 等待按键并关闭窗口
# cv2.waitKey(0)
# cv2.destroyAllWindows()
