import time
import pygame
from Configuration import Configurations
from Snake import SnakeBlock
from Apple import Apple
from Media import Background

def game_events() -> bool:
    """
    Función que administra los eventos del juego.
    :return: La bandera de fin del juego.
    """
    # Se declara la bandera de fin del juego que se retorna.
    game_over = False

    # Se verifican los eventos (teclado y ratón) del juego.
    for event in pygame.event.get():
        # El evento es un clic para cerrar el juego.
        if event.type == pygame.QUIT:
            game_over = True

        # El evento es presionar una tecla (KEYDOWN).
        elif event.type == pygame.KEYDOWN:
            # Movimiento hacia la derecha.
            if event.key == pygame.K_RIGHT:
                SnakeBlock.set_is_moving_right(True)
                SnakeBlock.set_is_moving_left(False)
                SnakeBlock.set_is_moving_up(False)
                SnakeBlock.set_is_moving_down(False)

            # Movimiento hacia la izquierda.
            if event.key == pygame.K_LEFT:
                SnakeBlock.set_is_moving_right(False)
                SnakeBlock.set_is_moving_left(True)
                SnakeBlock.set_is_moving_up(False)
                SnakeBlock.set_is_moving_down(False)

            # Movimiento hacia arriba.
            if event.key == pygame.K_UP:
                SnakeBlock.set_is_moving_right(False)
                SnakeBlock.set_is_moving_left(False)
                SnakeBlock.set_is_moving_up(True)
                SnakeBlock.set_is_moving_down(False)

            # Movimiento hacia abajo.
            if event.key == pygame.K_DOWN:
                SnakeBlock.set_is_moving_right(False)
                SnakeBlock.set_is_moving_left(False)
                SnakeBlock.set_is_moving_up(False)
                SnakeBlock.set_is_moving_down(True)

    # Se regresa la bandera.
    return game_over

def snake_movement(snake_body: pygame.sprite.Group) -> None:
    """
    Función que gestiona los movimientos de los bloques que componen el cuerpo de la serpiente.
    :param snake_body: Grupo con el cuerpo de la serpiente.
    """

    body_size = len(snake_body.sprites()) - 1

    for i in range(body_size,0,-1):
        snake_body.sprites()[i].rect.x = snake_body.sprites()[i-1].rect.x
        snake_body.sprites()[i].rect.y = snake_body.sprites()[i - 1].rect.y

    # El movimiento de la cabeza de la serpiente depende de las banderas de movimiento.
    head = snake_body.sprites()[0]          # La cabeza de la serpiente es el elemento [0] del grupo.

    if SnakeBlock.get_is_moving_right():
        head.rect.x += Configurations.get_snake_block_size()

    elif SnakeBlock.get_is_moving_left():
        head.rect.x -= Configurations.get_snake_block_size()

    elif SnakeBlock.get_is_moving_up():
        head.rect.y -= Configurations.get_snake_block_size()

    elif SnakeBlock.get_is_moving_down():
        head.rect.y += Configurations.get_snake_block_size()

def check_collicions(screen: pygame.surface.Surface,snake_body: pygame.sprite.Group, apples : pygame.sprite.Group ) -> bool:
    """
    Función que revisa las coliciones del juego
    - Cabeza de la serpiente con el cuerpo
    - Cabeza de la serpiente con el borde de la pantalla
    - Cabeza de la serpiente con la manzana
    """
    # Se declara la bandera de fin de juego
    game_over = False

    # Se obtiene la cabeza de la serpiente
    head = snake_body.sprites()[0]

    # Se revisa primero la cabeza de la serpiente con el borde de la pantalla.
    screen_rect = screen.get_rect()

    if (head.rect.right > screen_rect.right) or (head.rect.left < screen_rect.left) or (head.rect.top < screen_rect.top) or (head.rect.bottom > screen_rect.bottom):
        game_over = True

    # Se revisa las colición de la cabeza de la serpiente con el cuerpo de la serpiente.
    head_body_collicions = pygame.sprite.spritecollide(head, snake_body, dokill= False)

    if len(head_body_collicions) > 1:
        game_over  = True

    # se revisa la colicion de la cabeza de la serpiente con la manzana.
    apple_collitions = pygame.sprite.spritecollide(head, apples, dokill= True)

    if len(apple_collitions) > 0:
        new_snake_block = SnakeBlock()
        new_snake_block.rect.x = snake_body.sprites()[-1].rect.x
        new_snake_block.rect.y = snake_body.sprites()[-1].rect.y
        snake_body.add(new_snake_block)

        new_apple = Apple()
        new_apple.random_position(snake_body)
        apples.add(new_apple)

    return game_over

def screen_refresh(screen: pygame.surface.Surface, clock: pygame.time.Clock,
                   snake_body: pygame.sprite.Group, apples: pygame.sprite.Group, background : Background()) -> None:
    """
    Función que administra los elementos de la pantalla.
    :param screen: Objeto con la pantalla.
    :param clock: Objeto con el reloj del videojuego.
    :param snake_body: Grupo con el cuerpo de la serpiente.
    """
    # se dibuja el fondo de la pantalla
    background.blit(screen)

    # Se dibujan los elementos en la pantalla.
    #screen.fill(Configurations.get_background())    # Fondo de la pantalla en formato RGB.

    # Se dibuja la serpiente, dibujando primero el último bloque y al último la cabeza de la serpiente.
    for snake_block in reversed(snake_body.sprites()):
        snake_block.blit(screen)

    # Se dinuja la manzana.
    apples.draw(screen)

    # Se actualiza la pantalla, dando la impresión de movimiento.
    pygame.display.flip()

    # Se controla la velocidad de fotogramas (FPS) del videojuego.
    clock.tick(Configurations.get_fps())

def game_over_screen():
    """
    Función con la parte del fin del juego.
    """
    time.sleep(Configurations.get_time_game_over())