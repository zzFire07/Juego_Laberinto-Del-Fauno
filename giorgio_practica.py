import pygame
pygame.init()


def movimiento_jugador():
    if keys_pressed[pygame.K_a] or keys_pressed[pygame.K_LEFT] and jugador.x - vel > 0: #SI SE APRETA A O FLECHA IZQUIERDA SE MUEVE 3 PIXELES HACÍA AHÍ
    if keys_pressed[pygame.K_d] or keys_pressed[pygame.K_RIGHT] and jugador.x + vel < 1000: #SI SE APRETA D O FLECHA DERECHA SE MUEVE 3 PIXELES HACÍA AHÍ
    if keys_pressed[pygame.K_w] or keys_pressed[pygame.K_UP] and jugador.y + vel < 600: #SI SE APRETA W O FLECHA SUPERIOR SE MUEVE 3 PIXELES HACÍA AHÍ
    if keys_pressed[pygame.K_s] or keys_pressed[pygame.K_DOWN] and jugador.y - vel > 0: #SI SE APRETA S O FLECHA INFERIOR SE MUEVE 3 PIXELES HACÍA AHÍ



blanco = (255, 255, 255)
negro = (0, 0, 0)
rojo = (255, 0, 0)
azul = (0, 0, 255)

dimensiones = 1000, 600

VEL = 10
FPS = 60

largo_jugador, alto_jugador = 40, 40
jugador_imagen = pygame.draw.rect()
def main():
    run = True

    #CREAR VENTANA
    ventana = pygame.display.set_mode(dimensiones)
    pygame.display.set_caption("Laberinto del fauno")

    #PROGRAMA MAIN
    while run == True:

        clock.tick(FPS)

        for event in pygame.event.get():
            print(event)
            
            if event.type == pygame.QUIT:
            run = False
