"""
Nombre del equipo: Átomos
Integrantes: Bryan Gracida Tapia, Addi Toro Chávez
fecha: 13 de mayo del 2025
versión: 0.7
Se agregó la música y los efectos del sonido al juego. Para ello:
    -Se agregó la música (music.mp3) y los sonidos del juego (keyboard_sound.mp3 y results_sound.mp3) en el directorio media.
    -Se agregó la clase Audio en el módulo Media.py, en donde se carga la música y los sonidos del juego.
    -Inicialmente, se crea el objeto audio de la clase Audio, reproduciendo la música del juego.
    -Las funciones game_events() y game_over_screen() ahora reciben el objeto con el audio.
        -La función game_events() reproduce el sonido keyboard_sound cuando se selecciona una casilla correcta.
        -La función game_over_screen() desvanece la música y reproduce el sonido results_sound.
Todas las configuraciones realizadas se incluyeron en la clase Configurations, agregando los atributos necesarios y sus respectivos métodos de acceso.
Como resultado, ahora se tiene el juego funcional con la música del juego y los efectos de sonido al seleccionar una casilla y obtener un resultado.
"""
from pygame.sprite import Group
import pygame
from Configurations import Configurations
from Game_functionalities import game_events,screen_refresh,check_winner,game_over_screen
from Media import Background,TurnImage,Audio


def run_game()->None:
    """
    Función principal del videojuego.
    """
    # Inicia modulo pygame
    pygame.init()

    # Se inicializa la pantalla
    screen = pygame.display.set_mode(Configurations.get_screen_size())
    pygame.display.set_caption(Configurations.get_game_title())
    clock = pygame.time.Clock()

    background = Background()

    # Se crea el objeto con el sonido del juego y se reproduce la música y el sonido inicial del juego.
    audio = Audio()
    audio.play_music(volume=Configurations.get_music_volume())

    # Se crea el objeto de marcador.
    marks = Group()

    turn_image = TurnImage()

    result = ''

    game_over = False
    # Ciclo principal del juego
    while not game_over:
        game_events(marks, turn_image,audio)
        #Se verifica si existe un ganador por cada turno
        game_over,result = check_winner(marks)
        # Se dibuja los elementos gráficos en la pantalla
        screen_refresh(screen, clock, background, marks, turn_image)

        # Se cierran los recursos del juego
    game_over_screen(screen, clock, background, marks, turn_image, result,audio)
    pygame.quit()


# Código a nivel de módulo
if __name__ == '__main__':
    run_game()