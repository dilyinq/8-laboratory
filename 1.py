from PIL import Image

image = Image.open("открытка.jpg")

area = (200, 150, 1000, 1000)  # (лево, верх, право, низ)

cropped_image = image.crop(area)

cropped_image.save("обрезанная_открытка.jpg")