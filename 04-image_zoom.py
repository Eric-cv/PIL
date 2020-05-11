# coding=utf-8
# @Time     :2020/5/6 0006 17:36
# @Author   :Eric
# @Email    :zhangqi_@pku.edu.cn
# @File     :04-image_zoom.py
# @Software :PyCharm
from PIL import Image
import matplotlib.pyplot as plt

# 1.加载原图
im1 = Image.open('files/b1.jpg')
# print(im1.size)

# 2.缩放
# 图片对象.thumbnail(大小)
im1.thumbnail((100, 100))
im1.show()
# im1.save(r'files/b2.jpg')
