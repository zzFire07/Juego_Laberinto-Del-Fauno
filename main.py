import pygame
from player import Jugador
from game_functions import actualizar_pantalla, verificar_ganar, verificar_perder, actualizar_tiempo, reiniciar_tiempo
from ui import mostrar_mensaje
from config import ANCHO_VENTANA, ALTO_VENTANA, FPS, ROJO, AZULSITO
import time

pygame.init()
ventana = pygame.display.set_mode((ANCHO_VENTANA, ALTO_VENTANA + 50))
pygame.display.set_caption("Laberinto del fauno")

fondo = pygame.image.load("assets/laberinto.svg")
fondo = pygame.transform.rotate(pygame.transform.scale(fondo, (ANCHO_VENTANA, ALTO_VENTANA)), 180)

pasos_fuente = pygame.font.SysFont('comicsans', 40)
tiempo_fuente = pygame.font.SysFont('comicsans', 40)

def main():
    global CONTADOR_PASOS
    CONTADOR_PASOS = 0
    jugador = Jugador(ANCHO_VENTANA // 2 - 10, ALTO_VENTANA // 2 - 10)
    clock = pygame.time.Clock()
    run = True

    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        keys_pressed = pygame.key.get_pressed()
        jugador.acciones(keys_pressed, fondo)
        tiempo_transcurrido = actualizar_tiempo()
        actualizar_pantalla(ventana, fondo, jugador, pasos_fuente, tiempo_fuente)

        if verificar_ganar(jugador):
            if mostrar_mensaje(ventana, "¡YOU WIN!", AZULSITO):
                reiniciar_tiempo()
                main() # Reiniciar el juego si mostrar_mensaje devuelve True
            else:
                run = False # Si se cierra la ventana de perder
        elif verificar_perder(tiempo_transcurrido):
            if mostrar_mensaje(ventana, "¡YOU LOSE!", ROJO):
                reiniciar_tiempo()
                main() # Reiniciar el juego si mostrar_mensaje devuelve True
            else:
                run = False # Si se cierra la ventana de perder

    pygame.quit()

if __name__ == "__main__":
    main()