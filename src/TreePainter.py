from typing import List

import cv2 as cv
import numpy as np


class TreePainter:
    def draw(self, canvas: np.ndarray, trees: List) -> np.ndarray:
        """
        Draw all trees in image.

        :param np.ndarray canvas: The image witch will be used as canvas.
        :param List trees: The list off all trees.
        """

        for tree in trees:
            row, col, width, height = tree.get_image_info()

            center = (int(col + width / 2), int(row + height / 2))
            radius = int(min(height / 2, width / 2))
            cv.circle(canvas, center, radius, (0,0, 255), thickness=1, lineType=8, shift=0)

        return canvas
