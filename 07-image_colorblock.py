# coding=utf-8
# @Time     :2020/5/6 0006 18:03
# @Author   :Eric
# @Email    :zhangqi_@pku.edu.cn
# @File     :07-image_colorblock.py
# @Software :PyCharm

from PIL import Image, ImageDraw
import random

# 1. 加载图片
image1 = Image.new('RGB', (600, 600), (255, 255, 255))
# image1.show()

# 2. 创建draw对象
draw = ImageDraw.Draw(image1)
# 3.渲染颜色
# point(坐标, 颜色)
i = 0
# 画线
for i in range(200):
    draw.point((100, 100 + i), (255, 0, 0))
    draw.point((101, 100 + i), (0, 255, 0))
    draw.point((102, 100 + i), (0, 0, 255))


# 画颜色块
# for x in range(100, 201):
#     for y in range(100, 201):
#         draw.point((x, y ), (255, 0, 0))

# 颜色随机
def rand_color():
    color = random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)
    return color


# a = rand_color()
# print(type(a))


for x in range(100, 201):
    for y in range(100, 201):
        if y % 5 == 0:
            color = rand_color()
        draw.point((x, y), color)
image1.show()
