import pygame
from random import choice
from tkinter import messagebox

pygame.init()


class Block:
    def __init__(self, _x, _y, color):
        self.x = _x
        self.y = _y
        self.color = color
        self.rect = pygame.Rect(_x, _y, 50, 50)
        self.text = ''

    def setText(self, text=''):
        self.text = text

    def draw(self):
        pygame.draw.rect(scr, self.color, self.rect, 1, 0)  # рисуем квадрат
        font = pygame.font.SysFont('verdana', 25).render(self.text, True, 'white')  # создём шрифт для текста
        scr.blit(font, (self.rect.x + 15, self.rect.y + 5))


width = 800
height = 600
scr = pygame.display.set_mode((width, height))
score = 0
fails = 0
Win = False

man_image = pygame.image.load('img\Group 2.png')
man_rect = pygame.Rect(120, 170, 92, 252)

viselitsya_image1 = pygame.image.load("img\Line 6.png")
viselitsya_image1_rect = pygame.Rect(50, 125, 200, 1)

viselitsya_image2 = pygame.image.load("img\Line 7.png")
viselitsya_image2_rect = pygame.Rect(50, 125, 200, 1)

stul_image = pygame.image.load("img\Group 1.png")
stul_image_rect = pygame.Rect(120, 270, 200, 1)

petlya_image = pygame.image.load("img\Group 3.png")
petlya_image_rect = pygame.Rect(125, 125, 200, 1)


words = ["чайка", "дом", "дверь", "червяк", "конституция"]
word = choice(words)
spisok = []

x = 50
for i in range(len(word)):
    spisok.append(Block(x, 50, "white"))
    spisok[i].setText('')
    x += 50

keys = ["А", "Б", "В", "Г", "Д", "Е", "Ё", "Ж", "З", "И", "Й", "К", "Л", "М", "Н", "О", "П", "Р", "С", "Т", "У", "Ф",
        "Х", "Ц", "Ч", "Ш", "Щ", "Ъ", "Ы", "Ь", "Э", "Ю", "Я"]
keyboard = []
x = 50
y = 400
for i in range(len(keys)):
    keyboard.append(Block(x, y, 'blue'))
    keyboard[i].setText(keys[i])
    x += 50
    if i > 0 and i % 11 == 0:
        x = 50
        y += 50

GameOver = False
while not GameOver:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            GameOver = True
        if event.type == pygame.MOUSEBUTTONDOWN:
            for key in keyboard:
                if key.rect.collidepoint(event.pos):
                    keyboard.remove(key)
                    isGues = False
                    for i in range(len(word)):
                        if word[i].lower() == key.text.lower():
                            spisok[i].setText(key.text)
                            score += 1
                            isGues = True
                    if not isGues:
                        fails += 1

    scr.fill('black')

    scr.blit(man_image, man_rect)

    if fails >= 1:
        scr.blit(viselitsya_image1, viselitsya_image1_rect)
    if fails >= 2:
        scr.blit(viselitsya_image2, viselitsya_image2_rect)
    if fails >= 3:
        scr.blit(petlya_image, petlya_image_rect)



    for el in spisok:
        el.draw()

    for i in range(len(keyboard)):
        keyboard[i].draw()

    if score == len(word):
        GameOver = True
        Win = True
    elif fails == 4:
        Win = False
        GameOver = True
        stul_image = pygame.transform.rotate(stul_image, 90)

    scr.blit(stul_image, stul_image_rect)
    pygame.display.update()

if Win:
    messagebox.showinfo("Успіх!", f"Гру завершено\nВи ПЕРЕМОЖЕЦЬ!!!")
else:
    messagebox.showinfo("Невдача", f"Гру завершено\nНевгадане слово: {word}")