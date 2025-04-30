import pygame
from config import VELOCIDAD_JUGADOR, LARGO_JUGADOR, ALTO_JUGADOR

class Jugador(pygame.Rect):
    def __init__(self, x, y):
        super().__init__(x, y, LARGO_JUGADOR, ALTO_JUGADOR)
        self.imagen = pygame.transform.scale(pygame.image.load("assets/circ_rojo.png"), (LARGO_JUGADOR, ALTO_JUGADOR))
        self.pasos = 0  # El contador de pasos ahora es un atributo del jugador

    def acciones(self, keys_pressed, fondo):
        moved = False

        if (keys_pressed[pygame.K_a] or keys_pressed[pygame.K_LEFT]):
            for i in range(1, VELOCIDAD_JUGADOR):
                if self.collide_left(fondo):
                    break
                else:
                    self.x -= 1
            moved = True
        if (keys_pressed[pygame.K_d] or keys_pressed[pygame.K_RIGHT]):
            for i in range(1, VELOCIDAD_JUGADOR):
                if self.collide_right(fondo):
                    break
                else:
                    self.x += 1
            moved = True
        if (keys_pressed[pygame.K_w] or keys_pressed[pygame.K_UP]):
            for i in range(1, VELOCIDAD_JUGADOR):
                if self.collide_up(fondo):
                    break
                else:
                    self.y -= 1
            moved = True
        if (keys_pressed[pygame.K_s] or keys_pressed[pygame.K_DOWN]):
            for i in range(1, VELOCIDAD_JUGADOR):
                if self.collide_down(fondo):
                    break
                else:
                    self.y += 1
            moved = True

        if moved:
            self.pasos += 1 # Incrementa el contador de pasos del jugador

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