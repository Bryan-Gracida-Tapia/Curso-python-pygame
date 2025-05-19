"""
Nombre del equipo: Átomos
Integrantes: Bryan Gracida Tapia, Addi Toro Chávez
fecha: 13 de mayo del 2025
versión: 0.4
-Se agregaron las marcas ❌ y ⭕ al juego. Para ello:
 --Se agregaron las imágenes markO.png y markX.png al directorio media.
 --Se agregó la clase TicTacToeMark (hereda de la clase Sprite) en el módulo TikTacToe.py (nuevo).
   ---Esta clase contiene la imagen (❌ o ⭕) en el atributo image, dependiendo del turno del jugador.
   ---El turno del jugador se maneja como un atributo de clase, que inicialmente inicia en ❌ y conmuta cada que se crea un objeto de la clase.
   ---Como parámetro en el constructor, se recibe el número de la casilla (números del 1 al 9).
   ---Dependiendo del número de la casilla, se ajusta la posición (x, y) de su atributo rect.
-Se agregó el grupo marks que contiene todas las marcas (❌ y ⭕) de ambos jugadores.
-Se modificó la función game_events(), del módulo Game_functionalities.py, para agregar lo siguiente:
 --Cada que se presione alguna de las teclas (q, w, e, a, s, d, z, x, c), se crea un nuevo objeto de la clase TicTacToeMark, en donde se indica el número de la casilla (del 1 al 9) como argumento, dependiendo de la tecla presionada.
 --El objeto creado se agrega al grupo marks, por lo que debe recibirse como parámetro de la función      game_events().
-Se modificó la función screen_refresh(), del módulo Game_functionalities.py, para agregar lo siguiente:
 --La función recibe el grupo de las marcas como parámetro.
 --Se dibuja el grupo de las marcas en la ventana.
"""
from pygame.sprite import Group

#Se importan los módulos para el videojuego
import pygame
from Configurations import Configurations
from Game_functionalities import game_events,screen_refresh
from Media import Background


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

    #Se configura el título del juego
    pygame.display.set_caption(Configurations.get_game_title())#Mostrar título

    #Se crea el grupo de las marcas
    marks = Group()

    #Ciclo principal del videojuego
    game_over=False

    while not game_over:
        # Se verifican los eventos (teclado, ratón) del juego.
        game_over = game_events(marks)

        # Se dibujan los elementos gráficos en la pantalla
        screen_refresh(screen,clock, background,marks)

        # Se cierran los recursos de pygame
    pygame.quit()

if __name__ == '__main__':
    run_game()