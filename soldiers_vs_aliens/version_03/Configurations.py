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
    _game_title = "Soldairs vs Aliens"   #Título del juego
    _fps = 8
    _soldier_block_size = 80

    #Media del juego
    _background_image_path= "../Media/fondo.jpg"
    _soldier_image_path = "../Media/soldier.jpg"


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
    def get_fps(cls) -> int:
        """
        Getter para background.
        :return:
        """
        return cls._fps

    @classmethod
    def get_soldier_block_size(cls) -> int:
        """
        Getter para ._soldier_block_size
        :return:
        """
        return cls._soldier_block_size

    @classmethod
    def get_background_image_path(cls)->str:
        """
        Getter para background_image_path.
        :return:
        """
        return cls._background_image_path

    @classmethod
    def get_soldier_image_path(cls)->str:
        """
        Getter para background_image_path.
        :return:
        """
        return cls._soldier_image_path