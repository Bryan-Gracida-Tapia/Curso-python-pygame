"""
Nombre del equipo: Átomos
Integrantes: Bryan Gracida Tapia, Addi Toro Chávez
fecha: 13 de mayo del 2025
"""
import pygame


class Configurations:
    """
    Clase que contiene todas las configuraciones del juego.
    """
    #Configuraciones de la pantalla
    _screen_size = (1280, 720)  # Resolución de la pantalla (ancho,alto)
    _game_title = "Juego del gato"   #Título del juego
    _background = (50, 50, 50)  # Fondo de la pantalla en formato RGB
    _fps = 12

    _game_over_screen_time = 3
    _game_over_time = 500
    _scale_image = (400, 400)
    _scale_image2 = (400, 100)
    _center = (640, 360)
    _center2 = (600, 600)
    _center_turn = (450,50)
    #Media del juego
    _background_image_path= "../Media/media_juego_gato/background_image.png"
    _mark_x_path = "../Media/media_juego_gato/markX.png"
    _mark_o_path = "../Media/media_juego_gato/markO.png"

    # Marcadores de jugadores
    _mark_x_turn_path = "../Media/media_juego_gato/turnX.png"
    _mark_o_turn_path = "../Media/media_juego_gato/turnO.png"

    _mark_win_x_path = "../Media/media_juego_gato/winO.png"
    _mark_win_o_path = "../Media/media_juego_gato/winX.png"
    _mark_draw_path = "../Media/media_juego_gato/draw.png"
    _credits_image_path = "../Media/media_juego_gato/draw2.png"

    _mark_size = (100, 100)
    _mark_turn_image_size = (400, 200)

    # Configuraciones de la música del juego.
    _music_volume = 0.25  # Volumen de la música de fondo (valor entre 0 y 1).
    _music_fadeout_time = _game_over_screen_time * 1000  # Duración del desvanecimiento de la música (en ms).

    # Ruta de los audios del juego
    _music_path = "../Media/media_juego_gato/music.mp3"
    _keyboard_sound_path = "../Media/media_juego_gato/keyboard_sound.mp3"
    _game_over_sound_path = "../Media/media_juego_gato/results_sound.mp3"

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
    def get_time_over(cls) -> int:
        """
        Getter para _game_over_time.
        :return:
        """
        return cls._game_over_time

    @classmethod
    def get_scale_image(cls) -> tuple[int, int]:
        """
        Getter para _scale_image
        :return:
        """
        return cls._scale_image

    @classmethod
    def get_scale_image2(cls) -> tuple[int, int]:
        """
        Getter para _scale_image2
        :return:
        """
        return cls._scale_image2

    @classmethod
    def get_center(cls) -> tuple[int, int]:
        """
        Getter para _center.
        :return:
        """
        return cls._center

    @classmethod
    def get_center2(cls) -> tuple[int, int]:
        """
        Getter para _center2.
        :return:
        """
        return cls._center2

    @classmethod
    def get_center_turn(cls) -> tuple[int, int]:
        """
        Getter para _center2.
        :return:
        """
        return cls._center_turn

    @classmethod
    def get_background_image_path(cls)->str:
        """
        Getter para background_image_path.
        :return:
        """
        return cls._background_image_path

    @classmethod
    def get_mark_size(cls) -> tuple:
        """
        Getter para _mark_size.
        :return:
        """
        return cls._mark_size

    @classmethod
    def get_mark_turn_image_size(cls) -> tuple[int, int]:
        """Getter para _mark_turn_image_size"""
        return cls._mark_turn_image_size

    @classmethod
    def get_cell_position(cls, cell_number: int) -> tuple[int, int]:
        """
        Getter para la posición de una celda específica.
        :param cell_number: número de la casilla (1 a 9)
        :return: tupla con coordenadas (x, y)
        """
        return cls._cell_positions.get(cell_number, (0, 0))

    @classmethod
    def get_mark_x_path(cls) -> str:
        return cls._mark_x_path

    @classmethod
    def get_mark_o_path(cls) -> str:
        return cls._mark_o_path

    @classmethod
    def get_mark_x_turn(cls) -> str:
        return cls._mark_x_turn_path

    @classmethod
    def get_mark_o_turn(cls) -> str:
        return cls._mark_o_turn_path

    @classmethod
    def get_win_x_path(cls):
        return cls._mark_win_x_path

    @classmethod
    def get_win_o_path(cls):
        return cls._mark_win_o_path

    @classmethod
    def get_draw_path(cls):
        return cls._mark_draw_path

    @classmethod
    def get_credits_image_path(cls):
        return cls._credits_image_path

    @classmethod
    def get_music_volume(cls) -> float:
        """
        Getter para _music_volume.
        """
        return cls._music_volume

    @classmethod
    def get_music_fadeout_time(cls) -> int:
        """
        Getter para _music_fadeout_time.
        """
        return cls._music_fadeout_time

    @classmethod
    def get_music_path(cls) -> str:
        """
        Getter para _music_path.
        """
        return cls._music_path

    @classmethod
    def get_keyboard_sound_path(cls) -> str:
        """
        Getter para _keyboard_sound_path.
        """
        return cls._keyboard_sound_path

    @classmethod
    def get_game_over_sound_path(cls) -> str:
        """
        Getter para _game_over_sound_path.
        """
        return cls._game_over_sound_path


class ResultsImage:
    def __init__(self, result: str):
        if result == 'X':
            path = Configurations.get_win_x_path()
        elif result == 'O':
            path = Configurations.get_win_o_path()
        else:
            path = Configurations.get_draw_path()

        self.image = pygame.image.load(path)
        self.image = pygame.transform.scale(self.image, Configurations.get_scale_image())
        self.rect = self.image.get_rect()
        self.rect.center = Configurations.get_center()