from pygame import *
window = display.set_mode((700, 500))#the window created in the previous step
picture = transform.scale(image.load('background.jpg'), (700, 500))
run = True
while run: 
    window.blit(picture,(0,0))
    display.update()
quit()