import random
from PIL import Image, ImageDraw, ImageFont,ImageFilter


#
def check_code(width=120, height=30, char_length=4, font_file="Arial.ttf", font_size=30):
    code=[]
    # 创建一个新的图片对象
    img = Image.new(mode='RGB', size=(width, height), color=(255, 255, 255))
    # 创建一个画笔对象
    draw = ImageDraw.Draw(img)

    def rndChar():
        return chr(random.randint(65, 90))

    #
    def rndColor():
        return (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

    # 设置字体
    font = ImageFont.truetype(font_file, font_size)
    for i in range(char_length):
        ch = rndChar()
        code.append(ch)
        h = random.randint(0, 4)
        draw.text([i * width / char_length, h], ch, font=font, fill=rndColor())

    # # 获取字符的宽度和高度
    # # text_width, text_height = draw.textsize(code, font)
    # # 获取字符的宽度和高度
    # bbox = draw.textbbox((0, 0, width, height), code, font=font)
    # text_width = bbox[2] - bbox[0]
    # text_height = bbox[3] - bbox[1]
    #
    # # 将字符绘制在图片中央
    # x = (width - text_width) // 2
    # y = (height - text_height) // 2
    # draw.text((x, y), code, font=font, fill=(0, 0, 0))
    # 添加干扰线
    for i in range(5):
        x1 = random.randint(0, width)
        y1 = random.randint(0, height)
        x2 = random.randint(0, width)
        y2 = random.randint(0, height)
        draw.line((x1, y1, x2, y2), fill=(0, 0, 0), width=2)
    # 添加干扰点
    for i in range(20):
        x = random.randint(0, width)
        y = random.randint(0, height)
        draw.point((x, y), fill=(0, 0, 0))

    img = img.filter(ImageFilter.EDGE_ENHANCE_MORE)
    # 返回验证码图片对象
    return img, ''.join(code)


# imge,code_string = check_code()
# with open('code.png', 'wb') as f:
#     imge.save(f, format='png')