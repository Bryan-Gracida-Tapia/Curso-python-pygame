"""
Nombre del equipo: Átomos
Integrantes: Bryan Gracida Tapia, Addi Toro Chávez
fecha: 13 de mayo del 2025
"""
import pygame
from Configurations import Configurations

class TicTacToeMark(pygame.sprite.Sprite):
    """
    Clase que representa una marca en el tablero.
    Hereda de Sprite.
    """

    # Atributo de clase para manejar el turno del jugador
    _current_player = 'X'

    def __init__(self, cell_number: int):
        """
        Constructor que crea la marca según el turno actual
        y la posiciona en la casilla correspondiente.
        :param cell_number: número de la casilla (1a9)
        """
        super().__init__()
        self._cell_number = cell_number
        self._player = TicTacToeMark._current_player  # Para guardar al jugador

        # Determinar imagen según el turno actual
        if TicTacToeMark._current_player == 'X':
            image_path = Configurations.get_mark_o_path()
            TicTacToeMark._current_player = 'O'
        else:
            image_path = Configurations.get_mark_x_path()
            TicTacToeMark._current_player = 'X'

        self.image = pygame.image.load(image_path)
        self.image = pygame.transform.scale(self.image, Configurations.get_mark_size())

        self.rect = self.image.get_rect()

        # Posicionar marca en el lugar correcto
        self.rect.center = Configurations.get_cell_position(cell_number)

    def get_player(self):
        return self._player

    def get_cell_number(self) -> int:
        return self._cell_number

    @classmethod
    def get_current_player(cls) -> str:
        return cls._current_player