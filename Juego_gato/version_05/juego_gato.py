"""
Nombre del equipo: Átomos
Integrantes: Bryan Gracida Tapia, Addi Toro Chávez
fecha: 13 de mayo del 2025
versión: 0.5
Ahora se verifica que las casillas no estén ocupadas al crear una nueva marca. Para ello:
    -Se modificó la función game_events(), del módulo Game_functionalities.py, para realizar lo siguiente:
    -Se revisa el número de celdas utilizadas por las marcas que ya están creadas. Esto se realiza utilizando el mélodo de acceso get_cell_number() para obtener el número de celda de cada marca (objetos de la clase TicTacToeMark).
    -Si se presiona la tecla correspondiente y la casilla no está siendo utilizada, entonces se agrega el objeto de la nueva marca y después se agrega al grupo de las marcas.
Se agregaron las imágenes del turno (❌ o ⭕) en la pantalla. Para ello:w
    -Se agregaron las imágenes turnO.png y turnX.png al directorio media.
    -Se agregó la clase TurnImage en el módulo Media.py.
        -Esta clase contiene la imagen que indica el turno. Por lo tanto, se almacenan ambas imágenes (❌ y ⭕), aunque, inicialmente, el atributo image contiene la imagen del turno ❌.
        -Por lo tanto, también incluye un mélodo llamado change_turn() para conmutar la imagen del turno, el cual recibe una cadena del turno a cambiar como parámetro.
    -Se creó un objeto turn_image de la clase TurnImage.
    -Se modificó la función game_events(), del módulo Game_functionalities.py, para realizar lo siguiente:
        -Una vez que se agregó la marca al grupo de marcas, entonces también se conmuta la imagen del turno. En este caso, el turno actual se obtiene del atributo de clase _current_payer de la clase TicTacToeMark, así que se manda como argumento al método change_turn() del objeto turn_image.
        -La función game_events() ahora recibe el objeto turn_image.
    -Se modificó la función screen_refresh(), del módulo Game_functionalities.py, para agregar lo siguiente:
        -La función recibe el objeto con la imagen del turno como parámetro.
        -Se dibuja el objeto en la imagen del turno en la ventana.
"""
from pygame.sprite import Group

#Se importan los módulos para el videojuego
import pygame
from Configurations import Configurations
from Game_functionalities import game_events,screen_refresh
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

    game_over = False

    while not game_over:
        game_over = game_events(marks, turn_image)
        # Se dibuja los elementos gráficos en la pantalla
        screen_refresh(screen, clock, background, marks, turn_image)
        # Se cierran los recursos del juego
    pygame.quit()


# Código a nivel de módulo
if __name__ == '__main__':
    run_game()