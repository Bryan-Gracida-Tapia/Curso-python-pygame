class Configurations:
    """
    Clase que contiene todas las configuraciones del juego.
    """
    # Configuraciones de la pantalla.
    _game_title = "Snake game"            # Título de la ventana.
    _screen_size = (1280, 720)                      # Resolución de la pantalla (ancho, alto).
    #_background = (20, 30, 50)                      # Fondo de la pantalla en formato RGB.
    _fps = 10                                       # Número máximo de FPS del videojuego.

    # Tiempo de espera en cierre de juego.
    _time_game_over = 5

    # Configuraciones de la serpiente.
    _snake_block_size = 40                        # Tamaño del bloque. Es muy recomendable que sea
                                                    # divisor común del largo y ancho de _screen_size.
    _snake_head_color = (255, 255, 255)             # Color de la cabeza de la serpiente.
    _snake_body_color = (162, 208, 194)                 # Color del cuerpo de la serpiente.

    # Configuraciones de la manzana.
    _apple_color = (255,0,0)
    _apple_size = _snake_block_size
    _time_to_refresh = 200

    # media del juego.
    _background_image_path = "../Media/fondo.jpg"

    _image_apple_path = ["../Media/media snake_game/apple1.png","../Media/media snake_game/apple2.png",
                         "../Media/media snake_game/apple3.png","../Media/media snake_game/apple4.png"]

    _image_snake_path_head = ["../Media/media snake_game/head1.png","../Media/media snake_game/head2.png",
                         "../Media/media snake_game/head3.png","../Media/media snake_game/head4.png",
                         "../Media/media snake_game/head5.png","../Media/media snake_game/head6.png",
                         "../Media/media snake_game/head7.png","../Media/media snake_game/head8.png"]

    _image_snake_path_body = ["../Media/body1.png","../Media/body2.png","../Media/body3.png"]

    # Configuraciones de la música del juego.
    _music_volume = 0.25  # Volumen de la música de fondo (valor entre 0 y 1).
    _music_fadeout_time = _time_game_over * 1000  # Duración del desvanecimiento de la música (en ms).

    # Rutas de los audios utilizados en la clase Audio.
    _music_path = "../media/music/music.mp3"
    _start_sound_path = "../media//music/start_sound.wav"
    _eats_apple_sound_path = "../media/music/eats_apple_sound.wav"
    _game_over_sound_path = "../media//music/game_over_sound.wav"

    @classmethod
    def get_game_title(cls) -> str:
        """
        Getter para _game_title.
        """
        return cls._game_title

    @classmethod
    def get_screen_size(cls) -> tuple[int, int]:
        """
        Getter para _screen_size.
        """
        return cls._screen_size

    @classmethod
    def get_fps(cls) -> int:
        """
        Getter para _fps.
        """
        return cls._fps

    @classmethod
    def get_snake_block_size(cls) -> int:
        """
        Getter para _snake_block_size.
        """
        return cls._snake_block_size

    @classmethod
    def get_snake_head_color(cls) -> tuple[int, int, int]:
        """
        Getter para _snake_head_color.
        """
        return cls._snake_head_color

    @classmethod
    def get_snake_body_color(cls) -> tuple[int, int, int]:
        """
        Getter para _snake_body_color.
        """
        return cls._snake_body_color

    @classmethod
    def get_apple_color(cls) -> tuple[int, int, int]:
        """
        Getter para _snake_body_color.
        """
        return cls._apple_color

    @classmethod
    def get_apple_size(cls) -> int:
        """
        Getter para _snake_body_color.
        """
        return cls._apple_size

    @classmethod
    def get_time_to_refresh(cls) -> int:
        """
        Getter para _time_to_refresh.
        """
        return cls._time_to_refresh

    @classmethod
    def get_time_game_over(cls) -> int:
        """
        Getter para _time_game_over.
        """
        return cls._time_game_over

    @classmethod
    def get_image_background(cls) -> str:
        """
        Getter para background_image_path.
        """
        return cls._background_image_path

    @classmethod
    def get_image_apple(cls) -> list:
        """
        Getter para background_image_path.
        """
        return cls._image_apple_path

    @classmethod
    def get_image_snake_head(cls) -> list:
        """
        Getter para _image_snake_path_head.
        """
        return cls._image_snake_path_head

    @classmethod
    def get_image_snake_body(cls) -> list:
        """
        Getter para _image_snake_path_body1.
        """
        return cls._image_snake_path_body
    #//////////////////////////////////////////////////////////////////////
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
    def get_start_sound_path(cls) -> str:
        """
        Getter para _start_sound_path.
        """
        return cls._start_sound_path

    @classmethod
    def get_eats_apple_sound_path(cls) -> str:
        """
        Getter para _eats_apple_sound_path.
        """
        return cls._eats_apple_sound_path

    @classmethod
    def get_game_over_sound_path(cls) -> str:
        """
        Getter para _game_over_sound_path.
        """
        return cls._game_over_sound_path

