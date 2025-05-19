"""
Nombre del equipo: Átomos
Integrantes: Bryan Gracida Tapia, Addi Toro Chávez
fecha: 13 de mayo del 2025
"""
import pygame
from Configurations import Configurations
from Media import Background,ResultsImage, CreditsImage
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

def check_winner(marks: pygame.sprite.Group) -> tuple[bool, str]:
    """
    Verifica si hay un ganador o empate.
    :param marks: Grupo de marcas colocadas.
    :return: Una tupla (bool, str), donde el bool indica si el juego terminó,
             y el str indica el ganador ('❌', '⭕') o 'draw' en caso de empate.
    """
    # Inicializar el tablero vacío
    board = [''] * 9
    for mark in marks:
        index = mark.get_cell_number() - 1
        board[index] = mark.get_player()

    # Combinaciones ganadoras: filas, columnas y diagonales
    win_combinations = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8),  # Filas
        (0, 3, 6), (1, 4, 7), (2, 5, 8),  # Columnas
        (0, 4, 8), (2, 4, 6)              # Diagonales
    ]

    # Verificar si hay un ganador
    for combo in win_combinations:
        a, b, c = combo
        if board[a] and board[a] == board[b] == board[c]:
            return True, board[a]  # Hay un ganador

    # Verificar empate
    if all(cell != '' for cell in board):
        return True, 'draw'  # Empate

    return False, ''  # Juego en curso


def game_over_screen(screen: pygame.surface.Surface,
                   clock: pygame.time.Clock,
                   background:Background,
                   marks: pygame.sprite.Group,
                   turn_image, result:str) -> None:
    """
    Muestra pantalla final con resultado parpadeante y créditos.
    """


    result_image = ResultsImage(result)
    credits = CreditsImage()

    for _ in range(6):
        # Muestra el resultado
        screen_refresh(screen, clock, background, marks, turn_image)
        screen.blit(result_image.image, result_image.rect)
        screen.blit(credits.image, credits.rect)
        pygame.display.flip()
        pygame.time.wait(500)

        # Oculta el resultado (pero mantiene fondo y marcas)
        screen_refresh(screen, clock, background, marks, turn_image)
        pygame.display.flip()
        pygame.time.wait(500)