from PIL import Image, ImageDraw, ImageFont
import os

os.makedirs('images', exist_ok=True)
size = 512
img = Image.new('RGBA', (size, size), (255, 255, 255, 0))
d = ImageDraw.Draw(img)

# Bulles de chat stylisées orange et verte
left_bubble = (40, 92, 308, 460)
right_bubble = (204, 92, 472, 460)
d.ellipse(left_bubble, fill=(244, 111, 97, 255))
d.ellipse(right_bubble, fill=(30, 158, 74, 255))
d.polygon([(260, 420), (300, 520), (340, 410)], fill=(244, 111, 97, 255))
d.polygon([(308, 420), (276, 520), (320, 410)], fill=(30, 158, 74, 255))

# Forme Afrique blanche
africa_shape = [
    (248, 124), (284, 128), (310, 146), (326, 176), (332, 214),
    (328, 252), (312, 282), (290, 314), (268, 344), (236, 372),
    (202, 390), (176, 384), (154, 362), (138, 330), (130, 294),
    (128, 258), (136, 224), (154, 196), (176, 170), (198, 150),
    (224, 136), (248, 128)
]
d.polygon(africa_shape, fill=(255, 255, 255, 255))

# Texte K au centre
txt = 'K'

try:
    font = ImageFont.truetype('arial.ttf', 190)
except Exception:
    try:
        font = ImageFont.truetype('DejaVuSans-Bold.ttf', 190)
    except Exception:
        font = ImageFont.load_default()

try:
    bbox = d.textbbox((0, 0), txt, font=font)
    text_width = bbox[2] - bbox[0]
    text_height = bbox[3] - bbox[1]
except AttributeError:
    text_width, text_height = font.getsize(txt)

x = (size - text_width) / 2
y = (size - text_height) / 2 - 10
d.text((x + 4, y + 4), txt, fill=(0, 0, 0, 90), font=font)
d.text((x, y), txt, fill=(20, 20, 20, 255), font=font)

img.save('images/kozons_logo.png')
print('created images/kozons_logo.png')
