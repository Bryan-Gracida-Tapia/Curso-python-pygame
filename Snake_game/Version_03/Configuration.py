class Configurations:
    """
    Clase que contiene todas las configuraciones del juego
    """

    # Configuraciones de la pantalla.
    _screen_size = (1280, 720)               # Ancho y Alto
    _game_title = "Snake game in pygame"     # Título del juego
    _background = (10, 10, 90)               # Fondo de la pamtalla en formato RGB

    # Configuraciones de la serpiente
    _snake_block_size = 40                  # Tamaño del bloque de la serpiente
    _snake_head_color = (255, 200, 20)      # Color de la cabeza de la serpiente
    _snake_body_color = (0,255,0)           # color del cuerpo de la serpiente
    _fps = 8
    @classmethod
    def get_screen_size(cls)-> tuple[int,int]:
        """
        Getter para _screen_size
        :return:
        """
        return cls._screen_size

    @classmethod
    def get_game_title(cls) -> str:
        """
        Getter para _game_title
        :return:
        """
        return cls._game_title

    @classmethod
    def get_background(cls) -> tuple[int, int, int]:
        """
        Getter para _background
        :return:
        """
        return cls._background

    @classmethod
    def get_fps(cls) -> int:
        """
        Getter para _fps
        :return:
        """
        return cls._fps

    @classmethod
    def get_snake_block_size(cls) -> int:
        """
        Getter para _snake_block_size
        :return:
        """
        return cls._snake_block_size

    @classmethod
    def get_snake_head_color(cls) -> tuple[int, int, int]:
        """
        Getter para _snake_head_color
        :return:
        """
        return cls._snake_head_color

    @classmethod
    def get_snake_body_color(cls) -> tuple[int, int, int]:
        """
        Getter para _snake_body_color
        :return:
        """
        return cls._snake_body_color
