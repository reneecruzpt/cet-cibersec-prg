#importação da biblioteca
from pygame import *

#implementação de constantes
W_WIDTH = 700
W_HEIGHT = 500
BACK = (255,255,255)
GREEN = (0,255,0)
GROUND_Y = 310
GRAVITY = 1  # Gravidade que será aplicada ao jogador (puxando-o para baixo)
JUMP_STRENGTH = -15  # Força do salto, valor negativo para subir

#criação da janela
window = display.set_mode((W_WIDTH,W_HEIGHT))

#preenchimento do background com cor
#window.fill(BACK)

#preenchimento do background com imagem
background = image.load('background.jpg')

#redimensionamento da imagem 
background = transform.scale(background,(W_WIDTH,W_HEIGHT))

#nomear a janela
display.set_caption('Maze Game')

#classe base
class GameSprite(sprite.Sprite):
    def __init__(self,picture,w,h,x,y,): #construtor
        super().__init__() #construtor da parent class
        self.image = transform.scale(image.load(picture),(w,h)) #carregamento e redimensionamento da imagem
        self.rect = self.image.get_rect() #definicação do retângulo da imagem
        self.rect.x = x #posição do retângulo (imagem) no eixo x
        self.rect.y = y #posição do retângulo (imagem) no eixo x

    def draw(self): #metodo para a criação da imagem nas posições definidas
        window.blit(self.image,(self.rect.x,self.rect.y))

#child class para o player
class Player(GameSprite): 
    def __init__(self, picture, w, h, x, y, x_speed, y_speed): #construtor da classe, possui a propriedade speed para controlar a movimentação
        super().__init__(picture, w, h, x, y) #construtor da superclasse
        self.x_speed = x_speed #velocidade de movimentação no eixo x
        self.y_speed = y_speed # velocidade de movimentação no eixo y
        self.is_jumping = False  # Controle se o jogador está no ar

    def update(self): #método para atualizar a posição do player na tela / também calcula as colisões
        # Armazenar a posição anterior para calcular o movimento
        # prev_x = self.rect.x
        # prev_y = self.rect.y

        # Movimento horizontal
        if self.rect.x >= 0 and self.rect.x <= 650: #limita os extremos do ecrã no eixo x
            self.rect.x += self.x_speed
        elif self.rect.x < 0: # impede que o player vá para um x negativo 
            self.rect.x = 0
        else:
            self.rect.x = 650 #impede que o player exceda 650px no eixo x

        platforms_touched = sprite.spritecollide(self, walls, False) #uma lista que verifica a colisão entre o player e as paredes
        
        if self.x_speed > 0:  # Movendo para a direita
            for p in platforms_touched:
                self.rect.right = p.rect.left # Impede que o jogador atravesse a parede pela direita
        elif self.x_speed < 0:  # Movendo para a esquerda
            for p in platforms_touched:
                self.rect.left = p.rect.right # Impede que o jogador atravesse a parede pela esquerda

        # Movimento vertical
        self.y_speed += GRAVITY  # Aplicar gravidade (no loop incrementa em 1 até chegar a zero)
        self.rect.y += self.y_speed

        platforms_touched = sprite.spritecollide(self, walls, False) #uma lista que verifica a colisão entre o player e as paredes

        # Se estiver caindo
        if self.y_speed > 0:
            for p in platforms_touched:
                # Colisão com a parte superior da parede
                if self.rect.bottom > p.rect.top: #impede que o player se "teletransporte" para cima da parede
                    self.rect.bottom = p.rect.top
                    self.y_speed = 0
                    self.is_jumping = False  # Permite que o jogador pule novamente
        # Se estiver subindo
        elif self.y_speed < 0:
            for p in platforms_touched:
                # Colisão com a parte inferior da parede
                if self.rect.top < p.rect.bottom: #impede que o player se "teletransporte" para baixo da parede
                    self.rect.top = p.rect.bottom
                    self.y_speed = 0

        # Impedir que o jogador vá abaixo do chão
        if self.rect.y > GROUND_Y:
            self.rect.y = GROUND_Y
            self.y_speed = 0
            self.is_jumping = False

    def jump(self): #método para saltar
        if not self.is_jumping:  # Somente permitir o salto se o jogador estiver no chão
            self.y_speed = JUMP_STRENGTH  # Aplicar o salto
            self.is_jumping = True  # Marca o jogador como no ar


#instâncias de sprites sprites
wall1 = GameSprite('wall.png',50,50,120,310)
wall2 = GameSprite('wall.png',50,50,200,100)
wall3 = GameSprite('wall.png',50,50,230,250)
wall4 = GameSprite('wall.png',50,50,500,250)

player = Player('player_r.png',50,50,0,310,0,0)
enemy1 = Player('enemy1.png',50,50,400,310,0,0)
enemy2 = Player('enemy1.png',50,50,500,200,0,0)

#win = GameSprite('you-win.png',200,200,150,150)

#variáveis de controle
run = True #loop
finish = False #gameplay

#loop principal do jogo
while run:
    #ciclo para capturar eventos
    for e in event.get():
        if e.type == QUIT:
            run = False
        elif e.type == KEYDOWN:
            if e.key == K_UP:
                player.y_speed = -5
            elif e.key == K_DOWN:
                    player.y_speed = +5
            elif e.key == K_RIGHT:
                player.x_speed = +5
            elif e.key == K_LEFT:
                player.x_speed = -5 
            elif e.key == K_SPACE:
                player.jump()
                
        elif e.type == KEYUP:
            if e.key == K_UP:
                player.y_speed = 0
            elif e.key == K_DOWN:
                player.y_speed = 0
            elif e.key == K_RIGHT:
                player.x_speed = 0
            elif e.key == K_LEFT:
                player.x_speed = 0
                
    if finish != True:
        #posicionamento do background no ecrã
        window.blit(background,(0,0))
        
        #posicionamento dos objetos no ecrã
        wall1.draw()
        wall2.draw()
        wall3.draw()
        wall4.draw()
        
        walls = sprite.Group()
        walls.add(wall1)
        walls.add(wall2)
        walls.add(wall3)
        walls.add(wall4)
        
        player.draw()
        enemy1.draw()
        enemy2.draw()
        
        #atualização da posição do player
        player.update()
        if sprite.collide_rect(player,enemy1) or sprite.collide_rect(player,enemy2):
            finish = True
            window.blit(transform.scale(image.load('game-over.png'),(W_WIDTH/2,W_HEIGHT/2)),(W_WIDTH/4,W_HEIGHT/4))
            # font.init()
            # font = font.SysFont('Arial',40)
            # winning = font.render('YOU WIN!',True,(255,215,0))
            # window.blit(winning,(0,0))
    else:
        #adicionar uma imagem ou mensagem final
        pass
    #delay para tornar possível realizar a captura dos eventos
    time.delay(50)
    
    #atualização do ecrã        
    display.update()