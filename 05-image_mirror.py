# coding=utf-8
# @Time     :2020/5/6 0006 17:42
# @Author   :Eric
# @Email    :zhangqi_@pku.edu.cn
# @File     :05-image_mirror.py
# @Software :PyCharm

from PIL import Image

# 1.加载原图
im1 = Image.open('files/b1.jpg')
im1.show()
# 2.左右镜像
image_lr = im1.transpose(Image.FLIP_LEFT_RIGHT)
image_lr.show()
image_lr.save('files/b1_lr.jpg')
# 3.上下镜像
image_tb = im1.transpose(Image.FLIP_TOP_BOTTOM)
image_tb.show()
image_tb.save('files/b1_tb.jpg')
# 4.左右镜像的上下镜像
image_lrtb = image_lr.transpose(Image.FLIP_TOP_BOTTOM)
image_lrtb.show()
image_lrtb.save('files/b1_lrtb.jpg')