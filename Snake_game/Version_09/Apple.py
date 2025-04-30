from itertools import repeat

import pygame
from random import randint
from pygame.sprite import Sprite
from Configuration import Configurations

class Apple(Sprite):
    # atrinbuto de clase para la puntuacion
    _no_apple = 0
    def __init__(self):
        super().__init__()
        Apple._no_apple += 1
        image_apple_path = Configurations.get_image_apple()
        self.image = pygame.image.load(image_apple_path)

        apple_size = Configurations.get_apple_size()
        self.image = pygame.transform.scale(self.image,(apple_size,apple_size))
        self.rect = self.image.get_rect()


    def blit(self, screen: pygame.surface.Surface):
        """
        Se utiliza para dibujar la pamtalla
        :param screen:Pantalla donde se dibuja
        """

        screen.blit(self.image,self.rect)

    def random_position(self, snake_body: pygame.sprite.Group) -> None:
        """
        Se utiliza para incializar una ubicacion aleatoria de la manzana y verificar que no se sobreponga sobre el cuerpo de la serpiente
        """
        repetir = True

        while repetir:
            # Se genra la posicion aleatoria
            screen_width = Configurations.get_screen_size()[0]
            screen_height = Configurations.get_screen_size()[1]
            apple_block_size = Configurations.get_snake_block_size()
            self.rect.x = apple_block_size * randint(0, (screen_width // apple_block_size - 1))
            self.rect.y = apple_block_size * randint(0, (screen_height // apple_block_size - 1))

            # Se verifica que no se encuentre sobre el cuerpo de la serpiente.
            for snake_block in snake_body.sprites():
                if self.rect == snake_block.rect:
                    repetir = True
                    break
                else: repetir = False

    @classmethod
    def get_no_apples(cls) -> int:
        """
        Geter para el numero de apples
        """
        return cls._no_apple
