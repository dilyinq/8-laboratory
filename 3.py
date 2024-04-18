from PIL import ImageFont, Image, ImageDraw

name = input("Введите ваше имя: ")
recipient_name = input("Введите имя того, кого вы хотите поздравить: ")

img = Image.open("открытка.jpg")

# Создание объекта ImageDraw
draw = ImageDraw.Draw(img)

font = ImageFont.truetype("arial.ttf", 90)

# Добавление текста на изображение
draw.text((50,50), recipient_name + ", поздравляю " + "!", (255,255,255), font=font)

# Сохранение новой открытки
img.save('открытка с надписью.jpg')