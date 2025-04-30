import pygame
import time
from config import BLANCO, ROJO, AZULSITO, ANCHO_VENTANA, ALTO_VENTANA, TIEMPO_LIMITE

TIEMPO_INICIO = time.time()

def actualizar_tiempo():
    tiempo_actual = time.time()
    return tiempo_actual - TIEMPO_INICIO

def verificar_ganar(jugador):
    return jugador.y > ALTO_VENTANA - jugador.height - 4

def verificar_perder(tiempo_transcurrido):
    return tiempo_transcurrido > TIEMPO_LIMITE

def actualizar_pantalla(ventana, fondo, jugador, pasos_fuente, tiempo_fuente):
    ventana.fill(BLANCO)
    ventana.blit(fondo, (0, 0))
    jugador.dibujar(ventana)
    texto_pasos = pasos_fuente.render("Pasos: " + str(jugador.pasos), 1, ROJO) # Usa el atributo del jugador
    texto_tiempo = tiempo_fuente.render("Tiempo: " + str(int(actualizar_tiempo())), 1, ROJO)
    ventana.blit(texto_pasos, (ANCHO_VENTANA - texto_pasos.get_width() - 10, ALTO_VENTANA - 10))
    ventana.blit(texto_tiempo, (10, ALTO_VENTANA - 10))
    pygame.display.update()