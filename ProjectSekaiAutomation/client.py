from PIL import Image
from ppadb.client import Client as AdbClient
import win32con, win32gui, win32ui
from threading import Thread
from ahk import AHK
import keyboard
import subprocess
import time
import numpy as np
from matplotlib import pyplot as plt
import cv2

# ahk = AHK()


def captureWindow(window_title, width, height):
    hwnd = win32gui.FindWindow(None, window_title)
    wDC = win32gui.GetWindowDC(hwnd)
    dcObj = win32ui.CreateDCFromHandle(wDC)
    cDC = dcObj.CreateCompatibleDC()
    dataBitMap = win32ui.CreateBitmap()
    dataBitMap.CreateCompatibleBitmap(dcObj, width, height)
    cDC.SelectObject(dataBitMap)
    cDC.BitBlt((0, 0), (width, height), dcObj, (0, 0), win32con.SRCCOPY)
    dataBitMap.SaveBitmapFile(cDC, 'windowCapture.bmp')
    dcObj.DeleteDC()
    cDC.DeleteDC()
    win32gui.ReleaseDC(hwnd, wDC)
    win32gui.DeleteObject(dataBitMap.GetHandle())


def imageToNumpyArr(img, upper_bound=0.72, lower_bound=0.87, width_bound=0.05):
    image = "latest.png"
    image = Image.open(img)
    width, height = image.width, image.height
    image_array = np.array(image)
    return image_array[int(height * upper_bound):int(height * lower_bound),
                       int(width * width_bound):int(-width * width_bound)]


def createImageFromArr(array):
    image = Image.fromarray(array)
    image.save('output_image2.jpg')

# createImageFromArr(imageToNumpyArr("noteBar.png"))

def getContours(img):
    img = cv2.imread(img)
    imgray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # imgray = cv2.equalizeHist(imgray)
    cv2.imshow("w", imgray)
    ret, thresh = cv2.threshold(imgray, 45, 255, cv2.THRESH_BINARY_INV)
    contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE , cv2.CHAIN_APPROX_NONE)
    # cv2.drawContours(img, contours, -1, (0, 255, 0), 3)
    print(len(contours))
    for i in range(10,  len(contours)):
        # print(contours[i], "\n")
        cv2.drawContours(img, contours, i, (0, 255, 0), 3)
        cv2.imshow("contours", img)
        cv2.waitKey()

    cv2.imshow("contours", img)
    cv2.waitKey()
# getContours("output_image2.jpg")
template = cv2.imread('note1.png')
note1TestImg = cv2.imread("note1TestImg2.png")
note1 = cv2.imread("note1.png")

gray_image = cv2.cvtColor(note1TestImg, cv2.COLOR_BGR2GRAY)
gray_template = cv2.cvtColor(note1, cv2.COLOR_BGR2GRAY)
result = cv2.matchTemplate(gray_image, gray_template, cv2.TM_CCOEFF_NORMED)
# print(result)

min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
print(min_val)
print(max_val)
print(min_loc)
print(max_loc)
top_left = max_loc
bottom_right = (top_left[0] + template.shape[1], top_left[1] + template.shape[0])
cv2.rectangle(note1TestImg, top_left, bottom_right, (0, 255, 0), 2)


cv2.imshow('Template Matching Result', note1TestImg)
cv2.waitKey(0)



class Client:

    def __init__(self):
        self.title = "BlueStacks App Player"  # to store the title of the window
        self.process = "HD-Player.exe"
        self.window = None  # to store the window handle
        self.device = None  # to store the ADB device handle
        self.port = None
        self.client = AdbClient(host="127.0.0.1", port=5037)
        self.clock = time.time()
        self.emulatorThread = Thread(target=self.launchEmulator)  # to store the emulator thread

    def launchEmulator(self):
        print("starting up...")
        subprocess.call([rf"C:\Program Files\BlueStacks_nxt\{self.process}"], shell=True)

    def getWindow(self):
        try:
            # wait up to 5 seconds for WINDOW
            self.window = ahk.win_wait(title=self.title, timeout=5)
            print(f"Got AHK window handle at {self.window}")
        except TimeoutError:
            print(f'{self.title} was not found!')

    def getPort(self):
        with open("C:/ProgramData/BlueStacks_nxt/bluestacks.conf") as infile:
            matches = [line for line in infile.readlines() if "bst.instance.Pie64.status.adb_port" in line]
        self.port = matches[0][36:-2]

    def getDevice(self):
        adb_path = r"C:\platform-tools\adb.exe"
        subprocess.run([adb_path, "devices"])
        subprocess.run([adb_path, "connect", f"localhost:{self.port}"])

        self.device = self.client.device(f"localhost:{self.port}")

    def run(self):
        try:
            self.emulatorThread.start()
            self.getWindow()
            self.getPort()
            self.getDevice()

            time.sleep(3)

            while True:
                if keyboard.is_pressed("ctrl") and keyboard.is_pressed('q'):
                    print("Program terminated")
                    break

                if keyboard.is_pressed("ctrl") and keyboard.is_pressed('c'):
                    captureWindow(self.title, self.window.get_position()[2], self.window.get_position()[3])
                    createImageFromArr(imageToNumpyArr("windowCapture.bmp"))
                    time.sleep(1)

        finally:
            print("Finished running")

    def arrToContoursArr(array):
        img = cv2.imread("pjsekaiTest2.JPG")
