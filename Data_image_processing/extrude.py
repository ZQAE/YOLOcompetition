import cv2
import numpy as np

# 读取图像
image = cv2.imread('resized_image.jpg')

# 创建一个与图像大小相同的掩码，初始化为0 (表示背景)
mask = np.zeros(image.shape[:2], np.uint8)

# 创建前景和背景模型（这些模型由GrabCut算法使用）
bgd_model = np.zeros((1, 65), np.float64)  # 背景模型
fgd_model = np.zeros((1, 65), np.float64)  # 前景模型

# 初始化矩形框，手动定义前景区域
# 这里需要根据实际情况调整矩形框的位置和大小
rect = (50, 50, image.shape[1]-150, image.shape[0]-80)

# 使用GrabCut算法进行图像分割
cv2.grabCut(image, mask, rect, bgd_model, fgd_model, 10, cv2.GC_INIT_WITH_RECT)

# 将分割后的掩码转换为前景/背景掩码
mask2 = np.where((mask == 2) | (mask == 0), 0, 1).astype('uint8')

# 使用掩码提取前景
foreground = image * mask2[:, :, np.newaxis]

# 创建背景图像，将背景部分设置为白色
background = image * (1 - mask2[:, :, np.newaxis])
background[np.where(background == 0)] = 255  # 背景部分设置为白色
blurred_background = cv2.GaussianBlur(background, (21, 21), 0)
final_image = foreground +blurred_background
# 展示结果
cv2.imshow('Original Image', image)
cv2.imshow('Foreground', foreground)

cv2.imshow('Background', blurred_background)
cv2.imshow('final_image', final_image)


cv2.waitKey(0)
cv2.destroyAllWindows()
