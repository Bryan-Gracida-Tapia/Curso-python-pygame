"""
Nombre del equipo: Átomos
Integrantes: Bryan Gracida Tapia, Addi Toro Chávez
fecha: 13 de mayo del 2025
versión: 0.2
Se agregó la clase Configurations en el módulo Configurations.py (nuevo).
    -Esta clase va a incluir todas las configuraciones del juego.
Se agregó el módulo Game_functionalities.py (nuevo).
    -Este módulo va a contener todas las funcionalidades del juego.
    -En esta versión, contiene las funciones que administran los eventos del juego, llamada game_events(), y los elementos de la pantalla, llamada screen_refresh().
    -La función game_events() retorna la bandera del fin del juego.
    -La función screen_refresh() recibe el objeto con la pantalla.
"""

#Se importan los módulos para el videojuego
import pygame
from Configurations import Configurations
from Game_functionalities import game_events,screen_refresh


def run_game()->None:
    """
    Función principal del videojuego.
    """
    #Se inicializa el módulo de pygame
    pygame.init()

    #Se inicializa la pantalla
    screen=pygame.display.set_mode(Configurations.get_screen_size())

    #Se configura el título del juego
    pygame.display.set_caption(Configurations.get_game_title())#Mostrar título

    #Ciclo principal del videojuego
    game_over=False

    while not game_over:
        # Se verifican los eventos (teclado, ratón) del juego.
        game_over = game_events()

        # Se dibujan los elementos gráficos en la pantalla
        screen_refresh(screen)

        # Se cierran los recursos de pygame
    pygame.quit()

if __name__ == '__main__':
    run_game()