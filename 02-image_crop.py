# coding=utf-8
# @Time     :2020/5/6 0006 15:33
# @Author   :Eric
# @Email    :zhangqi_@pku.edu.cn
# @File     :02-image_crop.py
# @Software :PyCharm

from PIL import Image

# 1.加载图片
image1 = Image.open(r'.\files\a1.jpg')
image1.show()
# 2.图片剪切
# crop(范围)
# 范围 - (点1x,点1y,点2x,点2y)
image2 = image1.crop((300, 300, 700, 700))
image2.show()
