"""
Nombre del equipo: Átomos
Integrantes: Bryan Gracida Tapia, Addi Toro Chávez
fecha: 13 de mayo del 2025
"""
import pygame
from Configurations import Configurations
from Media import Background
from TikTacToe import TicTacToeMark


def game_events(marks: pygame.sprite.Group)->bool:
    """
    Función que administra los eventos de juego.
    :return: la bandera del fin del juego.
    """
    game_over=False

    # Se verifican los eventos (teclado, ratón) del juego.
    for event in pygame.event.get():
        # Un clic en cerrar el juego
        if event.type == pygame.QUIT:
            game_over = True
        elif event.type == pygame.KEYDOWN:
            # llaves de celda para obtener la posición según la letra que se presione.
            key_to_cell = {
                pygame.K_q: 1, pygame.K_w: 2, pygame.K_e: 3,
                pygame.K_a: 4, pygame.K_s: 5, pygame.K_d: 6,
                pygame.K_z: 7, pygame.K_x: 8, pygame.K_c: 9,
            }
            if event.key in key_to_cell:
                new_mark = TicTacToeMark(key_to_cell[event.key])
                marks.add(new_mark)
    #Se regresa la bandera
    return game_over

def screen_refresh(screen: pygame.surface.Surface,clock:pygame.time.Clock,
                   background:Background, marks: pygame.sprite.Group)->None:
    """
    Función que administra los elementos visuales del juego.
    :return:
    """
    #Fondo de la pantalla
    background.blit(screen)

    # Dibujar la marca sobre la pantalla
    marks.draw(screen)

    #Se actuliza la pantalla
    pygame.display.flip()

    #Se controla velocidad de pantalla de FPS del juego
    clock.tick(Configurations.get_fps())