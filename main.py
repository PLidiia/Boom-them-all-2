import random

import pygame

WIDTH_WINDOW = 500


class Bomb(pygame.sprite.Sprite):
    image = pygame.image.load("data/bomb.png")
    image_boom = pygame.image.load("data/boom.png")

    def __init__(self, group):
        super().__init__(group)
        self.image = Bomb.image
        self.rect = self.image.get_rect()
        while True:
            self.rect.topleft = (
                (random.randint(0, width - self.rect.width), random.randint(0, height - self.rect.height)))
            if len(pygame.sprite.spritecollide(self, group, False)) == 1:
                break

    def get_event(self, pos):
        if self.rect.collidepoint(pos):
            self.image = self.image_boom


if __name__ == '__main__':
    pygame.init()
    size = width, height = WIDTH_WINDOW, WIDTH_WINDOW
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption('Boom them all--2')
    group = pygame.sprite.Group()
    for _ in range(20):
        Bomb(group)
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                for bomb in group:
                    bomb.get_event(event.pos)
        group.update()
        screen.fill((255, 255, 255))
        group.draw(screen)
        pygame.display.flip()
