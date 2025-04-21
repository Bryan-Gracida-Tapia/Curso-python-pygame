import pygame
from random import randint

from Configuration import Configurations
from pygame.sprite import  Sprite

class Snakeblock(Sprite): #(Sprite) es un concepto de herencia ya que es una clase que ya fue creada, sin embargo es generica y nos permite modificarlo
    """

    """

    def __init__(self,is_head : bool = False):
        """
        Constructor de la clase
        """
        super().__init__()

        if is_head:
            color = Configurations.get_snake_head_color()
        else:
            color = Configurations.get_snake_body_color()

        snake_block_size = Configurations.get_snake_block_size()
        self.image = pygame.Surface((snake_block_size,snake_block_size))
        self.image.fill(color)

        self.rect = self.image.get_rect()

    def blit(self, screen: pygame.surface.Surface):
        """
        Se utiliza para dibujar el bloque de la serpiente
        :param screen: pantalla donde se dibuja
        """

        screen.blit(self.image,self.rect)

    def snake_head_init(self)-> None:
        """
        Se genera una ubicación aleatoria de la cabeza de la serpiente
        :return:
        """
        screen_width = Configurations.get_screen_size()[0]
        screen_height = Configurations.get_screen_size()[1]

        snake_block_size = Configurations.get_snake_block_size()
        self.rect.x = snake_block_size * randint(0,(screen_width // snake_block_size -1))
        self.rect.y = snake_block_size * randint(0, (screen_height // snake_block_size -1))