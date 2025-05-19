"""
Nombre del equipo: Átomos
Integrantes: Bryan Gracida Tapia, Addi Toro Chávez
fecha: 13 de mayo del 2025
"""
class Configurations:
    """
    Clase que contiene todas las configuraciones del juego.
    """
    #Configuraciones de la pantalla
    _screen_size = (1280, 720)  # Resolución de la pantalla (ancho,alto)
    _game_title = "Juego del gato"   #Título del juego
    _background = (50, 50, 50)  # Fondo de la pantalla en formato RGB
    _fps = 8

    #Media del juego
    _background_image_path= "../Media/media_juego_gato/background_image.png"
    _markO = "../Media/media_juego_gato/markO.png"
    _markX = "../Media/media_juego_gato/markX.png"

    _mark_size = (100, 100)
    # Agregando las celdas.
    _cell_positions = {
        1: (500, 310),
        2: (640, 310),
        3: (775, 310),

        4: (500, 450),
        5: (640, 450),
        6: (775, 450),

        7: (500, 570),
        8: (640, 570),
        9: (775, 570)
    }

    @classmethod
    def get_screen_size(cls)->tuple[int,int]:
        """
        Getter para screen_size.
        :return:
        """
        return  cls._screen_size

    @classmethod
    def get_game_title(cls)->str:
        """
        Getter para _game_title.
        :return:
        """
        return  cls._game_title

    @classmethod
    def get_background(cls)->tuple[int,int,int]:
        """
        Getter para background.
        :return:
        """
        return  cls._background

    @classmethod
    def get_fps(cls) -> int:
        """
        Getter para background.
        :return:
        """
        return cls._fps

    @classmethod
    def get_background_image_path(cls)->str:
        """
        Getter para background_image_path.
        :return:
        """
        return cls._background_image_path

    @classmethod
    def get_markO_image(cls) -> str:
        """
        Getter para _markO.
        :return:
        """
        return cls._markO

    @classmethod
    def get_markX_image(cls) -> str:
        """
        Getter para _markX.
        :return:
        """
        return cls._markX

    @classmethod
    def get_mark_size(cls) -> tuple:
        """
        Getter para _mark_size.
        :return:
        """
        return cls._mark_size

    @classmethod
    def get_cell_position(cls, cell_number: int) -> tuple[int, int]:
        """
        Getter para la posición de una celda específica.
        :param cell_number: número de la casilla (1 a 9)
        :return: tupla con coordenadas (x, y)
        """
        return cls._cell_positions.get(cell_number, (0, 0))