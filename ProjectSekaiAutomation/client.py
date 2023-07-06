import cv2, time
import numpy as np
from PIL import Image
from matplotlib import pyplot as plt

class Client:

    def __init__(self):
        self.title = ""

    def imageToNumpyArr(upper_bound=0.72, lower_bound=0.87, width_bound=0.05):
        image = Image.open("latest.png")
        width, height = image.width, image.height
        upper_bound = 0.72
        lower_bound = 0.87
        width_bound = 0.05
        image_array = np.array(image)
        return image_array[int(height * upper_bound):int(height * lower_bound),
               int(width * width_bound):int(-width * width_bound)]

    def createImageFromArr(array):
        image = Image.fromarray(array)
        image.save('output_image.jpg')

    # createImageFromArr(imageToNumpyArr())  # function composition lol

    def arrToContoursArr(array):
        img = cv2.imread("pjsekaiTest2.JPG")
