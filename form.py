import pygame


class Form(object):
    def __init__(self, settings, screen, compass):
        self.settings = settings
        self.screen = screen
        self.compass = compass

        self.sheet = [[i * 3 + j + 1 for j in range(3)] for i in range(3)]
        self.form_x = list()
        self.form_y = list()
        self.flag = False

    def create_form(self, pos):
        size = self.settings.block_size + self.settings.line_size
        for i in range(3):
            self.form_x.append(pos[0] + (i - 1.5) * size + self.settings.line_size // 2 + 1)
            self.form_y.append(pos[1] + (i - 1.5) * size + self.settings.line_size // 2 + 1)

    def draw_select(self):
        size = self.settings.block_size + self.settings.line_size
        for i in range(3):
            for j in range(3):
                pygame.draw.rect(self.screen, self.settings.select_line_color,
                                 (self.form_x[i] - self.settings.line_size // 2 - 1,
                                  self.form_y[j] - self.settings.line_size // 2 - 1,
                                  size + 1, size + 1), self.settings.line_size)
                pygame.draw.rect(self.screen, (0, 255, 0),
                                 (self.form_x[i], self.form_y[j],
                                  self.settings.block_size, self.settings.block_size))
                num_image = pygame.font.SysFont(None, 64).render(str(self.sheet[j][i]), True, (0, 0, 255))
                num_rect = num_image.get_rect()
                num_rect.center = (self.form_x[i] + self.settings.block_size / 2,
                                   self.form_y[j] + self.settings.block_size / 2)
                self.screen.blit(num_image, num_rect)
