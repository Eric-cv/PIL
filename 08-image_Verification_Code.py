# coding=utf-8
# @Time     :2020/5/6 0006 18:30
# @Author   :Eric
# @Email    :zhangqi_@pku.edu.cn
# @File     :08-image_Verification_Code.py
# @Software :PyCharm

from PIL import Image, ImageFont, ImageDraw, ImageFilter
from random import randint


# 1.创建空图片
image1 = Image.new('RGB', (120, 60), (255, 255, 255))
# image1.show()
# 2.渲染背景

draw = ImageDraw.Draw(image1)
for x in range(0, 120):
    for y in range(0, 60):
        r = randint(0, 255)
        g = randint(0, 255)
        b = randint(0, 255)
        draw.point((x, y), (r, g, b))

image1 = image1.filter(ImageFilter.BLUR)
# image1.show()

# 3.渲染文字
draw = ImageDraw.Draw(image1)
font = ImageFont.truetype('file/consolaz.ttf', 30)

# nums = (randint(0, 9), randint(0, 9), randint(0, 9), randint(0, 9))
for x in range(4):
    num = str(randint(0, 9))
    y = randint(10, 40)
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)

    draw.text((30*x, y), num, (r, g, b), font)

image1.show()
