import pygame
from random import choice
pygame.init()


class Block:
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color
        self.rect = pygame.Rect(x, y, 50, 50)
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


words = ["чайка", "дом", "дверь", "червяк", "конституция"]
word = choice(words)
spisok = []

fails_text = Block(750, 0, 'white')


x = 50
for i in range(len(word)):
    spisok.append(Block(x, 50, "white"))
    spisok[i].setText('')
    x += 50

keys = ["А", "Б", "В", "Г", "Д", "Е", "Ё", "Ж", "З", "И", "Й", "К", "Л", "М", "Н", "О", "П", "Р", "С", "Т", "У", "Ф", "Х",
        "Ц", "Ч", "Ш", "Щ", "Ъ", "Ы", "Ь", "Э", "Ю", "Я"]
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
                    fails += 1
                    for i in range(len(word)):
                        if word[i].lower() == key.text.lower():
                            spisok[i].setText(key.text)
                            score += 1
                            fails -= 1
    scr.fill('black')

    fails_text.setText(str(fails))
    fails_text.draw()

    for el in spisok:
        el.draw()

    for i in range(len(keyboard)):
        keyboard[i].draw()

    if score == len(word):
        GameOver = True
    elif fails == 4:
        GameOver = True

    pygame.display.update()
