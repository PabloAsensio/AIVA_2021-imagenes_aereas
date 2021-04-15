import cv2 as cv

from src.NeuralNetwork import NeuralNetwork
from src.TreeDetector import TreeDetector
from src.TreePainter import TreePainter

if __name__ == "__main__":

    image_path = "./images/5000/austin1.tif"
    image = cv.imread(image_path)
    coordenates = (None, None)

    resnet = NeuralNetwork("./src/model/model.h5")

    tree_detector = TreeDetector(resnet)
    trees = tree_detector.recognize(image, coordenates) 

    tree_painter = TreePainter()
    canvas = tree_painter.draw(image.copy(), trees)

    cv.imwrite("detectiton.png", canvas)
