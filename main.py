# color detection

import cv2

import numpy as np

from PIL import Image


def get_limits(color):
    c = np.uint8([[color]])  # here insert the bgr values which you want to convert to hsv
    hsvC = cv2.cvtColor(c, cv2.COLOR_BGR2HSV)

    lowerlimit = hsvC[0][0][0] - 10, 100, 100
    upperlimit = hsvC[0][0][0] + 10, 255, 255

    lowerlimit = np.array(lowerlimit, dtype=np.uint8)
    upperlimit = np.array(upperlimit, dtype=np.uint8)

    return lowerlimit, upperlimit


yellow = [0, 255, 255]  # yellow in BGR colorspace
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()

    hsvImage = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    lowerlimit, upperlimit = get_limits(color=yellow)

    mask = cv2.inRange(hsvImage, lowerlimit, upperlimit)

    mask_ = Image.fromarray(mask)

    bbox = mask_.getbbox()

    if bbox is not None:
        x1, y1, x2, y2 = bbox

        frame = cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 5)

    cv2.imshow('frame', frame)
    if cv2.waitKey(40) & 0xFF == ord('q'):  # press 'q' to exit
        break

cap.release()
cv2.destroyAllWindows()
