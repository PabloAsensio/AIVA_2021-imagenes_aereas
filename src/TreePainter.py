from typing import List

import cv2 as cv
import numpy.typing as npt


class TreePainter:
    def draw(self, canvas: npt.ArrayLike, trees: List):
        """
        Draw all trees in image.

        :param npt.ArrayLike canvas: The image witch will be used as canvas.
        :param List trees: The list off all trees.
        """

        for tree in trees:
            continue
