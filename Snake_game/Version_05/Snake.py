import pygame
from random import randint

from Configuration import Configurations
from pygame.sprite import  Sprite

class Snakeblock(Sprite): #(Sprite) es un concepto de herencia ya que es una clase que ya fue creada, sin embargo es generica y nos permite modificarlo
    """

    """
    # Atributos de clase (banderas de movimiento de juego)
    _is_moving_right = False
    _is_moving_letf = False
    _is_moving_up = False
    _is_moving_down = False

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

    # ///////////////////////////////////////////////////////////////////////////
    @classmethod
    def get_is_moving_right(cls)-> bool:
        """
        Getter para _is_moving_right
        """
        return cls._is_moving_right

    @classmethod
    def set_is_moving_right(cls,value: bool):
        """
        Setter para la bandera is_moving_right
        """
        cls._is_moving_right = value

    #////////////////////////////////////////
    @classmethod
    def get_is_moving_letf(cls)-> bool:
        """
        Getter para _is_moving_letf
        """
        return cls._is_moving_letf

    @classmethod
    def set_is_moving_letf(cls,value: bool):
        """
        Setter para la bandera is_moving_letf
        """
        cls._is_moving_letf = value

    #////////////////////////////////////////
    @classmethod
    def get_is_moving_up(cls)-> bool:
        """
        Getter para _is_moving_up
        """
        return cls._is_moving_up

    @classmethod
    def set_is_moving_up(cls,value: bool):
        """
        Setter para la bandera is_moving_up
        """
        cls._is_moving_up = value

    #////////////////////////////////////////
    @classmethod
    def get_is_moving_down(cls)-> bool:
        """
        Getter para _is_moving_down
        """
        return cls._is_moving_down

    @classmethod
    def set_is_moving_down(cls,value: bool):
        """
        Setter para la bandera is_moving_down
        """
        cls._is_moving_down = value