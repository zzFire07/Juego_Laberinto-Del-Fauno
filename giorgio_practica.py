import pygame, os
pygame.init()


def movimiento_jugador(keys_pressed, jugador): #Funcion para el movimiento del jugador.
    if keys_pressed[pygame.K_a] or keys_pressed[pygame.K_LEFT]: #SI SE APRETA A O FLECHA IZQUIERDA SE MUEVE 4 PIXELES HACÍA LA IZQUIERDA.
        jugador.x -= vel
    if keys_pressed[pygame.K_d] or keys_pressed[pygame.K_RIGHT]: #SI SE APRETA D O FLECHA DERECHA SE MUEVE 4 PIXELES HACÍA LA DERECHA.
        jugador.x += vel
    if keys_pressed[pygame.K_w] or keys_pressed[pygame.K_UP]: #SI SE APRETA W O FLECHA SUPERIOR SE MUEVE 4 PIXELES HACÍA ARRIBA.
        jugador.y -= vel
    if keys_pressed[pygame.K_s] or keys_pressed[pygame.K_DOWN]: #SI SE APRETA S O FLECHA INFERIOR SE MUEVE 4 PIXELES HACÍA ABAJO.
        jugador.y += vel

def mov_imagenes(jugador): #Funcion para las imagenes en el juego
    ventana.blit(imagen, (0, 0)) #Se crea el fondo del juego.
    ventana.blit(imagen_jugador, (jugador.x, jugador.y)) #Se crea la imagen del jugador.

    pygame.display.update() #Actualiza las imagenes.

def main():
    jugador = pygame.Rect(500, 250, largo_jugador, alto_jugador) #Se crea el objeto jugador.

    clock = pygame.time.Clock()
    run = True

    #PROGRAMA MAIN
    while run == True:

        clock.tick(FPS) #Se limitan los fotogramas a "FPS".
        ventana.blit(imagen, (0,0))
        ventana.blit(imagen_jugador, (jugador.x, jugador.y))

        for event in pygame.event.get():
            if event.type == pygame.QUIT: #Se terminara el bucle si se cierra la ventana.
                run = False

        keys_pressed = pygame.key.get_pressed() #Registra las teclas presionadas y las asigna.
        movimiento_jugador(keys_pressed, jugador #Llama a la funcion para mover al jugador.
        mov_imagenes(jugador) #Llama a la funcion para dibujar las imagenes.

#------------------------------------------------------------------------------#
#COLORES
blanco = (255, 255, 255)
negro = (0, 0, 0)
rojo = (255, 0, 0)
azul = (0, 0, 255)

#CONSTANTES
vel = 4 #Velocidad del jugador
FPS = 60 #Fotogramas por segundo que tendra el programa

ancho, alto = 1000, 600 #Dimensiones de la ventana del juego
ventana = pygame.display.set_mode((ancho, alto)) #Se crea la ventana del juego.
pygame.display.set_caption("Laberinto del fauno") #NOMBRE DEL JUEGO


imagen = pygame.image.load("labim.jpg") #Cargamos la imagen que representara al jugador
imagen = pygame.transform.scale(imagen, (1000,600)) #Escalamos la imagen al tamaño de la ventana.

largo_jugador, alto_jugador = 40, 40 #Dimensiones del jugador
imagen_jugador = pygame.transform.scale(pygame.image.load("stickman.jpg"), (largo_jugador, alto_jugador))


main()
                           
