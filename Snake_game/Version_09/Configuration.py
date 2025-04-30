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
    _time_game_over = 1

    # Configuraciones de la serpiente.
    _snake_block_size = 40                        # Tamaño del bloque. Es muy recomendable que sea
                                                    # divisor común del largo y ancho de _screen_size.
    _snake_head_color = (255, 255, 255)             # Color de la cabeza de la serpiente.
    _snake_body_color = (162, 208, 194)                 # Color del cuerpo de la serpiente.

    # Configuraciones de la manzana.
    _apple_color = (255,0,0)
    _apple_size = _snake_block_size

    # media del juego.
    _background_image_path = "../Media/fondo.jpg"
    _image_apple_path = "../Media/apple1.png"
    _image_snake_path_head = "../Media/head1.png"
    _image_snake_path_body = ["../Media/body1.png","../Media/body2.png","../Media/body3.png"]


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
    '''
    @classmethod
    def get_background(cls) -> tuple[int, int, int]:
        """
        Getter para _background.
        """
        return cls._background
    '''
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
    def get_image_apple(cls) -> str:
        """
        Getter para background_image_path.
        """
        return cls._image_apple_path

    @classmethod
    def get_image_snake_head(cls) -> str:
        """
        Getter para _image_snake_path_head.
        """
        return cls._image_snake_path_head

    @classmethod
    def get_image_snake_body(cls) -> [str,str,str]:
        """
        Getter para _image_snake_path_body1.
        """
        return cls._image_snake_path_body

