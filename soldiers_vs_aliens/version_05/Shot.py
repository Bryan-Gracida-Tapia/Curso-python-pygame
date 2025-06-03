from pygame.sprite import Sprite
from Configurations import Configurations
import pygame


class Shot(Sprite):
    def __init__(self,screen: pygame.surface.Surface):
        super().__init__()
        # se lee si el objeto esta en movimiento
        self._is_shot = False



        # Lista que almacena los frames del disparo.
        self._frames = []


        # Se carga la hoja que contiene los frames del disparo.
        sheet_path = Configurations.get_shot_sheet_path()
        shot_sheet = pygame.image.load(sheet_path)


        # Se obtienen los datos para "recortar" cada sprite de la hoja de sprites.
        sheet_frames_per_row = Configurations.get_frames_per_row()
        sheet_width = shot_sheet.get_width()
        sheet_height = shot_sheet.get_height()
        soldier_frame_width = sheet_width // sheet_frames_per_row
        soldier_frame_height = sheet_height


        # Se obtiene el tamaño para escalar cada frame.
        shot_frame_size = Configurations.get_shot_block_size()


        # Se recortan los sprites de la hoja, se escalan y se guardan en la lista de sprites.
        for i in range(sheet_frames_per_row):
            x = i * soldier_frame_width
            y = 0
            subsurface_rect = (x, y, soldier_frame_width, soldier_frame_height)
            frame = shot_sheet.subsurface(subsurface_rect)

            frame = pygame.transform.scale(frame, (shot_frame_size,shot_frame_size))

            self._frames.append(frame)


        # Se incluyen los atributos para la animación.
        self._last_update_time = pygame.time.get_ticks()  # Se relaciona con el tiempo de actualización de cada frame.
        self._frame_index = 0  # Índice de la lista.


        # Se selecciona la primera imagen a mostrar.
        self.image = self._frames[self._frame_index]
        self._frame_index = 1

        # Se obtiene el rectángulo que representa la posición del sprite.
        self.rect = self.image.get_rect()

        # Se inicializa la posición inicial, en este caso, a la derecha de la pantalla.
        screen_rect = screen.get_rect()
        self.rect.right = screen_rect.right
        self.rect.centery = screen_rect.centery


        # Se incluyen los atributos para el movimiento.
        self._rect_x = float(self.rect.y)
        self._speed = Configurations.get_soldier_speed()

    def update_position(self, screen: pygame.surface.Surface) -> None:
        """
                Se utiliza para actualizar la posición del soldado de acuerdo a las banderas de movimiento.
                :param screen: Pantalla en donde se verifican los límites.
                """
        # Se obtiene el rectángulo del borde de la pantalla
        screen_rect = screen.get_rect()

        # Se verifican los estados de la bandera para modificar la posición.
        if self._is_shot:
            self._rect_x -= self._speed*5

        # Se verifica que el disparo no sobrepase los bordes de la pantalla.
        if self._rect_x < float(screen_rect.top):
            self._rect_x = float(screen_rect.y)

        elif self._rect_x > (screen_rect.bottom - self.image.get_height()):
            self._rect_x = float(screen_rect.bottom - self.image.get_height())

        # Se actualiza la posición del rectángulo de acuerdo a la posición.
        self.rect.x = int(self._rect_x)

    def update_animation(self) -> None:
        """
        Se utiliza para actualizar el frame visible del soldado, dando la impresión de animación.
        """
        # Se verifica si el tiempo transcurrido es mayor o igual al tiempo establecido para actualizar el frame.
        current_time = pygame.time.get_ticks()
        frame_delay = Configurations.get_soldier_frame_delay()
        needs_refresh = (current_time - self._last_update_time) >= frame_delay

        if needs_refresh:
            # En caso verdadero, se actualiza el frame por el siguiente en la lista.
            # Además, se actualizan los atributos para resetear el tiempo y actualizar el índice.
            self.image = self._frames[self._frame_index]
            self._last_update_time = current_time
            self._frame_index += 1

            # Finalmente, se verica si el índice ha recorrido todos los frames para volver al inicio de la lista.
            if self._frame_index >= len(self._frames):
                self._frame_index = 0

    def blit(self, screen: pygame.surface.Surface) -> None:
        """
        Se utiliza para dibujar el soldado en la pantalla.
        :param screen: Pantalla en donde se dibuja el bloque.
        """
        # Se dibuja sobre la pantalla.
        screen.blit(self.image, self.rect)

    @property
    def is_shot(self) -> bool:
        """
        Getter para self._is_moving_up.
        """
        return self._is_shot

    @is_shot.setter
    def is_shot(self, value: bool) -> None:
        """
        Setter para self._is_moving_up
        """
        self._is_shot = value