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
        if event.type == pygame.KEYDOWN:
            if event.type == pygame.K_RIGHT:    # verificar movimiento a la derecha.
                Snakeblock.set_is_moving_right(True)
                Snakeblock.set_is_moving_letf(False)
                Snakeblock.set_is_moving_up(False)
                Snakeblock.set_is_moving_down(False)

            if event.type == pygame.K_LEFT:     # verificar movimiento a la izquierda.
                Snakeblock.set_is_moving_right(False)
                Snakeblock.set_is_moving_letf(True)
                Snakeblock.set_is_moving_up(False)
                Snakeblock.set_is_moving_down(False)

            if event.type == pygame.K_UP:       # verificar movimiento hacia arriba.
                Snakeblock.set_is_moving_right(False)
                Snakeblock.set_is_moving_letf(False)
                Snakeblock.set_is_moving_up(True)
                Snakeblock.set_is_moving_down(False)

            if event.type == pygame.K_DOWN:     # verificar movimiento hacia abajo.
                Snakeblock.set_is_moving_right(False)
                Snakeblock.set_is_moving_letf(False)
                Snakeblock.set_is_moving_up(False)
                Snakeblock.set_is_moving_down(True)

    return game_over

def snake_movment(snake_body : pygame.sprite.Group):
    """
    Función que gestiona el movimiento del cuarpo de la serpiente.
    :param snake_body: Grupo con el cuerpo de la serpiente.
    """
    head = snake_body.sprites()[0]

    if Snakeblock.get_is_moving_right():
        head.rect.x += Configurations.get_snake_block_size()

    elif Snakeblock.get_is_moving_letf():
        head.rect.x -= Configurations.get_snake_block_size()

    elif Snakeblock.get_is_moving_up():
        head.rect.y += Configurations.get_snake_block_size()

    elif Snakeblock.get_is_moving_down():
        head.rect.y -= Configurations.get_snake_block_size()


def screen_refresh(screen: pygame.surface.Surface, clock: pygame.time.Clock, snake_body: pygame.sprite.Group) -> None:
    """
    Funcion que administra los elementos visuales del juego
    """

    # Fondo de la pantalla en formato RGB
    screen.fill(Configurations.get_background())
    # Se dibuja el cuerpo de la serpiente
    for snake_block in snake_body.sprites():
        snake_block.blit(screen)
    # Se actualiza la pantalla.
    pygame.display.flip()

    # Se controla la velocidad de FPS del juego
    clock.tick(Configurations.get_fps())