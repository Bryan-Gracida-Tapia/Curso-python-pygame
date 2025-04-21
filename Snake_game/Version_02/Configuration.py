class Configurations:
    """
    Clase que contiene todas las configuraciones del juego
    """

    # Configuraciones de la pantalla.
    _screen_size = (1280, 720)               # Ancho y Alto
    _game_title = "Snake game in pygame"     # Título del juego
    _background = (10, 10, 90)               # Fondo de la pamtalla en formato RGB

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
