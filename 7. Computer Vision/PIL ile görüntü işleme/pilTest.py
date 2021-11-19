from PIL import Image, ImageFilter
from PIL import ImageEnhance

im = Image.open('ornek.png')

im = im.convert("RGB")

enh = ImageEnhance.Contrast(im)
im = enh.enhance(1.8)

im = im.rotate(45)

im.save('sonuc.png')
