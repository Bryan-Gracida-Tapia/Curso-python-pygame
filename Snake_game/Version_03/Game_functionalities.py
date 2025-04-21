import pygame
from Configuration import Configurations
from Snake import Snakeblock


def game_event()-> bool:

    """
    Funcion que administra los eventos del juego

    :return: bandera de fin de juego
    """
    game_over = False

    # verificar los eventos del juego.
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True

    return game_over


def screen_refresh(screen: pygame.surface.Surface, clock: pygame.time.Clock, snake_head : Snakeblock) -> None:
    """
    Funcion que administra los elementos visuales del juego

    :return:
    """

    # Fondo de la pantalla en formato RGB
    screen.fill(Configurations.get_background())
    # Se dibuja la cabeza de la serpiente
    snake_head.blit(screen)
    # Se actualiza la pantalla.
    pygame.display.flip()

    # Se controla la velocidad de FPS del juego
    clock.tick(Configurations.get_fps())