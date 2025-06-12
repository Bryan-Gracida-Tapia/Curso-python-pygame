"""
Nombre del equipo: Átomos
Integrantes: Bryan Gracida Tapia, Addi Toro Chávez
fecha: 13 de mayo del 2025
versión: 0.3

"""

#Se importan los módulos para el videojuego
import pygame
from pygame.sprite import Group
from Configurations import Configurations
from Game_functionalities import game_events,screen_refresh
from Media import Background
from soldier import Soldier
from Shot import Shot



def run_game()->None:
    """
    Función principal del videojuego.
    """
    #Se inicializa el módulo de pygame
    pygame.init()


    #Se configura el reloj del juego
    clock=pygame.time.Clock()

    #Se crea el objeto con el fondo de pantalla
    background=Background()

    #Se inicializa la pantalla
    screen=pygame.display.set_mode(Configurations.get_screen_size())

    #Se crea el objeto del soldado
    soldier = Soldier(screen)

    shots = Group()
    #Se configura el título del juego
    pygame.display.set_caption(Configurations.get_game_title())#Mostrar título

    #Ciclo principal del videojuego
    game_over=False

    while not game_over:
        # Se verifican los eventos (teclado, ratón) del juego.
        game_over = game_events(soldier,shots)


        # Se dibujan los elementos gráficos en la pantalla
        screen_refresh(screen,clock, background,soldier,shots)

        # Se cierran los recursos de pygame
    pygame.quit()

if __name__ == '__main__':
    run_game()