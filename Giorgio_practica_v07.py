import pygame, os
pygame.init()


def movimiento_jugador(keys_pressed, jugador): #Funcion para el movimiento del jugador
    if keys_pressed[pygame.K_a] or keys_pressed[pygame.K_LEFT] and jugador.x > 0: #SI SE APRETA A O FLECHA IZQUIERDA SE MUEVE 4 PIXELES HACÍA LA IZQUIERDA
        jugador.x -= vel
    if keys_pressed[pygame.K_d] or keys_pressed[pygame.K_RIGHT] and jugador.x + largo_jugador < ancho: #SI SE APRETA D O FLECHA DERECHA SE MUEVE 4 PIXELES HACÍA LA DERECHA
        jugador.x += vel
    if keys_pressed[pygame.K_w] or keys_pressed[pygame.K_UP] and jugador.y > 0: #SI SE APRETA W O FLECHA SUPERIOR SE MUEVE 4 PIXELES HACÍA ARRIBA
        jugador.y -= vel
    if keys_pressed[pygame.K_s] or keys_pressed[pygame.K_DOWN] and jugador.y + alto_jugador < alto: #SI SE APRETA S O FLECHA INFERIOR SE MUEVE 4 PIXELES HACÍA ABAJO
        jugador.y += vel

def mov_imagenes(jugador): #Funcion para las imagenes en el juego
    ventana.fill(blanco)
    ventana.blit(imagen, (0, 0))
    ventana.blit(imagen_jugador, (jugador.x, jugador.y))

    pygame.display.update()

def main():
    jugador = pygame.Rect(400, 15, largo_jugador, alto_jugador)

    clock = pygame.time.Clock()
    run = True

    #PROGRAMA MAIN
    while run == True:

        clock.tick(FPS) #Se limitan los fotogramas a "FPS"

        for event in pygame.event.get():
            if event.type == pygame.QUIT: #Se terminara el bucle si se cierra la ventana.
                run = False

        keys_pressed = pygame.key.get_pressed()
        movimiento_jugador(keys_pressed, jugador)
        mov_imagenes(jugador)

#------------------------------------------------------------------------------#
#COLORES
blanco = (255, 255, 255)
negro = (0, 0, 0)
rojo = (255, 0, 0)
azul = (0, 0, 255)

#CONSTANTES
vel = 2 #Velocidad del jugador
FPS = 60 #Fotogramas por segundo que tendra el programa

ancho, alto = 800, 600 #Dimensiones de la ventana del juego
ventana = pygame.display.set_mode((ancho, alto))
pygame.display.set_caption("Laberinto del fauno") #NOMBRE DEL JUEGO


imagen = pygame.image.load("laberinto.svg") #Cargamos la imagen que representara al jugador
imagen = pygame.transform.scale(imagen, (ancho, alto))

largo_jugador, alto_jugador = 20, 20 #Dimensiones del jugador
imagen_jugador = pygame.transform.scale(pygame.image.load("circ_rojo.png"), (largo_jugador, alto_jugador))


main()
