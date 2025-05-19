"""
Nombre del equipo: Átomos
Integrantes: Bryan Gracida Tapia, Addi Toro Chávez
fecha: 13 de mayo del 2025
versión: 0.6
Se implementó la lógica del juego para determinar al ganador. Para ello:
    -Se agregó la función check_winner() en el módulo Game_functionalities.py, con las siguientes características:
        -Esta función recibe como parámetro el grupo de las marcas.
        -Los valores de retorno son la bandera de game_over y el resultado.
        -La bandera de game_over es verdadera si hay un ganador o si se tiene un empate.
        -El resultado puede ser que hay un ganador (❌ o ⭕) o un empate (draw).
    -La función check_winner() se llama en el ciclo while dentro de la función principal del juego.
Se agregó la pantalla del fin del juego. Para ello:
    -Se agregó la clase ResultsImage en el módulo Media.py, por lo que:
        -Se agregaron tres imágenes en el directorio media para cada caso: ganó ❌ (winX.png), ganó ⭕ (winO.png) o fue un empate (draw.png).
        -La clase carga la imagen de acuerdo al resultado (recibido como un parámetro).
    -Se agregó la clase CreditsImage en el módulo Media.py, por lo que:
        -Se agregó la imagen credits_image.png en el directorio Media.py.
        -La clase únicamente carga la imagen para mostrarla.
    -Se agregó la función game_over_screen() en el módulo Game_functionalities.py, con las siguientes características:
        -Esta función recibe como parámetros el resultado y todos los parámetros de la función screen_refresh().
        -Dentro de esta función, se crea un objeto de la clase ResultsImage y otro de la clase CreditsImage. Para dar un efecto de parpadeo, se dibuja y elimina el objeto del resultado cada determinado tiempo.
        -Para lograr lo anterior, se utiliza a la función screen_refresh(), del módulo Game_functionalities.py. En este caso, se dibuja el objeto del resultado y se espera un tiempo, después se llama a función para redibujar los elementos (sin el resultado) y se espera un tiempo, y así sucesivamente. Ese es el motivo de por qué se requieren todos los parámetros de la función screen_refresh() en la función game_over_screen().
    -La función game_over_screen() se llama si la bandera game_over de la función check_winner() es verdadera.
"""
from pygame.sprite import Group

#Se importan los módulos para el videojuego
import pygame
from Configurations import Configurations
from Game_functionalities import game_events,screen_refresh,check_winner,game_over_screen
from Media import Background,TurnImage


def run_game()->None:
    """
    Función principal del videojuego.
    """
    # Inicia modulo pygame
    pygame.init()

    # Se inicializa la pantalla
    screen = pygame.display.set_mode(Configurations.get_screen_size())
    pygame.display.set_caption(Configurations.get_game_title())
    clock = pygame.time.Clock()

    background = Background()
    # Ciclo principal del juego

    # Se crea el objeto de marcador.
    marks = Group()

    turn_image = TurnImage()

    result = ''

    game_over = False

    while not game_over:
        game_events(marks, turn_image)
        #Se verifica si existe un ganador por cada turno
        game_over,result = check_winner(marks)
        # Se dibuja los elementos gráficos en la pantalla
        screen_refresh(screen, clock, background, marks, turn_image)

        # Se cierran los recursos del juego
    game_over_screen(screen, clock, background, marks, turn_image, result)
    pygame.quit()


# Código a nivel de módulo
if __name__ == '__main__':
    run_game()