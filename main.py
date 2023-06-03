import pygame
from random import choice
pygame.init()


class Block:
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color
        self.rect = pygame.Rect(x, y, 50, 50)

    def setText(self, text=''):
        font = pygame.font.SysFont('verdana', 25).render(text, True, 'white')  # создём шрифт для текста
        scr.blit(font, (self.rect.x, self.rect.y))  # отображаем наш текст

    def draw(self):
        pygame.draw.rect(scr, self.color, self.rect, 1, 0)  # рисуем квадрат



width = 800
height = 600
scr = pygame.display.set_mode((width, height))

words = ["чайка", "дом", "дверь"]
word = choice(words)
spisok = []
x = 50
for i in range(len(word)):
    spisok.append(Block(x, 50, "white"))
    spisok[i].draw()
    spisok[i].setText(word[i])
    x += 50

GameOver = False
while not GameOver:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            GameOver = True

    scr.fill('black')

    for el in spisok:
        el.draw()

    pygame.display.update()
