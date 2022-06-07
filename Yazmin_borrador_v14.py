import pygame, os, sys, pygame.display, itertools, time

pygame.init()

CONT_PASOS = 0
start = time.time() #Comienzo de timer

    
def collide_DOWN(jugador):
    choque = False
    for i in range (1, largo_jugador):
        pixeles_fondo = pygame.Surface.get_at(fondo, (jugador.x + i, jugador.y + 20))
        if pixeles_fondo == (0, 0, 0, 255):
            choque = False
    return choque

def collide_UP(jugador):
    choque = False
    for i in range (1, largo_jugador):
        pixeles_fondo = pygame.Surface.get_at(fondo, (jugador.x + i, jugador.y))
        if pixeles_fondo == (0, 0, 0, 255):
            choque = True
    return choque

def collide_RIGHT(jugador):
    choque = False
    for i in range (1, largo_jugador):
        pixeles_fondo = pygame.Surface.get_at(fondo, (jugador.x + 20, jugador.y + i))
        if pixeles_fondo == (0, 0, 0, 255):
            choque = True
    return choque

def collide_LEFT(jugador):
    choque = False
    for i in range (1, largo_jugador):
        pixeles_fondo = pygame.Surface.get_at(fondo, (jugador.x, jugador.y + i))
        if pixeles_fondo == (0, 0, 0, 255):
            choque = True
    return choque


def movimiento_jugador(keys_pressed, jugador): #Funcion para el movimiento del jugador
    global CONT_PASOS
    if keys_pressed[pygame.K_a] or keys_pressed[pygame.K_LEFT]: #SI SE APRETA A O FLECHA IZQUIERDA SE MUEVE 1 PIXELES HACÍA LA IZQUIERDA
        if collide_LEFT(jugador) == False:
            jugador.x -= vel
            CONT_PASOS += 1
    if keys_pressed[pygame.K_d] or keys_pressed[pygame.K_RIGHT]: #SI SE APRETA D O FLECHA DERECHA SE MUEVE 1 PIXELES HACÍA LA DERECHA
        if collide_RIGHT(jugador) == False:
            jugador.x += vel
            CONT_PASOS += 1
    if keys_pressed[pygame.K_w] or keys_pressed[pygame.K_UP]: #SI SE APRETA W O FLECHA SUPERIOR SE MUEVE 1 PIXELES HACÍA ARRIBA
        if collide_UP(jugador) == False:
            jugador.y -= vel
            CONT_PASOS += 1
    if keys_pressed[pygame.K_s] or keys_pressed[pygame.K_DOWN]: #SI SE APRETA S O FLECHA INFERIOR SE MUEVE 1 PIXELES HACÍA ABAJO
        if collide_DOWN(jugador) == False:
            jugador.y += vel
            CONT_PASOS += 1
         

def mov_imagenes(jugador): #Funcion para las imagenes en el juego
    ventana.fill(blanco)
    ventana.blit(fondo, (0, 0))
    ventana.blit(imagen_jugador, (jugador.x, jugador.y))
   
    
    pygame.display.update()

def main():
    jugador = pygame.Rect(ancho/2, alto/2, largo_jugador, alto_jugador)

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
        collide_DOWN(jugador)
        print(CONT_PASOS)
        if jugador.y > alto - alto_jugador - 4:
            run = False


#COLORES
blanco = (255, 255, 255)
negro = (0, 0, 0)
rojo = (255, 0, 0)
azul = (0, 0, 255)

#CONSTANTES
vel = 1 #Velocidad del jugador
FPS = 60 #Fotogramas por segundo que tendra el programa
ancho, alto = 800, 600 #Dimensiones de la ventana del juego


#PANTALLA
ventana = pygame.display.set_mode((ancho, alto+50))
pygame.display.set_caption("Laberinto del fauno") #NOMBRE DEL JUEGO

fondo = pygame.image.load("laberinto.svg") #Cargamos la imagen que representara al jugador
fondo = pygame.transform.rotate(pygame.transform.scale(fondo, (ancho, alto)), 180)

largo_jugador, alto_jugador = 20, 20 #Dimensiones del jugador
imagen_jugador = pygame.transform.scale(pygame.image.load("circulo.png"), (largo_jugador, alto_jugador))

main()

 #TIMER
stop = time.time() # Fin de timer
print("The time of the run:", stop - start) #Segundos transcurridos totales


# JUEGO GANADO

class AnimatedBackground(pygame.sprite.Sprite):
    def __init__(self, position, images, delay):
        super(AnimatedBackground, self).__init__()

        self.images = itertools.cycle(images)
        self.image = next(self.images)
        self.rect = pygame.Rect(position,  self.image.get_rect().size)

        self.animation_time = delay
        self.current_time = 0

    def update(self, dt):
        self.current_time += dt
        if self.current_time >= self.animation_time:
            self.current_time = 0
            self.image = next(self.images)
def load_images(path):
    images = [pygame.image.load(path + os.sep + background_frames).convert() for background_frames in sorted(os.listdir(path))]
    return images

def main():
    pygame.init()
    SIZE = WIDTH, HEIGHT = 250, 220
    BACKGROUND_COLOR = pygame.Color('black')
    FPS = 60
    screen = pygame.display.set_mode(SIZE)
    clock = pygame.time.Clock()

    imagen = load_images(path='anim')
    background = AnimatedBackground(position=(0, 0), images=imagen, delay = 0.50)
    all_sprites = pygame.sprite.Group(background)

    while True:
        dt = clock.tick(FPS) / 1000
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        all_sprites.update(dt)

        screen.fill(BACKGROUND_COLOR)
        screen.blit(background.image, background.rect)
        all_sprites.draw(screen)
        pygame.display.update()


if __name__ == '__main__':
    main()

#JUEGO PERDIDO

class AnimatedBackground(pygame.sprite.Sprite):
    def __init__(self, position, images, delay):
        super(AnimatedBackground, self).__init__()

        self.images = itertools.cycle(images)
        self.image = next(self.images)
        self.rect = pygame.Rect(position,  self.image.get_rect().size)

        self.animation_time = delay
        self.current_time = 0

    def update(self, dt):
        self.current_time += dt
        if self.current_time >= self.animation_time:
            self.current_time = 0
            self.image = next(self.images)
def load_images(path):
    images = [pygame.image.load(path + os.sep + background_frames).convert() for background_frames in sorted(os.listdir(path))]
    return images

def main():
    pygame.init()
    SIZE = WIDTH, HEIGHT = 500, 333
    BACKGROUND_COLOR = pygame.Color('black')
    FPS = 60
    screen = pygame.display.set_mode(SIZE)
    clock = pygame.time.Clock()

    imagen = load_images(path='anim3')
    background = AnimatedBackground(position=(0, 0), images=imagen, delay = 0.2 )
    all_sprites = pygame.sprite.Group(background)

    while True:
        dt = clock.tick(FPS) / 1000
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        all_sprites.update(dt)

        screen.fill(BACKGROUND_COLOR)
        screen.blit(background.image, background.rect)
        all_sprites.draw(screen)
        pygame.display.update()


if __name__ == '__main__':
    main()





