import itertools
import os
import sys
import pygame

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