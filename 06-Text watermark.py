# coding=utf-8
# @Time     :2020/5/6 0006 17:51
# @Author   :Eric
# @Email    :zhangqi_@pku.edu.cn
# @File     :06-Text watermark.py
# @Software :PyCharm

from PIL import Image, ImageFont, ImageDraw

# 1.打开图片
image1 = Image.open('files/b1.jpg')
# image1.show()

# 2.创建字体对象
# truetype(字体文件，字号')
font = ImageFont.truetype('字体文件的path', 20)
# 3.创建draw对象
draw = ImageDraw.Draw(image1)
# 4.文字渲染
# text(坐标，文字内容，字体对象，文字颜色)
draw.text((0, 0), '你好', font=font, fill=(0, 0, 0))
image1.show()
