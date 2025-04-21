"""
Nombre:
Fecha:
Versión 01
Se crea la pantalla de inicio y se crea el titulo de la pantalla
"""
import pygame
from Game_functionalities import game_event,screen_refresh
from Configuration import Configurations
from Snake import Snakeblock
from pygame.sprite import Group



def run_game()->None:
    """
    Función principal del juego
    :return:
    """

    pygame.init()

    # Se configura el reloj del juego
    clock = pygame.time.Clock()
    # Inicializar la pantalla
    screen = pygame.display.set_mode(Configurations.get_screen_size())

    # Se configura el nombre del juego.
    pygame.display.set_caption(Configurations.get_game_title())

    # se crea el objeto(cabeza de la serpiente
    snake_head = Snakeblock(is_head= True)
    snake_head.snake_head_init()

    # Se crea un grupo para almacenar el cuerpo de 'la serpiente
    snake_body = Group()
    snake_body.add(snake_head)

    # Ciclo principal del juego.
    game_over = False
    while not game_over:
        # verificar los eventos del juego.
        game_over = game_event()

        # Dibujar los elementos graficos en la panatalla.
        screen_refresh(screen,clock,snake_body)

    pygame.quit()

if __name__ == '__main__':
    run_game()