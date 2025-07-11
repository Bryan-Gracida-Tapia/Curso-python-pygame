import pygame
from pygame.sprite import Sprite
from Configurations import Configurations

class Soldier(Sprite):
    """
    Clase que representa un soldado (personaje principal).
    Hereda de la clase Sprite para utilizar grupos de sprites y detectar colisiones entre sprites.
    Sus atributos son: image (apariencia), rect (posición y tamaño) y banderas de movimiento y estado.
                       Además, tiene una lista con los frames para el movimiento y la animación, así como los
                       atributos requeridos para tal fin.
    Sus métodos son: blit() (dibujar), update_position (para el movimiento), update_animation (para la animación),
                     y getters y setters de las banderas de movimiento.
    """


    def __init__(self, screen: pygame.surface.Surface):
        """
        Constructor del soldado, en donde se llama al constructor padre de Sprite.
        :param screen: Objeto con la pantalla.
        """
        # Se llama al constructor de la clase padre.
        super().__init__()

        # Banderas de movimiento. Inicialmente, el personaje no se mueve.
        self._is_moving_up = False
        self._is_moving_down = False

        """NUEVO."""
        # Se agregan banderas para indicar el estado del personaje. Inicialmente, el personaje está en reposo.
        self._is_shooting = False

        # Lista que almacena los frames del soldado.
        self._frames = []

        # Se carga la hoja que contiene los frames del soldado.
        sheet_path = Configurations.get_soldier_sheet_path()
        soldier_sheet = pygame.image.load(sheet_path)

        """CAMBIO. Ahora se tiene un número columnas de la hoja de frames. Así que se considera para los recortes."""
        # Se obtienen los datos para "recortar" cada sprite de la hoja de sprites.
        sheet_frames_per_row = Configurations.get_soldier_frames_per_row()
        sheet_frames_per_column = Configurations.get_soldier_frames_per_column()
        """NUEVO."""
        sheet_width = soldier_sheet.get_width()
        sheet_height = soldier_sheet.get_height()
        soldier_frame_width = sheet_width // sheet_frames_per_row
        soldier_frame_height = sheet_height // sheet_frames_per_column
        """CAMBIO."""

        # Se obtiene el tamaño para escalar cada frame.
        soldier_frame_size = Configurations.get_soldier_size()

        """CAMBIO. Ahora también se consideran los frames de las columnas."""
        # Se recortan los sprites de la hoja, se escalan y se guardan en la lista de sprites.
        # Frames 0*(sheet_frames_per_row) a 1*(sheet_frames_per_row) - 1: Descansando.
        # Frames 1*(sheet_frames_per_row) a 2*(sheet_frames_per_row) - 1: Disparando.
        for j in range(sheet_frames_per_column):                # CAMBIO. Se agregó este segundo for.
            for i in range(sheet_frames_per_row):
                x = i * soldier_frame_width
                y = j * soldier_frame_height                    # CAMBIO. Aquí es donde se consideran las columnas.
                subsurface_rect = (x, y, soldier_frame_width, soldier_frame_height)
                frame = soldier_sheet.subsurface(subsurface_rect)

                frame = pygame.transform.scale(frame, soldier_frame_size)

                self._frames.append(frame)

        # Se incluyen los atributos para la animación.
        self._last_update_time = pygame.time.get_ticks()    # Se relaciona con el tiempo de actualización de cada frame.
        self._frame_index = 0                               # Índice de la lista.

        # Se selecciona la primera imagen a mostrar.
        self.image = self._frames[self._frame_index]
        self._frame_index = 1

        # Se obtiene el rectángulo que representa la posición del sprite.
        self.rect = self.image.get_rect()

        # Se actualiza la posición inicial, en este caso, a la derecha de la pantalla.
        screen_rect = screen.get_rect()
        self.rect.right = screen_rect.right
        self.rect.centery = screen_rect.centery

        # Se incluyen los atributos para el movimiento.
        self._rect_y = float(self.rect.y)
        self._speed = Configurations.get_soldier_speed()


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
            self._rect_y = float(screen_rect.y)

        elif self._rect_y > (screen_rect.bottom - self.image.get_height()):
            self._rect_y = float(screen_rect.bottom - self.image.get_height())

        # Se actualiza la posición del rectángulo de acuerdo a la posición.
        self.rect.y = int(self._rect_y)


    def update_animation(self) -> None:
        """
        Se utiliza para actualizar el frame visible del soldado, dando la impresión de animación.
        """
        # Se obtiene el tiempo que ha transcurrido.
        current_time = pygame.time.get_ticks()

        """CAMBIO. Se verifica el estado del personaje."""
        # Se verifica el tiempo de cada frame dependiendo del estado del personaje.
        if self._is_shooting:
            frame_delay = Configurations.get_soldier_shooting_frame_delay()

        else:
            frame_delay = Configurations.get_soldier_frame_delay()

        # Se verifica la condición para indicar si requiere actualizarse el frame.
        needs_refresh = (current_time - self._last_update_time) >= frame_delay

        # En caso verdadero, se actualiza el frame por el siguiente en la lista.
        if needs_refresh:
            self.image = self._frames[self._frame_index]
            self._last_update_time = current_time
            self._frame_index += 1

            """CAMBIO. Se modificó la forma de verificar los índices dependiendo del estado del personaje."""
            # Finalmente, se verifica si el índice ha recorrido todos los frames para volver al inicio de la lista.
            # Frames 0*(sheet_frames_per_row) a 1*(sheet_frames_per_row) - 1: Descansando.
            # Frames 1*(sheet_frames_per_row) a 2*(sheet_frames_per_row) - 1: Disparando.
            sheet_frames_per_row = Configurations.get_soldier_frames_per_row()

            if (not self._is_shooting and self._frame_index >= sheet_frames_per_row or
                    self._is_shooting and self._frame_index >= 2 * sheet_frames_per_row):
                self._frame_index = 0

            elif self._is_shooting and self._frame_index == 1:
                self._is_shooting = False


    """NUEVO."""
    def shoots(self) -> None:
        """
        Se utiliza para indicar que el personaje está disparando, por lo que debe indicar este estado.
        """
        # Se modifica la bandera del estado del soldado.
        self._is_shooting = True

        # Se modifica el índice de los frames.
        sheet_frames_per_row = Configurations.get_soldier_frames_per_row()
        self._frame_index = sheet_frames_per_row

        # Se resetea el tiempo de actualización del último frame.
        self._last_update_time = pygame.time.get_ticks()


    def blit(self, screen: pygame.surface.Surface) -> None:
        """
        Se utiliza para dibujar el soldado en la pantalla.
        :param screen: Pantalla en donde se dibuja el bloque.
        """
        # Se dibuja sobre la pantalla.
        screen.blit(self.image, self.rect)


    """ %%%%%%%     MÉTODOS DE ACCESO.    %%%%%%%%%%%%%%%%%%%%% """
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
