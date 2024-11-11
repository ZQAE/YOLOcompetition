from PIL import Image

# 打开 JPG 图片
image_path = '123.jpg'
image = Image.open(image_path)

# 设置缩放的大小
new_width = 510
new_height = 510

# 使用 PIL 的 thumbnail 方法或 resize 方法进行缩放
# 使用 thumbnail 保持图片的宽高比
image.thumbnail((new_width, new_height))

# 如果不需要保持比例，可以直接使用 resize
# image_resized = image.resize((new_width, new_height))

# 保存缩放后的图片
image.save('resized_image.jpg')

# 显示缩放后的图片
image.show()
