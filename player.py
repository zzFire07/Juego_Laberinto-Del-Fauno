import pygame
from config import VELOCIDAD_JUGADOR, LARGO_JUGADOR, ALTO_JUGADOR, resource_path

class Jugador(pygame.Rect):
    def __init__(self, x, y):
        super().__init__(x, y, LARGO_JUGADOR, ALTO_JUGADOR)
        self.imagen = pygame.transform.scale(pygame.image.load(resource_path("assets/characterr.png")), (LARGO_JUGADOR, ALTO_JUGADOR))
        self.pasos = 0  # El contador de pasos ahora es un atributo del jugador
        self.imagen_arriba = self.imagen  # Imagen original
        self.imagen_abajo = pygame.transform.flip(self.imagen, False, True)  # Voltea la imagen hacia abajo
        self.imagen_derecha = pygame.transform.rotate(self.imagen, -90)  # Voltea la imagen hacia la derecha 90 grados
        self.imagen_izquierda = pygame.transform.rotate(self.imagen, 90)  # Voltea la imagen hacia la izquierda -90 grados
        self.direccion = "arriba"  # Dirección inicial
        
        # Variables para el cooldown de pasos
        self.ultimo_paso = 0  # Tiempo del último incremento de pasos
        self.paso_cooldown = 188  # Cooldown en milisegundos (0.188 segundos)

    def acciones(self, keys_pressed, fondo):
        moved = False

        if (keys_pressed[pygame.K_a] or keys_pressed[pygame.K_LEFT]):
            self.imagen = self.imagen_izquierda  # Voltea la imagen a la izquierda
            self.direccion = "izquierda"  # Actualiza la dirección
            for i in range(1, VELOCIDAD_JUGADOR):
                if self.collide_left(fondo):
                    break
                else:
                    self.x -= 1
                    moved = True
        if (keys_pressed[pygame.K_d] or keys_pressed[pygame.K_RIGHT]):
            self.imagen = self.imagen_derecha  # Voltea la imagen a la derecha
            self.direccion = "derecha"  # Actualiza la dirección
            for i in range(1, VELOCIDAD_JUGADOR):
                if self.collide_right(fondo):
                    break
                else:
                    self.x += 1
                    moved = True
        if (keys_pressed[pygame.K_w] or keys_pressed[pygame.K_UP]):
            self.imagen = self.imagen_arriba
            self.direccion = "arriba"
            for i in range(1, VELOCIDAD_JUGADOR):
                if self.collide_up(fondo):
                    break
                else:
                    self.y -= 1
                    moved = True
        if (keys_pressed[pygame.K_s] or keys_pressed[pygame.K_DOWN]):
            self.imagen = self.imagen_abajo
            self.direccion = "abajo"
            for i in range(1, VELOCIDAD_JUGADOR):
                if self.collide_down(fondo):
                    break
                else:
                    self.y += 1
                    moved = True

        # Verificar si se movió y si ha pasado suficiente tiempo desde el último paso
        tiempo_actual = pygame.time.get_ticks()
        if moved and (tiempo_actual - self.ultimo_paso >= self.paso_cooldown):
            self.pasos += 1  # Incrementa el contador de pasos
            self.ultimo_paso = tiempo_actual  # Actualiza el tiempo del último paso

    def collide_down(self, superficie):
        for i in range(1, self.width):
            if superficie.get_at((self.x + i, self.y + self.height)) == (0, 0, 0, 255):
                return True
        return False

    def collide_up(self, superficie):
        for i in range(1, self.width):
            if superficie.get_at((self.x + i, self.y)) == (0, 0, 0, 255):
                return True
        return False

    def collide_right(self, superficie):
        for i in range(1, self.height):
            if superficie.get_at((self.x + self.width, self.y + i)) == (0, 0, 0, 255):
                return True
        return False

    def collide_left(self, superficie):
        for i in range(1, self.height):
            if superficie.get_at((self.x, self.y + i)) == (0, 0, 0, 255):
                return True
        return False

    def dibujar(self, ventana):
        ventana.blit(self.imagen, (self.x, self.y))