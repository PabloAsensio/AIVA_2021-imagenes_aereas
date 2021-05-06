import unittest
import cv2 as cv

import sys, os
sys.path.insert(0, os.path.abspath('..'))

from src.TreeDetector import TreeDetector


class TestTreeDetector(unittest.TestCase):
    def test_recognize(self):
    #     img = cv.imread("images/peticion/austin14750_1250.tif")
    #     tree_detector = TreeDetector(img)
    #     result = tree_detector.recognize()
    #     self.assertEqual(result, "done")
        pass

    def test_slide_images(self):
        # img = cv.imread("images/5000/austin1.tif")
        # tree_detector = TreeDetector(img)
        # result = tree_detector.slide()
        # self.assertEqual(result, 400)
        pass

if __name__ == "__main__":
    unittest.main()
