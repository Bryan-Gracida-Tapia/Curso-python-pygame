"""
Nombre del equipo: Átomos
Integrantes: Bryan Gracida Tapia, Addi Toro Chávez
fecha: 13 de mayo del 2025
"""

import pygame
from Configurations import Configurations

class TicTacToeMark(pygame.sprite.Sprite):
    """
    Clase que representa una marca (X o O) en el tablero.

    """

    # Atributo de clase para manejar el turno del jugador
    turn = 'X'

    def __init__(self, number: int):
        """
        Constructor que crea la marca según el turno actual
        y la posiciona en la casilla correspondiente.
        :param number: celda elegida
        """
        super().__init__()

        # Determinar imagen según el turno actual
        if TicTacToeMark.turn == 'X':
            image_path = Configurations.get_markX_image()
            TicTacToeMark.turn = 'O'
        else:
            image_path = Configurations.get_markO_image()
            TicTacToeMark.turn = 'X'

        self.image = pygame.image.load(image_path)
        self.image = pygame.transform.scale(self.image, Configurations.get_mark_size())

        self.rect = self.image.get_rect()

        # Posicionar marca en el lugar correcto
        self.rect.center = Configurations.get_cell_position(number)