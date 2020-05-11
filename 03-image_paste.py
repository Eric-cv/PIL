# coding=utf-8
# @Time     :2020/5/6 0006 15:51
# @Author   :Eric
# @Email    :zhangqi_@pku.edu.cn
# @File     :03-image_paste.py
# @Software :PyCharm

from PIL import Image
import matplotlib.pyplot as plt

# im = plt.imread('files/b1.jpg')
im1 = Image.open('files/b1.jpg')
print(im1.size)
# plt.figure(figsize=(10, 8), dpi=80)
# plt.imshow(im)
# plt.show()

# 1.准备图片
# image1 = Image.open('files/a1.jpg')
# image2 = Image.open('files/b1.jpg')


# 2.图片粘贴
# 图片1.paste(图片2, 位置),把图片2粘贴到图片1上，直接改变原图
# image1.paste(image2, (0, 0))
# image1.show()
#
# 3.图片拼接
# 创建空白图：new(模式,大小,颜色)
# 模式：'RGB'/'RGBA'
# 颜色 - (红,绿，蓝) (255, 0, 0)-红色  (0, 255, 0)-绿色 (0, 0, 255)-蓝色
# (0, 0, 0)-黑色 (255, 255, 255)-白
empty = Image.new('RGB', (2500, 1100), (255, 255, 255))
empty.show()
image3 = Image.open('files/a1.jpg')
image4 = Image.open('files/b1.jpg')
empty.paste(image4, (0, 0))
empty.paste(image3, (1440, 0))
empty.show()

