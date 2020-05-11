# coding=utf-8
# @Time     :2020/5/6 0006 14:36
# @Author   :Eric
# @Email    :zhangqi_@pku.edu.cn
# @File     :01-image_filter.py
# @Software :PyCharm
# import PIL
from PIL import Image, ImageFilter
import os

# print(os.getcwd())
# 1.加载图片
image = Image.open(r'.\files\a1.jpg')
# # 2.显示图片,自动调用电脑上的图片打开软件
# image.show()
# # 3.保存图片
# image.save(r'.\files\a2.jpg')

# ========滤镜效果=========
# 1.添加系统滤镜
# 图片对象.filter(滤镜效果)  - 返回一个新的图片对象
# image2 = image.filter(ImageFilter.EMBOSS)  # 浮雕效果
# image2.show()
# image2.save(r'.\files\a3.jpg')
#
# image3 = image.filter(ImageFilter.CONTOUR)  # 铅笔画效果
# image3.show()

# image4 = image.filter(ImageFilter.BLUR)  # 模糊效果
# image4.show()

image5 = image.filter(ImageFilter.EDGE_ENHANCE)  # 模糊效果
image5.show()

