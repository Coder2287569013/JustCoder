import pygame
from random import choice, randrange

pygame.init()

w,h = 1920,1080
res = (w,h)

font_s = 35
alpha_value = randrange(30,40,5)

chars = ['ｦ', 'ｱ', 'ｳ', 'ｴ', 'ｵ', 'ｶ', 'ｷ', 'ｹ', 'ｺ', 'ｻ', 'ｼ', 'ｽ', 'ｾ', 'ｿ', 'ﾀ', 'ﾂ', 'ﾃ', 'ﾅ', 'ﾆ', 'ﾇ', 'ﾈ',
         'ﾊ', 'ﾋ', 'ﾎ', 'ﾏ', 'ﾐ', 'ﾑ', 'ﾒ', 'ﾓ', 'ﾔ', 'ﾕ', 'ﾗ', 'ﾘ', 'ﾜ', '9', '8', '7', '5', '2', '1', ':', '.',
         '"', '=', '*', '+', '-', '¦', '|', '_', '╌', '日', '0', 'A', 'B', 'C', 'D', '?', 'Z', 'H', 'W', 'F', 'Q', 
         '<', '>', 'a', 'b', 'c', 'd', 'z', 'h', 'w', 'f', 'q']

font = pygame.font.Font('MS mincho.ttf', font_s)
font_2 = pygame.font.Font('MS mincho.ttf', font_s - font_s // 6)
font_3 = pygame.font.Font('MS mincho.ttf', font_s - font_s // 3)

grn_chars = [font.render(char, True, (randrange(0, 255), randrange(0,255), randrange(0,255))) for char in chars]
grn_chars_2 = [font_2.render(char, True, (randrange(0,255), randrange(0,255), randrange(0,255)))for char in chars]
grn_chars_3 = [font_3.render(char, True, (randrange(0,255), randrange(0,255), randrange(0,255)))for char in chars]

sc = pygame.display.set_mode(res)
display_s = pygame.Surface(res)
display_s.set_alpha(alpha_value)

clock = pygame.time.Clock()

class Symbol:
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.value = choice(grn_chars)
        self.speed = 40

    def draw(self):
        self.value = choice(grn_chars)
        self.y = self.y + self.speed if self.y < h else -font_s*randrange(1,10)
        sc.blit(self.value, (self.x, self.y))
    def draw_2(self):
        self.value_2 = choice(grn_chars_2)
        self.y = self.y + self.speed if self.y < h else -font_s*randrange(1,10)
        sc.blit(self.value_2, (self.x, self.y))
    def draw_3(self):
        self.value_3 = choice(grn_chars_3)
        self.y = self.y + self.speed if self.y < h else -font_s*randrange(1,10)
        sc.blit(self.value_3, (self.x, self.y))

symbols = [Symbol(x, randrange(-h, 0)) for x in range(0, w, font_s * 3)]
symbols_2 = [Symbol(x, randrange(-h, 0))for x in range(font_s, w, font_s * 3)]
symbols_3 = [Symbol(x, randrange(-h, 0))for x in range(font_s*2, w, font_s * 3)]

run = True
while run:
    sc.blit(display_s, (0,0))
    display_s.fill(pygame.Color('black'))

    [symbol.draw()for symbol in symbols]
    [symbol_2.draw_2()for symbol_2 in symbols_2]
    [symbol_3.draw_3()for symbol_3 in symbols_3]

    pygame.time.delay(200)
    pygame.display.update()
    clock.tick(120)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False