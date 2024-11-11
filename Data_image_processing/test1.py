import cv2
import numpy as np
import matplotlib.pyplot as plt
def show_image(image, title, pos):
    #  顺序转换：BGR TO RGB
    image_RGB = image[:, :, ::-1] # shape : (height, width, channel)
    # 显示标题
    plt.subplot(2, 2, pos) # 定位
    plt.title(title)
    plt.imshow(image_RGB)

def show_histogram(hist, title, pos, color):
    # 显示标题
    plt.subplot(2, 2, pos) # 定位图片
    plt.title(title)
    plt.xlabel("Bins") # 横轴信息
    plt.ylabel("Pixels") # 纵轴信息
    plt.xlim([0, 256]) # 范围
    plt.plot(hist, color=color) # 绘制直方图

def main():
    #创建画布
    plt.figure(figsize=(20, 10)) # 画布大小
    plt.suptitle("Gray Image Histogram", fontsize=14, fontweight="bold") # 设置标题形式

    img = cv2.imread("bridge.JPG")

    #灰度转换
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    hist_img_gray = cv2.calcHist([img_gray], [0], None, [256], [0, 256])

    #计算灰度图的直方图
    img_equ = cv2.equalizeHist(img_gray)
    hist_img_equ = cv2.calcHist([img_equ], [0], None, [256], [0, 256])

    #展示灰度直方图
    #将灰度图像转换为 BGR 彩色图像。虽然转换后的图像是三通道，但每个通道的值都相同，即图像实际上是灰度色调的彩色表示。
    #灰度图像转换为 BGR 彩色图像时，主要是为了某些图像处理算法需要输入彩色图像，
    # 但你不希望影响图像内容或颜色。在某些显示和保存图像时也可能会用到这种转换。
    img_BGR_GRAY = cv2.cvtColor(img_gray, cv2.COLOR_GRAY2BGR)
    img_BGR_EQU = cv2.cvtColor(img_equ, cv2.COLOR_GRAY2BGR)

    show_image(img_BGR_GRAY, "gray image", 1)
    show_image(img_BGR_EQU, "equalized image", 3)

    show_histogram(hist_img_gray, "gray image histogram", 2, "m")
    show_histogram(hist_img_equ, "equalized image histogram", 4, "m")

    plt.show()

if __name__ == '__main__':
    main()

