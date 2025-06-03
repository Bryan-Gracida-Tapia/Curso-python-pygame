

from Configurations import Configurations
from pygame import sprite
import pygame
from random import randint

class Soldier:
    """
    Clase que contiene el fondo de pantalla.
    """

    def __init__(self):
        soldier_image_path=Configurations.get_soldier_image_path()
        self.image=pygame.image.load(soldier_image_path)

        soldier_size=Configurations.get_soldier_block_size()
        self.image = pygame.transform.scale(self.image,[soldier_size,soldier_size])

        self.rect=self.image.get_rect()


    def blit(self,screen:pygame.surface.Surface):
        """
        Se utiliza para dibujar el fondo de pantalla.
        :param screen:
        :return:
        """
        screen.blit(self.image,self.rect)


    def soldier_init(self,screen) -> None:
        screen_rect = screen.get_rect()
        self.rect.center = screen_rect.center
        self.rect.right = screen_rect.right
        """
        screen_width = Configurations.get_screen_size()[0]
        screen_height = Configurations.get_screen_size()[1]

        soldier_block_size = Configurations.get_soldier_block_size()
        self.rect.x = soldier_block_size * randint(0, (screen_width // soldier_block_size - 1))
        self.rect.y = soldier_block_size * randint(0, (screen_height // soldier_block_size - 1))
        """