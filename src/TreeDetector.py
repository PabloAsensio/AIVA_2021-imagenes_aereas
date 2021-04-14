from typing import List, Tuple

import cv2 as cv
import numpy as np
import numpy.typing as npt


class TreeDetector:
    def __init__(self, nn):
        """
        TreeDetector constructor.

        :param NeuralNetwork nn: the neural network witch we will used.
        """
        self._img = None
        self._coordenates = None
        self._nn = nn  # Neural Network
        self._trees = []

    def recognize(self, img: npt.ArrayLike, coordenates: Tuple) -> List:
        """
        Recognize trees in image.

        :param npt.ArrayLike img: The target image.
        :param tuple coordenates: The coordenates of the image.
        :return: the list with all detected trees.
        """
        self._img = img
        self._slide()
        return self._trees

    def _slide(self):
        """
        Iterates around the image and calls NN to detect trees in sub-image.
        """
        STEP = 400
        cols, rows = self._img.shape[:-1]
        for col in range(0, cols - STEP, STEP):
            for row in range(0, rows - STEP, STEP):
                trees = self._nn.detect_trees(
                    self._img[row : row + STEP, col : col + STEP], row, col
                )
                self._trees.append(trees)
