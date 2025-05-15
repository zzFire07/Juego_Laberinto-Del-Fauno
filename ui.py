import pygame
import sys
from config import ANCHO_VENTANA, ALTO_VENTANA, BLANCO, AZULSITO, ROJO, ROJO_OSCURO, NEGRO, MARRON_TOSTADO, ARENA_PALIDA, GRIS_ROCA, GRIS_OSCURO

class Boton:
    def __init__(self, x, y, ancho, alto, texto, color, color_hover):
        self.rect = pygame.Rect(x, y, ancho, alto)
        self.color = color
        self.color_hover = color_hover
        self.texto = texto
        self.fuente = pygame.font.SysFont('Arial', 40)
        self.activo = False
    
    def dibujar(self, ventana):
        # Determinar color basado en si el mouse está sobre el botón
        color_actual = self.color_hover if self.activo else self.color
        
        # Dibujar el rectángulo del botón
        pygame.draw.rect(ventana, color_actual, self.rect, border_radius=10)
        pygame.draw.rect(ventana, BLANCO, self.rect, 3, border_radius=10)  # Borde del botón
        
        # Dibujar el texto del botón
        texto_renderizado = self.fuente.render(self.texto, True, BLANCO)
        ventana.blit(texto_renderizado, 
                     (self.rect.centerx - texto_renderizado.get_width() // 2, 
                      self.rect.centery - texto_renderizado.get_height() // 2))
    
    def esta_sobre(self, pos):
        self.activo = self.rect.collidepoint(pos)
        return self.activo

def mostrar_finjuego(ventana, mensaje, color):
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
                if event.key == pygame.K_ESCAPE:
                    return True
                elif event.key == pygame.K_r:
                    return False  # Indica reiniciar en cualquier mensaje
        # Si no se presiona 'r' o se cierra la ventana, el bucle continúa

def mostrar_menu_principal(ventana):
    # Configuración de los botones
    boton_jugar = Boton(ANCHO_VENTANA // 2 - 150, ALTO_VENTANA // 2 - 100, 
                         300, 70, "Entrar", MARRON_TOSTADO, GRIS_ROCA)
    
    boton_configuracion = Boton(ANCHO_VENTANA // 2 - 150, ALTO_VENTANA // 2, 
                               300, 70, "Configuración", MARRON_TOSTADO, GRIS_ROCA)
    
    boton_salir = Boton(ANCHO_VENTANA // 2 - 150, ALTO_VENTANA // 2 + 100, 
                         300, 70, "Cerrar juego", ROJO, ROJO_OSCURO)
    
    # Fondo del menú (puedes usar una imagen si prefieres)
    fondo_menu = pygame.Surface((ANCHO_VENTANA, ALTO_VENTANA + 50))
    fondo_menu.fill(ARENA_PALIDA)  # Color de fondo oscuro
    
    # Título del juego
    fuente_titulo = pygame.font.SysFont('Comicsans', 70, bold=True)
    texto_titulo = fuente_titulo.render("Laberinto del Fauno", True, MARRON_TOSTADO)
    
    # Loop del menú
    ejecutando_menu = True
    clock = pygame.time.Clock()
    
    while ejecutando_menu:
        clock.tick(60)
        pos_mouse = pygame.mouse.get_pos()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return "salir"
            
            # Verificar si el mouse está sobre los botones
            boton_jugar.esta_sobre(pos_mouse)
            boton_configuracion.esta_sobre(pos_mouse)
            boton_salir.esta_sobre(pos_mouse)
            
            # Verificar clics en los botones
            if event.type == pygame.MOUSEBUTTONDOWN:
                if boton_jugar.activo:
                    return "jugar"
                elif boton_configuracion.activo:
                    return "configuracion"
                elif boton_salir.activo:
                    return "salir"
        
        # Dibujar el menú
        ventana.blit(fondo_menu, (0, 0))
        ventana.blit(texto_titulo, (ANCHO_VENTANA // 2 - texto_titulo.get_width() // 2, 80))
        
        # Dibujar botones
        boton_jugar.dibujar(ventana)
        boton_configuracion.dibujar(ventana)
        boton_salir.dibujar(ventana)
        
        pygame.display.update()
    
    return "salir"  # Por defecto

def mostrar_configuracion(ventana):
    # Configuración de los botones
    boton_volver = Boton(ANCHO_VENTANA // 2 - 150, ALTO_VENTANA - 100, 
                          300, 70, "Volver", AZULSITO, (0, 0, 150))
    
    # Fondo de la pantalla de configuración
    fondo_config = pygame.Surface((ANCHO_VENTANA, ALTO_VENTANA + 50))
    fondo_config.fill(GRIS_ROCA)
    
    # Título de la configuración
    fuente_titulo = pygame.font.SysFont('Arial', 70, bold=True)
    texto_titulo = fuente_titulo.render("Configuración", True, BLANCO)
    
    # Opciones de configuración (ejemplos)
    fuente_opciones = pygame.font.SysFont('Arial', 40)
    texto_opciones = [
        fuente_opciones.render("Pantalla: Completa / Ventana", True, BLANCO),
        fuente_opciones.render("Dificultad: Fácil / Normal / Difícil", True, BLANCO),
        fuente_opciones.render("Música: Activada / Desactivada", True, BLANCO)
    ]
    
    # Loop de la pantalla de configuración
    ejecutando_config = True
    clock = pygame.time.Clock()
    
    while ejecutando_config:
        clock.tick(60)
        pos_mouse = pygame.mouse.get_pos()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return "salir"
            
            # Verificar si el mouse está sobre el botón volver
            boton_volver.esta_sobre(pos_mouse)
            
            # Verificar clics en los botones
            if event.type == pygame.MOUSEBUTTONDOWN:
                if boton_volver.activo:
                    return "menu"
        
        # Dibujar la configuración
        ventana.blit(fondo_config, (0, 0))
        ventana.blit(texto_titulo, (ANCHO_VENTANA // 2 - texto_titulo.get_width() // 2, 80))
        
        # Dibujar opciones
        for i, texto in enumerate(texto_opciones):
            ventana.blit(texto, (ANCHO_VENTANA // 2 - texto.get_width() // 2, 200 + i * 80))
        
        # Dibujar botón de volver
        boton_volver.dibujar(ventana)
        
        pygame.display.update()
    
    return "menu"  # Por defecto

def mostrar_menu_pausa(ventana):
    # Crear una superficie semitransparente para oscurecer el juego
    superficie_pausa = pygame.Surface((ANCHO_VENTANA, ALTO_VENTANA + 50), pygame.SRCALPHA)
    superficie_pausa.fill(GRIS_OSCURO)  # Negro semitransparente
    
    # Configuración de los botones
    boton_continuar = Boton(ANCHO_VENTANA // 2 - 150, ALTO_VENTANA // 2 - 100, 
                         300, 70, "Continuar", MARRON_TOSTADO, GRIS_ROCA)
    
    boton_menu = Boton(ANCHO_VENTANA // 2 - 150, ALTO_VENTANA // 2, 
                       300, 70, "Menú Principal", MARRON_TOSTADO, GRIS_ROCA)
    
    boton_salir = Boton(ANCHO_VENTANA // 2 - 150, ALTO_VENTANA // 2 + 100, 
                         300, 70, "Salir del Juego", ROJO, ROJO_OSCURO)
    
    # Título del menú de pausa
    fuente_titulo = pygame.font.SysFont('Arial', 70, bold=True)
    texto_titulo = fuente_titulo.render("PAUSA", True, BLANCO)
    
    # Loop del menú de pausa
    ejecutando_pausa = True
    clock = pygame.time.Clock()
    
    while ejecutando_pausa:
        clock.tick(60)
        pos_mouse = pygame.mouse.get_pos()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return "salir"
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return "continuar"  # Volver al juego al presionar ESC nuevamente
            
            # Verificar si el mouse está sobre los botones
            boton_continuar.esta_sobre(pos_mouse)
            boton_menu.esta_sobre(pos_mouse)
            boton_salir.esta_sobre(pos_mouse)
            
            # Verificar clics en los botones
            if event.type == pygame.MOUSEBUTTONDOWN:
                if boton_continuar.activo:
                    return "continuar"
                elif boton_menu.activo:
                    return "menu"
                elif boton_salir.activo:
                    return "salir"
        
        # Dibujar el menú de pausa encima del juego
        ventana.blit(superficie_pausa, (0, 0))
        ventana.blit(texto_titulo, (ANCHO_VENTANA // 2 - texto_titulo.get_width() // 2, 80))
        
        # Dibujar botones
        boton_continuar.dibujar(ventana)
        boton_menu.dibujar(ventana)
        boton_salir.dibujar(ventana)
        
        pygame.display.update()
    
    return "continuar"  # Por defecto

