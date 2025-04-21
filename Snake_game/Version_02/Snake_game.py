"""
Nombre:
Fecha:
Versión 02
- Se agregó la clase configurations que va a incluir todas las configuariones del juego
- Se agregó el módulo functionalities que contiene la función que administra los eventos y elementos del juego
"""
import pygame
from Game_functionalities import game_event,screen_refresh
from Configuration import Configurations



def run_game()->None:
    """
    Función principal del juego
    :return:
    """

    pygame.init()

    # Inicializar la pantalla
    screen = pygame.display.set_mode(Configurations.get_screen_size())

    # Se configura el nombre del juego.
    pygame.display.set_caption(Configurations.get_game_title())

    # Ciclo principal del juego.
    game_over = False
    while not game_over:
        # verificar los eventos del juego.
        game_over = game_event()

        # Dibujar los elementos graficos en la panatalla.
        screen_refresh(screen)

    pygame.quit()

if __name__ == '__main__':
    run_game()
