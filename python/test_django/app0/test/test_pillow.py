from PIL import Image, ImageDraw


img = Image.new(mode="RGB",  size=(120,30), color=(255,255,255))

draw = ImageDraw.Draw(img, mode="RGB")

draw.text([0,0], 'python', 'red')

with open('code.png', 'wb') as f:
    img.save(f, format='png')