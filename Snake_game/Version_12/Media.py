import pygame
from Configuration import Configurations


class Background:
    """
        Clase que contiene el fondo de la pantalla
    """

    def __init__(self):
        background_image_path = Configurations.get_image_background()
        self.image = pygame.image.load(background_image_path)

        # Se restaura la escala del tamaÑo de la pantalla
        screen_size = Configurations.get_screen_size()
        self.image = pygame.transform.scale(self.image,screen_size)
        self.rec = self.image.get_rect()

    def blit(self, screen: pygame.surface.Surface):
        screen.blit(self.image,self.rec)

class Audio:
    """
    Clase que contiene el audio del videojuego, incluyendo la música y los efectos de sonido.
    Sus atributos son: la música y los sonidos.
    Sus métodos son: para reproducir y controlar la música, así como los que reproducen los sonidos.
    """
    def __init__(self):
        # Se carga la música del videojuego.
        pygame.mixer.music.load(Configurations.get_music_path())

        # Se carga el sonido de inicio.
        self._start_sound = pygame.mixer.Sound(Configurations.get_start_sound_path())

        # Se carga el sonido cuando la serpiente come una manzana.
        self._eats_apple_sound = pygame.mixer.Sound(Configurations.get_eats_apple_sound_path())

        # Se carga el sonido cuando el jugador ha perdido.
        self._game_over_sound = pygame.mixer.Sound(Configurations.get_game_over_sound_path())


    @classmethod
    def play_music(cls, volume) -> None:
        """
        Se utiliza para reproducir la música en bucle.
        """
        pygame.mixer.music.play(loops=-1)   # Un -1 indica que la música se reproduce en bucle.
        pygame.mixer.music.set_volume(volume)


    @classmethod
    def music_fadeout(cls, time) -> None:
        """
        Se utiliza para realizar un desvanecimiento de la música del juego hasta parar.
        :param time: Tiempo de desvanecimiento de la música (en ms).
        """
        pygame.mixer.music.fadeout(time)


    def play_star_sound(self) -> None:
        """
        Se utiliza para reproducir el sonido de inicio del juego.
        """
        self._start_sound.play()


    def play_eats_apple_sound(self) -> None:
        """
        Se utiliza para reproducir el sonido cuando la serpiente come la manzana.
        """
        self._eats_apple_sound.play()


    def play_game_over_sound(self) -> None:
        """
        Se utiliza para reproducir el sonido cuando el jugador ha perdido.
        """
        self._game_over_sound.play()

class Scoreboard:
    def __init__(self):
        self._typeface = "Kimono"
        self._font_size = 40
        self._font_color = (171,250,10)

        # Se agrega la imagen con el score
        self._font = pygame.font.SysFont(self._typeface,self._font_size)
        self.image = self._font.render("Puntos: 0", True, self._font_color)
        self.rect = self.image.get_rect()

        # Se ajusta la posición del marcador
        self.rect.x = Configurations.get_screen_size()[0]*0.05
        self.rect.y = Configurations.get_screen_size()[1]*0.05

    def update(self, new_score: int) ->None:
        text = "Puntos: " + str(new_score)
        self.image = self._font.render(text,True,self._font_color)

    def blit(self, screen: pygame.surface.Surface):
        screen.blit(self.image,self.rect)

class GameOverImage:
    def __init__(self):
        self.image = pygame.image.load("../Media/media snake_game/game_over_image.png")
        self.rect = self.image.get_rect()

    def blit(self, screen:pygame.surface.Surface) -> None:
        self.rect.centerx = screen.get_rect().centerx
        self.rect.bottom = screen.get_rect().bottom - Configurations.get_snake_block_size()
        screen.blit(self.image,self.rect)