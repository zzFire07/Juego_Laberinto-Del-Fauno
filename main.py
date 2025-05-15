import pygame
from player import Jugador
from game_functions import actualizar_pantalla, verificar_ganar, verificar_perder, actualizar_tiempo, reiniciar_tiempo
from ui import mostrar_finjuego, mostrar_menu_principal, mostrar_configuracion
from config import ANCHO_VENTANA, ALTO_VENTANA, FPS, ROJO, AZULSITO
import time

pygame.init()
ventana = pygame.display.set_mode((ANCHO_VENTANA, ALTO_VENTANA + 50))
pygame.display.set_caption("Laberinto del fauno")

fondo = pygame.image.load("assets/laberinto.svg")
fondo = pygame.transform.rotate(pygame.transform.scale(fondo, (ALTO_VENTANA, ALTO_VENTANA)), 180)

pasos_fuente = pygame.font.SysFont('comicsans', 40)
tiempo_fuente = pygame.font.SysFont('comicsans', 40)

def juego():
    jugador = Jugador(ANCHO_VENTANA // 2 - 10, ALTO_VENTANA // 2 - 10)
    clock = pygame.time.Clock()
    run = True
    reiniciar_tiempo()  # Reiniciar el tiempo al comenzar una nueva partida
    tiempo_acumulado = 0  # Para mantener registro del tiempo durante pausas
    
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return "salir"
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    # Guardar tiempo antes de la pausa
                    tiempo_antes_pausa = actualizar_tiempo()
                    
                    # Mostrar menú de pausa
                    from ui import mostrar_menu_pausa  # Importación local para evitar circular imports
                    resultado_pausa = mostrar_menu_pausa(ventana)
                    
                    if resultado_pausa == "continuar":
                        # Acumular el tiempo previo a la pausa
                        tiempo_acumulado += tiempo_antes_pausa
                        # Reiniciar el tiempo desde este punto
                        reiniciar_tiempo()
                    else:
                        return resultado_pausa  # menu o salir

        keys_pressed = pygame.key.get_pressed()
        jugador.acciones(keys_pressed, fondo)
        
        # Calcular tiempo total: tiempo actual + tiempo acumulado de pausas anteriores
        tiempo_transcurrido = actualizar_tiempo() + tiempo_acumulado
        
        # Pasar el tiempo total a la función de actualización
        actualizar_pantalla(ventana, fondo, jugador, pasos_fuente, tiempo_fuente, tiempo_transcurrido)

        if verificar_ganar(jugador):
            if mostrar_finjuego(ventana, "¡YOU WIN!", AZULSITO):
                reiniciar_tiempo()
                return "menu"  # Ir al menú si mostrar_mensaje devuelve True
            else:
                return "jugar" # Reiniciar el juego si mostrar_mensaje devuelve False
        elif verificar_perder(tiempo_transcurrido):
            if mostrar_finjuego(ventana, "¡YOU LOSE!", ROJO):
                reiniciar_tiempo()
                return "menu"  # Ir al menú si mostrar_mensaje devuelve True
            else:
                return "jugar" # Reiniciar el juego si mostrar_mensaje devuelve False

    return "menu"

def main():
    estado = "menu"
    
    while estado != "salir":
        if estado == "menu":
            estado = mostrar_menu_principal(ventana)
        elif estado == "jugar":
            estado = juego()
        elif estado == "configuracion":
            estado = mostrar_configuracion(ventana)
    
    pygame.quit()

if __name__ == "__main__":
    main()