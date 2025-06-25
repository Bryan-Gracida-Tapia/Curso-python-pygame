"""
Nombre: Alberto Martínez Barbosa.
Fecha:
Versión 0.6:
- Ahora el soldado muestra una animación al disparar una bala. Para ello:
  * Se agregó el archivo soldier-idle_shooting_sheet.png al directorio media.
    + Esta hoja de frames contiene 2 filas con 4 frames cada una, la primera fila tiene los frames de la
      animación de descanso y la segunda con la animación del disparo.
    + Esta hoja reemplaza a soldier-idle-sheet.png de la versión anterior.
  * Se modificó lo siguiente en la clase Soldier:
    + Se agregó una bandera como atributo que indica si está o no disparando.
    + Se consideró la forma de "recortar" los frames de la hoja de frames, considerando las 2 filas. Además,
      se identificó que los frames 0 a 3 representan la animación de descanso y los frames 4 a 7 a la animación
      de disparo.
    + Se agregó el métod0 shoots(), en donde se activa la bandera que indica que está disparando, se establece
      el índice del frame inicial de la animación del disparo y se reinicializan los tiempos para la animación.
    + Se modificó el métod0 update_animation(), considerando que se tiene que verificar el estado del soldado
      (descansando o disparando). Dependiendo de ello, se van a mostrar ciertos frames de la lista de frames.
      Dependiendo de la misma condición, se modificó el tiempo de espera entre cada frame, considerando que la
      animación del disparo es más rápida que la de descanso. Una vez se mostraron todos los frames de la
      animación del disparo, entonces se desactiva la bandera que indica que está disparando, regresando a la
      animación de descanso.
  * Se modificó lo siguiente en la función game_events() del módulo Game_functionalities.py:
    + Ahora, además de crear el nuevo objeto del disparo cuando se revisa el evento de presionar la tecla espacio,
      también se llama al métod0 soldier.shoots(), para iniciar la lógica descrita anteriormente.
- Todas las configuraciones realizadas se incluyeron en la clase Configurations, agregando los atributos necesarios
  y sus respectivos métodos de acceso.
- Como resultado, ahora el soldado muestra una animación cada que se dispara una bala 🔫. En este caso, la cantidad
  de disparos sigue siendo ilimitada.

"""
from random import randint

# Se importan los módulos necesarios.
import pygame
from Configurations import Configurations
from Game_functionalities import game_events, screen_refresh
from Media import Background
from soldier import Soldier
from pygame.sprite import Group
from Alien import Alien


def run_game() -> None:
    """
    Función principal del videojuego.
    """
    # Se inicializa el módulo de pygame y se realizan las configuraciones iniciales.
    pygame.init()
    screen_size = Configurations.get_screen_size()
    screen = pygame.display.set_mode(screen_size)
    clock = pygame.time.Clock()  # Se usa para controlar la velocidad de fotogramas (FPS).

    # Se configura el título de la ventana.
    game_title = Configurations.get_game_title()
    pygame.display.set_caption(game_title)

    # Se crea el objeto del fondo de pantalla.
    background = Background()

    # Se crea el objeto del soldado (personaje principal).
    soldier = Soldier(screen)

    # Se crea el grupo para almacenar los disparos del soldado.
    gunshots = Group()

    # Se crea el grupo para almacenar los disparos del soldado.
    aliens = Group()
    min_aliens = 5
    aliens_to_spawn = min_aliens* randint(0,10)
    for i in range(aliens_to_spawn):
        alien = Alien(screen)
        aliens.add(alien)


    # Ciclo principal del videojuego.
    game_over = False
    while not game_over:

        # Función que administra los eventos del juego.
        game_over = game_events(soldier, gunshots)

        # Función que administra los elementos de la pantalla.
        screen_refresh(screen, clock, background, soldier, gunshots,aliens)

    # Cierra todos los recursos del módulo pygame.
    pygame.quit()

""" %%%%%%%     CÓDIGO A NIVEL DE MÓDULO    %%%%%%%%%%%%%%%%%%%%% """
if __name__ == "__main__":
    run_game()

