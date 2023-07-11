import cv2
import numpy as np
import os
from PIL import Image

# cam = cv2.VideoCapture("C:/Users/michh/Downloads/pjSekaiVideos/butterfly_on_your_right_shoulder.mp4")

frameno = 0
def getSekaiScreenshots():
    while(True):
       ret,frame = cam.read()
       if ret:
          # if video is still left continue creating images
          name = "pjSekaiScreenshots/butterfly_on_your_right_shoulder" + str(frameno) + '.jpg'
          cv2.imwrite(name, frame)
          frameno += 1

       else:
          break

# cam.release()
# cv2.destroyAllWindows(

def imageToNumpyArr(img):
    image = Image.open(img)
    width, height = image.width, image.height
    upper_bound = 0.68
    lower_bound = 0.87
    width_bound = 0.05
    image_array = np.array(image)
    return image_array[int(height * upper_bound):int(height * lower_bound),
           int(width * width_bound):int(-width * width_bound)]


def createImageFromArr(imgName, array):
    image = Image.fromarray(array)
    image.save("processed_pj_Sekai_Screenshots/" + imgName)

def resizeScreenshot(imgName):
    searchDirectory = "pjSekaiScreenshots/"
    img = cv2.imread(searchDirectory + imgName)
    width = 1400
    height = int( width/img.shape[1] * img.shape[0] )
    dim = (width, height)
    resizedImg = cv2.resize(img, dim, interpolation = cv2.INTER_AREA)
    cv2.imwrite("resized_pj_sekai_images/" + imgName, resizedImg)


fileName = "butterfly_on_your_right_shoulder0.jpg"

# imageToNumpyArr("pjSekaiScreenshots/butterfly_on_your_right_shoulder0.jpg")
dirName = "pjSekaiScreenshots"
for image in os.listdir(dirName):
    resizeScreenshot(image)
    createImageFromArr( image, imageToNumpyArr( "resized_pj_sekai_images/" + image ))
