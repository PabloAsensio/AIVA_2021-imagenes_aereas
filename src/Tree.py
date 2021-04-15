from typing import Tuple

class Tree:
    def __init__(self, row: int, col: int, width: int, height: int):
        self._row = row
        self._col = col
        self._width = width
        self._height = height
        self._coordx = None
        self._coordy = None

    def set_coordenates(self, x: float, y: float):
        """
        Set coordenates in Tree object.

        :param float x: x coordenate (West-East).
        :param float y: y coordenate (North-Sourth).
        """
        self._coordx = x
        self._coordy = y

    def get_image_info(self) -> Tuple:
        """
        Returns in Tree image info.

        :retun: row, col, width, height
        """
        return self._row, self._col, self._width, self._height
        
