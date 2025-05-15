import pygame
import time
from config import BLANCO, ROJO, AZULSITO, ANCHO_VENTANA, ALTO_VENTANA, TIEMPO_LIMITE
from ui import mostrar_finjuego, mostrar_menu_principal, mostrar_configuracion, mostrar_menu_pausa

global tiempo_inicio
tiempo_inicio = time.time()



def actualizar_tiempo():
    tiempo_actual = time.time()
    return tiempo_actual - tiempo_inicio

def reiniciar_tiempo():
    global tiempo_inicio
    tiempo_inicio = time.time()

def verificar_ganar(jugador):
    return jugador.y > ALTO_VENTANA - jugador.height - 4

def verificar_perder(tiempo_transcurrido):
    return tiempo_transcurrido > TIEMPO_LIMITE

def actualizar_pantalla(ventana, fondo, jugador, pasos_fuente, tiempo_fuente, tiempo_mostrar=None):
    ventana.fill(BLANCO)
    ventana.blit(fondo, (0, 0))
    jugador.dibujar(ventana)
    texto_pasos = pasos_fuente.render("Pasos: " + str(jugador.pasos), 1, ROJO) # Usa el atributo del jugador
    
    # Si se proporciona un tiempo específico, usarlo; de lo contrario, usar el tiempo actual
    if tiempo_mostrar is None:
        tiempo_mostrar = actualizar_tiempo()
        
    texto_tiempo = tiempo_fuente.render("Tiempo: " + str(int(tiempo_mostrar)), 1, ROJO)
    ventana.blit(texto_pasos, (ANCHO_VENTANA - texto_pasos.get_width() - 10, ALTO_VENTANA - 10))
    ventana.blit(texto_tiempo, (10, ALTO_VENTANA - 10))
    pygame.display.update()