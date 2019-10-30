import pygame


class Functions(object):
    def __init__(self, settings, screen, compass, place, form):
        self.settings = settings
        self.screen = screen
        self.compass = compass
        self.place = place
        self.form = form

    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                pos = pygame.mouse.get_pos()
                if self.form.flag:
                    for i in range(len(self.form.form_x)):
                        for j in range(len(self.form.form_y)):
                            if (self.form.form_x[i] < pos[0] < self.form.form_x[i] + self.settings.block_size and
                                    self.form.form_y[j] < pos[1] < self.form.form_y[j] + self.settings.block_size):
                                self.compass.compose[self.form.form_x[-1]][self.form.form_y[-1]] = self.form.sheet[j][i]
                                self.form.flag = False
                                return
                for i in range(len(self.place.place_x)):
                    for j in range(len(self.place.place_y)):
                        if (self.place.place_x[i] < pos[0] < self.place.place_x[i] + self.settings.block_size and
                                self.place.place_y[j] < pos[1] < self.place.place_y[j] + self.settings.block_size):
                            self.form.form_x.clear()
                            self.form.form_y.clear()
                            self.form.create_form(pos)
                            self.form.form_x.append(j)
                            self.form.form_y.append(i)
                            self.form.flag = True
                            return

    def draw_screen(self):
        self.screen.fill((0, 0, 0))
        self.place.draw_place()
        if self.form.flag:
            self.form.draw_select()
        pygame.display.flip()
