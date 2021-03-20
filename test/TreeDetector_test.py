import unittest
import cv2 as cv

from src.TreeDetector import TreeDetector


class TestTreeDetector(unittest.TestCase):
    def test_Recognize(self):
        img = cv.imread("images/peticion/austin14750_1250.tif")
        tree_detector = TreeDetector(img)
        result = tree_detector.recognize()
        self.assertEquals(result, "done")


if __name__ == "__main__":
    unittest.main()