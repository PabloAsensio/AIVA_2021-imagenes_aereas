import cv2 as cv


class TreeDetector:
    def __init__(self, img):
        self.__img = cv.imread(img)

    def recognize(self):
        return "done"

    def slide(self):
        return 400