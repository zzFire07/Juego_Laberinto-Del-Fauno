import pygame
import sys
from config import BLANCO, AZUL, ROJO, ANCHO_VENTANA, ALTO_VENTANA

def mostrar_mensaje(ventana, mensaje, color):
    pygame.init()
    fuente = pygame.font.SysFont("Arial", 80)
    while True:
        ventana.fill(BLANCO)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif mensaje == "¡YOU LOSE!":
                if event.key == pygame.K_r:
                    return True  # Indica que se debe reiniciar el juego
        texto = fuente.render(mensaje, 0, (color))
        ventana.blit(texto, (ANCHO_VENTANA // 2 - texto.get_width() // 2, ALTO_VENTANA // 2 - texto.get_height() // 2))
        pygame.display.update()
        return False # Si no se presiona 'r' o no es la pantalla de derrota