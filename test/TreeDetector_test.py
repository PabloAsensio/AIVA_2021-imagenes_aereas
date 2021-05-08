import unittest
import cv2 as cv

import sys, os

sys.path.insert(0, os.path.abspath('..'))

from src.TreeDetector import TreeDetector
from src.NeuralNetwork import NeuralNetwork


class TestTreeDetector(unittest.TestCase):
    def test_recognize(self):
        # Load one image which contains trees
        img_path = "../images/test_images/test_completa1_2.png"
        img = cv.imread(img_path)
        coordenates = (None, None)

        # Load retinanet
        retinanet = NeuralNetwork("../src/model/model.h5")

        # Run the detection of trees
        tree_detector = TreeDetector(retinanet)
        trees = tree_detector.recognize(img, coordenates)

        # If the number of objects 'Tree' generated is greater than zero the neural network works fine.
        self.assertGreater(len(trees), 0)
        pass

if __name__ == "__main__":
    unittest.main()
