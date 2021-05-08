from typing import List, Tuple

import cv2 as cv
import numpy as np


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

    def recognize(self, img: np.ndarray, coordenates: Tuple) -> List:
        """
        Recognize trees in image.

        :param np.ndarray img: The target image.
        :param tuple coordenates: The coordenates of the image.
        :return: the list with all detected trees.
        """
        self._img = img
        self._slide()

        # Flatten list
        self._trees = [val for sublist in self._trees for val in sublist]
        return self._trees

    def _slide(self):
        """
        Iterates around the image and calls NN to detect trees in sub-image.
        """

        STEP = 500
        
        cols, rows = self._img.shape[:-1]

        for col in range(0, cols, STEP):
            for row in range(0, rows, STEP):
                trees = self._nn.detect_trees(
                    self._img[row : row + STEP, col : col + STEP], row, col
                )
                self._trees.append(trees)
