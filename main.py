import pygame

FPS = 200


class Game(pygame.sprite.Sprite):

    def __init__(self, group):
        super().__init__(group)
        self.image = pygame.image.load("data/gameover.png")
        self.rect = self.image.get_rect()


if __name__ == '__main__':
    pygame.init()
    pygame.display.set_caption('Game over')
    size = width, height = 600, 300
    screen = pygame.display.set_mode(size)
    running = True
    clock = pygame.time.Clock()
    all_sprites = pygame.sprite.Group()
    game = Game(all_sprites)
    game.rect.x = -width
    size_game = game.image.get_size()
    move_strange = True
    gif_yandex_par = 15
    pix = 1
    while running:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
        if game.rect.x == width - size_game[0] - gif_yandex_par:
            move_strange = False
        if move_strange:
            screen.fill((0, 0, 255))
            all_sprites.draw(screen)
            game.rect.x += pix
        pygame.display.flip()
    pygame.quit()
