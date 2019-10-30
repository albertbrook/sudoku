import pygame
from functions import Functions
from settings import Settings
from compass import Compass
from place import Place
from form import Form


class Game(object):
    def __init__(self):
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode(self.settings.screen_size)
        self.compass = Compass()
        self.place = Place(self.settings, self.screen, self.compass)
        self.form = Form(self.settings, self.screen, self.compass)
        self.functions = Functions(self.settings, self.screen, self.compass, self.place, self.form)

    def start(self):
        while True:
            self.functions.check_events()
            self.functions.draw_screen()


if __name__ == '__main__':
    game = Game()
    game.start()
