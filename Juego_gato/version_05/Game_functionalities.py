"""
Nombre del equipo: Átomos
Integrantes: Bryan Gracida Tapia, Addi Toro Chávez
fecha: 13 de mayo del 2025
"""
import pygame
from Configurations import Configurations
from Media import Background
from TikTacToe import TicTacToeMark


def game_events(marks: pygame.sprite.Group, turn_image)->bool:
    """
    Función que administra los eventos de juego.
    :return: la bandera del fin del juego.
    """
    game_over = False

    used_cells = [mark.get_cell_number() for mark in marks]

    # llaves de celda para obtener la posición según la letra que se presione.
    key_to_cell = {
        pygame.K_q: 1, pygame.K_w: 2, pygame.K_e: 3,
        pygame.K_a: 4, pygame.K_s: 5, pygame.K_d: 6,
        pygame.K_z: 7, pygame.K_x: 8, pygame.K_c: 9,
    }

    # Se verifican los eventos(teclado y ratón) del juego
    for event in pygame.event.get():
        # Un clic en cerrar el juego
        if event.type == pygame.QUIT: game_over = True

        if event.type == pygame.KEYDOWN:
            if event.key in key_to_cell:
                cell = key_to_cell[event.key]
                if cell not in used_cells:  # Sí la celda no está en uso.
                    mark = TicTacToeMark(cell)
                    # new_mark = TicTacToeMark(key_to_cell[event.key])
                    marks.add(mark)
                    # Cambiar la imagen según el turno.
                    turn_image.change_turn(TicTacToeMark._current_player)

    # Se regresa la bandera
    return game_over


def screen_refresh(screen: pygame.surface.Surface,
                   clock: pygame.time.Clock,
                   background: Background,
                   marks: pygame.sprite.Group,
                   turn_image) -> None:
    """
    Función que administra los elementos visuales del juego
    """

    # Se dibuja el fondo de la pantalla
    background.blit(screen)

    # Dibujar la marca sobre la pantalla
    marks.draw(screen)

    screen.blit(turn_image.image, turn_image.rect)

    # Se actualiza la pantalla
    pygame.display.flip()

    # Se controla la velocidad de fotogramas (FPS) del videojuego.
    clock.tick(Configurations.get_fps())