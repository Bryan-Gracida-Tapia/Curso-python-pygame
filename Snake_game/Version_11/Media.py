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
    def __init__(self):
        # se carga la música del juego
        pygame.mixer.music.load("../Media/music/music.mp3")

        # se cargan los sonidos
        self._start_sound = pygame.mixer.Sound("../Media/music/start_sound.wav")
        self._eats_apple_sound = pygame.mixer.Sound("../Media/music/eats_apple_sound.wav")
        self._game_over_sound = pygame.mixer.Sound("../Media/music/game_over_sound.wav")


    @classmethod
    def play_music(cls,volume) -> None:
        pygame.mixer.music.play(loops=-1) # El menos uno ndica que se produce en bucle
        pygame.mixer.music.set_volume(volume)


