import pygame
from Configuration import Configurations


class Background:
    """
        Clase que contiene el fondo de la pantalla
    """

    def __init__(self):
        background_image_path = Configurations.get_image_background()
        self.image = pygame.image.load(background_image_path)

        # Se restaura la escala del tamaÑo de la pantalla
        screen_size = Configurations.get_screen_size()
        self.image = pygame.transform.scale(self.image,screen_size)
        self.rec = self.image.get_rect()

    def blit(self, screen: pygame.surface.Surface):
        screen.blit(self.image,self.rec)
