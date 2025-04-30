import pygame
import sys
from config import BLANCO, AZULSITO, ROJO, ANCHO_VENTANA, ALTO_VENTANA

def mostrar_mensaje(ventana, mensaje, color):
    fuente = pygame.font.SysFont("Arial", 80)

    while True:
        ventana.fill(BLANCO)
        texto = fuente.render(mensaje, 0, color)
        ventana.blit(texto, (ANCHO_VENTANA // 2 - texto.get_width() // 2, ALTO_VENTANA // 2 - texto.get_height() // 2))
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    return True  # Indica reiniciar en cualquier mensaje
        # Si no se presiona 'r' o se cierra la ventana, el bucle continúa