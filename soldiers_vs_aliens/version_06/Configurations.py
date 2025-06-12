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
    _shot_block_size = 60

    _frames_per_row = 4  # Número de frames que contiene cada fila de la hoja de frames.
    _frames_row = 2
    _soldier_frame_delay = 10  # Tiempo de cada frame del personaje (en ms).
    _soldier_speed = 12.5  # Velocidad (en píxeles) del personaje.

    #Media del juego
    _background_image_path= "../Media/fondo.jpg"
    _soldier_sheet_path = "../Media/soldier-idle_shooting_sheet.png"
    _shot_sheet_path = "../Media/shot-sheet.png"


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
    def get_shot_block_size(cls) -> int:
        """
        Getter para ._soldier_block_size
        :return:
        """
        return cls._shot_block_size

    """NUEVO."""
    @classmethod
    def get_frames_per_row(cls) -> int:
        """
        Getter para _soldier_frames_per_row.
        """
        return cls._frames_per_row

    @classmethod
    def get_frames_row(cls) -> int:
        """
        Getter para _soldier_frames_columns_row.
        """
        return cls._frames_row
    """NUEVO."""
    @classmethod
    def get_soldier_frame_delay(cls) -> int:
        """
        Getter para _soldier_frame_delay.
        """
        return cls._soldier_frame_delay

    """NUEVO."""
    @classmethod
    def get_soldier_speed(cls) -> float:
        """
        Getter para _soldier_speed.
        """
        return cls._soldier_speed

    @classmethod
    def get_background_image_path(cls)->str:
        """
        Getter para background_image_path.
        :return:
        """
        return cls._background_image_path

    @classmethod
    def get_soldier_sheet_path(cls) -> str:
        """
        Getter para _soldier_sheet_path.
        """
        return cls._soldier_sheet_path

    @classmethod
    def get_shot_sheet_path(cls) -> str:
        """
        Getter para _soldier_sheet_path.
        """
        return cls._shot_sheet_path