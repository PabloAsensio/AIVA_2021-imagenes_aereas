import unittest
import cv2 as cv

from src.TreeDetector import TreeDetector


class TestTreeDetector(unittest.TestCase):
    def test_recognize(self):
        img = cv.imread("images/peticion/austin14750_1250.tif")
        tree_detector = TreeDetector(img)
        result = tree_detector.recognize()
        self.assertEqual(result, "done")

    def test_slide_images(self):
        img = cv.imread("images/5000/austin1.tif")
        tree_detector = TreeDetector(img)
        result = tree_detector.slide()
        self.assertEqual(result, 400)


if __name__ == "__main__":
    unittest.main()
