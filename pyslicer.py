import cv2
import numpy as np


def videoSlicer(video_path, intervals=20):
    video = cv2.VideoCapture(video_path)

    frames = int(video.get(cv2.CAP_PROP_FRAME_COUNT))
    fps = video.get(cv2.CAP_PROP_FPS)

    video_length = float(frames)/fps

    for t in np.linspace(1, video_length, intervals):
        video.set(cv2.CAP_PROP_POS_MSEC, int(t) * 1000)  # Convert to milliseconds

        success, frame = video.read()

        if not success:
            print("Error reading frame at timestamp:", int(t))

        cv2.imwrite(rf"screenshots/src_@{int(t)}.jpg", frame)

    video.release()


videoSlicer("pirate.mp4")
