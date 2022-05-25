import pygame, os
pygame.init()


def movimiento_jugador(keys_pressed, jugador):
    if keys_pressed[pygame.K_a] or keys_pressed[pygame.K_LEFT]: #SI SE APRETA A O FLECHA IZQUIERDA SE MUEVE 3 PIXELES HACÍA AHÍ
        jugador.x -= vel
    if keys_pressed[pygame.K_d] or keys_pressed[pygame.K_RIGHT]: #SI SE APRETA D O FLECHA DERECHA SE MUEVE 3 PIXELES HACÍA AHÍ
        jugador.x += vel
    if keys_pressed[pygame.K_w] or keys_pressed[pygame.K_UP]: #SI SE APRETA W O FLECHA SUPERIOR SE MUEVE 3 PIXELES HACÍA AHÍ
        jugador.y -= vel
    if keys_pressed[pygame.K_s] or keys_pressed[pygame.K_DOWN]: #SI SE APRETA S O FLECHA INFERIOR SE MUEVE 3 PIXELES HACÍA AHÍ
        jugador.y += vel


blanco = (255, 255, 255)
negro = (0, 0, 0)
rojo = (255, 0, 0)
azul = (0, 0, 255)

ancho, alto = 1000, 600
ventana = pygame.display.set_mode((ancho, alto))
pygame.display.set_caption("Laberinto del fauno")

vel = 4
FPS = 60

largo_jugador, alto_jugador = 40, 40

imagen = pygame.image.load("labim.jpg")
imagen = pygame.transform.scale(imagen, (1000,600))

imagen_jugador = pygame.image.load("stickman.jpg")
imagen_jugador = pygame.transform.scale(imagen_jugador, (largo_jugador, alto_jugador))

def mov_imagenes(jugador):
    ventana.blit(imagen, (0, 0))
    ventana.blit(imagen_jugador, (jugador.x, jugador.y))

    pygame.display.update()

def main():import pygame, os
pygame.init()


def movimiento_jugador(keys_pressed, jugador):
    if keys_pressed[pygame.K_a] or keys_pressed[pygame.K_LEFT] and jugador.x > 0: #SI SE APRETA A O FLECHA IZQUIERDA SE MUEVE 3 PIXELES HACÍA AHÍ
        jugador.x -= vel
    if keys_pressed[pygame.K_d] or keys_pressed[pygame.K_RIGHT] and jugador.x + largo_jugador < 1000: #SI SE APRETA D O FLECHA DERECHA SE MUEVE 3 PIXELES HACÍA AHÍ
        jugador.x += vel
    if keys_pressed[pygame.K_w] or keys_pressed[pygame.K_UP] and jugador.y > 0: #SI SE APRETA W O FLECHA SUPERIOR SE MUEVE 3 PIXELES HACÍA AHÍ
        jugador.y -= vel
    if keys_pressed[pygame.K_s] or keys_pressed[pygame.K_DOWN] and jugador.y + alto_jugador < 600: #SI SE APRETA S O FLECHA INFERIOR SE MUEVE 3 PIXELES HACÍA AHÍ
        jugador.y += vel


blanco = (255, 255, 255)
negro = (0, 0, 0)
rojo = (255, 0, 0)
azul = (0, 0, 255)

ancho, alto = 1000, 600
ventana = pygame.display.set_mode((ancho, alto))
pygame.display.set_caption("Laberinto del fauno")

vel = 4
FPS = 60

largo_jugador, alto_jugador = 40, 40

imagen = pygame.image.load("labim.jpg")
imagen = pygame.transform.scale(imagen, (1000,600))

imagen_jugador = pygame.image.load("stickman.jpg")
imagen_jugador = pygame.transform.scale(imagen_jugador, (largo_jugador, alto_jugador))

def mov_imagenes(jugador):
    ventana.blit(imagen, (0, 0))
    ventana.blit(imagen_jugador, (jugador.x, jugador.y))

    pygame.display.update()

def main():
    jugador = pygame.Rect(500, 250, largo_jugador, alto_jugador)

    clock = pygame.time.Clock()
    run = True

    #PROGRAMA MAIN
    while run == True:

        clock.tick(FPS)
        ventana.blit(imagen, (0,0))
        ventana.blit(imagen_jugador, (jugador.x, jugador.y))

        for event in pygame.event.get():
            print(event)

            if event.type == pygame.QUIT:
                run = False

        keys_pressed = pygame.key.get_pressed()
        movimiento_jugador(keys_pressed, jugador)
        mov_imagenes(jugador)

main()

    jugador = pygame.Rect(500, 250, largo_jugador, alto_jugador)

    clock = pygame.time.Clock()
    run = True

    #PROGRAMA MAIN
    while run == True:

        clock.tick(FPS)
        ventana.blit(imagen, (0,0))
        ventana.blit(imagen_jugador, (jugador.x, jugador.y))

        for event in pygame.event.get():
            print(event)

            if event.type == pygame.QUIT:
                run = False

        keys_pressed = pygame.key.get_preassdadassed()
        movimiento_jugador(qqkeys_pressed, jugadoasdadr)
        mov_imagenes(jugador)

main()
