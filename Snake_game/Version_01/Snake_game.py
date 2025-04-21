"""
Nombre:
Fecha:
Versión 01
Se crea la pantalla de inicio y se crea el titulo de la pantalla
"""
import pygame


def run_game()->None:
    """
    Función principal del juego
    :return:
    """

    pygame.init()

    # Inicializar la pantalla
    screen_size = (1280, 720) # Ancho y Alto
    screen = pygame.display.set_mode(screen_size)

    # Se configura el nombre del juego.
    game_title="Snake game in pygame"
    pygame.display.set_caption(game_title)

    # Ciclo principal del juego.
    game_over= False
    while not game_over:
        # verificar los eventos del juego.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True

        # Dibujar los elementos graficos en la panatalla.
        background = (10, 10, 90) # Fondo de la pamtalla en formato RGB
        screen.fill(background)

        # Se actualiza la pantalla.
        pygame.display.flip()

    pygame.quit()

if __name__ == '__main__':
    run_game()
