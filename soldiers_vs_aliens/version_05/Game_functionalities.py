"""
Nombre del equipo: Átomos
Integrantes: Bryan Gracida Tapia, Addi Toro Chávez
fecha: 13 de mayo del 2025
"""
import pygame
from Configurations import Configurations
from Media import Background
from soldier import Soldier
from Shot import  Shot

def game_events(soldier:Soldier,shots:pygame.sprite.Group)->bool:
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
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                soldier.is_moving_up = True
            if event.key == pygame.K_DOWN:
                soldier.is_moving_down = True

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                soldier.is_moving_up = False
            if event.key == pygame.K_DOWN:
                soldier.is_moving_down = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                new_shot = Shot(soldier)
                #shots.remove(shots.sprites()[0])
                shots.add(new_shot)

    #Se regresa la bandera
    return game_over

def screen_refresh(screen: pygame.surface.Surface,clock:pygame.time.Clock,
                   background:Background, soldier:Soldier, shots:pygame.sprite.Group)->None:
    """
    Función que administra los elementos visuales del juego.
    :return:
    """
    #Fondo de la pantalla
    background.blit(screen)

    #Se actualiza la posicion del soldado
    soldier.update_position(screen)
    soldier.update_animation()
    #Se sobrepone la image del soldado
    soldier.blit(screen)

    for shot in shots.sprites():
        shot.update_position()
        shot.update_animation()

    shots.draw(screen)

    #Se actuliza la pantalla
    pygame.display.flip()

    #Se controla velocidad de pantalla de FPS del juego
    clock.tick(Configurations.get_fps())