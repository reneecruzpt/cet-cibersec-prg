from pygame import *

#parent class for other classes
class GameSprite(sprite.Sprite):
# constructor of the class
    def __init__(self, player_image, player_x, player_y, size_x, size_y):
        # Calling for the constructor of the class (Sprite):
        sprite.Sprite.__init__(self)
        # each sprite needs to have image 
        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        # each sprite must store the property rect - the rectangle in which it is inscribed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    # method that draws the hero on the window
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))


class Player(GameSprite):
#a method that implements sprite control by keyboard arrow buttons
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_x_speed,player_y_speed):
        # Calling for the constructor of the class (Sprite):
        GameSprite.__init__(self, player_image, player_x, player_y,size_x, size_y)
        self.x_speed = player_x_speed
        self.y_speed = player_y_speed
    def update(self):
        ''' moves the character using the current horizontal and vertical speed'''
        
        #move horizontally
        self.rect.x += self.x_speed
        platforms_touched = sprite.spritecollide(self, walls, False)
        if self.x_speed > 0: #a mover para a direita
            for p in platforms_touched:
                self.rect.right = min(self.rect.right,p.rect.left) #troca a posição do jogador
        elif self.x_speed < 0: #a mover para a esquerda
            for p in platforms_touched:
                self.rect.left = max(self.rect.left,p.rect.right) #troca a posição do jogador

        #move vertically
        self.rect.y += self.y_speed
        platforms_touched = sprite.spritecollide(self, walls, False)
        if self.y_speed > 0: #a mover para baixo
            for p in platforms_touched:
                self.rect.bottom = min(self.rect.bottom,p.rect.top) #troca a posição do jogador
        elif self.y_speed < 0: #a mover para cima
            for p in platforms_touched:
                self.rect.top = max(self.rect.top,p.rect.bottom) #troca a posição do jogador

#Creating window
win_width = 700
win_height = 500
display.set_caption("Maze")
window = display.set_mode((win_width, win_height))
back = (119, 210, 223)#set the color according to the RGB color scheme

#create wall pictures
w1 = GameSprite('platform2.png',win_width / 2 - win_width / 3, win_height / 2, 300, 50)
w2 = GameSprite('platform2_v.png', 370, 100, 50, 400)

#criando grupos de sprites e adicionando as paredes ao grupo
walls = sprite.Group()
walls.add(w1)
walls.add(w2)

#Creating sprites
packman = Player('hero.png', 5, win_height - 80, 80, 80, 0, 0)
final = GameSprite('trophy.png',630,450,50,50)

#game loop
run = True
finish = False
victory = False

win = transform.scale(image.load('thumb.jpg'),(700,500))
lose = transform.scale(image.load('game-over_1.png'),(700,500))


while run:
#loop runs every 0.05 seconds
    for e in event.get():
        if e.type == QUIT:
            run = False
        elif e.type == KEYDOWN:
            if e.key == K_LEFT:
                packman.x_speed = -5
            elif e.key == K_RIGHT:
                packman.x_speed = 5
            elif e.key == K_UP:
                packman.y_speed = -5
            elif e.key == K_DOWN:
                packman.y_speed = 5
        elif e.type == KEYUP:
            if e.key == K_LEFT:
                packman.x_speed = 0
            elif e.key == K_RIGHT:
                packman.x_speed = 0
            elif e.key == K_UP:
                packman.y_speed = 0
            elif e.key == K_DOWN:
                packman.y_speed = 0
    if finish != True:
        window.fill(back)#color the window
        #draw objects
        w1.reset()
        w2.reset()
        packman.reset()
        final.reset()
        #turn on the movement
        packman.update()
        if sprite.collide_rect(packman,final):
            finish = True
            victory = True
        # if sprite.spritecollide(packman, walls, False):
        #     finish = True
    else:
        if victory == True:
            window.blit(win,(0,0))
        else:
            window.blit(lose,(0,0))
    display.update()
    time.delay(50)