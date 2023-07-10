from ppadb.client import Client as AdbClient
import win32con, win32gui, win32ui
from threading import Thread
from ahk import AHK
import keyboard
import subprocess
import time


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

        finally:
            print("Finished running")

