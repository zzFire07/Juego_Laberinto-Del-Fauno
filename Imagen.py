import pygame

ventana=pygame.display.set_mode((800,600))
clock=pygame.time.Clock()

done=False

imagen=pygame.image.load("labim.jpg")
imagen = pygame.transform.scale(imagen, (800,600))
while not done:
    for event in pygame.event.get():
       if event.type==pygame.QUIT:
           done=True
    
    ventana.blit(imagen, [0,0])

    pygame.display.flip()
    clock.tick(60)

done=False


pygame.quit()
