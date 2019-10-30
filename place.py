import pygame


class Place(object):
    def __init__(self, settings, screen, compass):
        self.settings = settings
        self.screen = screen
        self.compass = compass

        self.place_x = list()
        self.place_y = list()

        self.create_place()

    def create_place(self):
        center = self.screen.get_rect().center
        size = self.settings.block_size + self.settings.line_size
        for i in range(9):
            self.place_x.append(center[0] + (i - 4.5) * size + self.settings.line_size // 2 + 1)
            self.place_y.append(center[1] + (i - 4.5) * size + self.settings.line_size // 2 + 1)

    def draw_place(self):
        size = self.settings.block_size + self.settings.line_size
        for i in range(9):
            for j in range(9):
                pygame.draw.rect(self.screen, self.settings.compass_line_color,
                                 (self.place_x[i] - self.settings.line_size // 2 - 1,
                                  self.place_y[j] - self.settings.line_size // 2 - 1,
                                  size + 1, size + 1),
                                 self.settings.line_size)
                num_image = pygame.font.SysFont(None, 64).render(str(self.compass.compose[j][i]), True, (255, 255, 255))
                num_rect = num_image.get_rect()
                num_rect.center = (self.place_x[i] + self.settings.block_size // 2,
                                   self.place_y[j] + self.settings.block_size // 2)
                self.screen.blit(num_image, num_rect)
