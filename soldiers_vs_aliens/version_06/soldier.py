from pygame.sprite import Sprite
from Configurations import Configurations
import pygame


class Soldier(Sprite):
    """
    Clase que contiene al soldado.
    """

    def __init__(self,screen: pygame.surface.Surface):
        super().__init__()
        # se lee si el objeto esta en movimiento
        self._is_moving_up = False
        self._is_moving_down = False
        self._is_shoot = False
        """NUEVO."""
        # Lista que almacena los frames del soldado.
        self._frames = []

        """CAMBIO. Ahora se carga la hoja, en lugar de una única imagen."""
        # Se carga la hoja que contiene los frames del soldado.
        sheet_path = Configurations.get_soldier_sheet_path()
        soldier_sheet = pygame.image.load(sheet_path)

        # Se obtienen los datos para "recortar" cada sprite de la hoja de sprites.
        sheet_frames_per_row = Configurations.get_frames_per_row()
        sheet_frames_row = Configurations.get_frames_row()

        sheet_width = soldier_sheet.get_width()
        sheet_height = soldier_sheet.get_height()

        # Calculamos el ancho y alto de cada frame en la hoja
        soldier_frame_width = sheet_width // sheet_frames_per_row
        soldier_frame_height = sheet_height // sheet_frames_row

        # Se obtiene el tamaño para escalar cada frame
        soldier_frame_size = Configurations.get_soldier_block_size()

        # Se recortan los sprites, se escalan y se guardan en la lista de frames
        for j in range(sheet_frames_row):
            for i in range(sheet_frames_per_row):
                x = i * soldier_frame_width
                y = j * soldier_frame_height

                # Definir el rectángulo que recorta la imagen desde la hoja de sprites
                subsurface_rect = (x, y, soldier_frame_width, soldier_frame_height)
                frame = soldier_sheet.subsurface(subsurface_rect)

                # Escalar la imagen al tamaño deseado
                frame = pygame.transform.scale(frame, (soldier_frame_size, soldier_frame_size))

                # Guardar el frame recortado y escalado
                self._frames.append(frame)


        """NUEVO."""
        # Se incluyen los atributos para la animación.
        self._last_update_time = pygame.time.get_ticks()  # Se relaciona con el tiempo de actualización de cada frame.
        self._frame_index = 0  # Índice de la lista.

        """NUEVO."""
        # Se selecciona la primera imagen a mostrar.
        self.image = self._frames[self._frame_index]
        self._frame_index = 1

        # Se obtiene el rectángulo que representa la posición del sprite.
        self.rect = self.image.get_rect()

        # Se inicializa la posición inicial, en este caso, a la derecha de la pantalla.
        screen_rect = screen.get_rect()
        self.rect.right = screen_rect.right
        self.rect.centery = screen_rect.centery

        """NUEVO."""
        # Se incluyen los atributos para el movimiento.
        self._rect_y = float(self.rect.y)
        self._speed = Configurations.get_soldier_speed()

    """NUEVO."""

    def update_position(self, screen: pygame.surface.Surface) -> None:
        """
        Se utiliza para actualizar la posición del soldado de acuerdo a las banderas de movimiento.
        :param screen: Pantalla en donde se verifican los límites.
        """
        # Se obtiene el rectángulo del borde de la pantalla
        screen_rect = screen.get_rect()

        # Se verifican los estados de la bandera para modificar la posición.
        if self._is_moving_up:
            self._rect_y -= self._speed

        elif self._is_moving_down:
            self._rect_y += self._speed

        # Se verifica que el personaje no sobrepase los bordes de la pantalla.
        if self._rect_y < float(screen_rect.top):
            self._rect_y = float(screen_rect.x)

        elif self._rect_y > (screen_rect.bottom - self.image.get_height()):
            self._rect_y = float(screen_rect.bottom - self.image.get_height())

        # Se actualiza la posición del rectángulo de acuerdo a la posición.
        self.rect.y = int(self._rect_y)

    """NUEVO."""

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
            if self._is_shoot:
                if self._frame_index >= len(self._frames):
                    self._frame_index = 0
            else:
                if self._frame_index >= len(self._frames) / 2:
                    self._frame_index = 0


    def blit(self, screen: pygame.surface.Surface) -> None:
        """
        Se utiliza para dibujar el soldado en la pantalla.
        :param screen: Pantalla en donde se dibuja el bloque.
        """
        # Se dibuja sobre la pantalla.
        screen.blit(self.image, self.rect)

    @property
    def is_moving_up(self) -> bool:
        """
        Getter para self._is_moving_up.
        """
        return self._is_moving_up

    @is_moving_up.setter
    def is_moving_up(self, value: bool) -> None:
        """
        Setter para self._is_moving_up
        """
        self._is_moving_up = value

    @property
    def is_moving_down(self) -> bool:
        """
        Getter para self._is_moving_down.
        """
        return self._is_moving_down

    @is_moving_down.setter
    def is_moving_down(self, value: bool) -> None:
        """
        Setter para self._is_moving_down
        """
        self._is_moving_down = value

    @property
    def is_shoot(self) -> bool:
        """
        Getter para self._is_shoot.
        """
        return self._is_shoot

    @is_shoot.setter
    def is_shoot(self, value: bool) -> None:
        """
        Setter para self._is_shoot.
        """
        self._is_shoot = value
