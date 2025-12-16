import cv2
import numpy as np

def preprocess_image(frame):
    blurred = cv2.GaussianBlur(frame, (7, 7), 0)
    hsv = cv2.cvtColor(blurred, cv2.COLOR_BGR2HSV)

    # Fruit-friendly HSV ranges (NOT skin)
    lower = np.array([20, 60, 60])     # excludes skin tones
    upper = np.array([90, 255, 255])   # green/yellow fruits

    mask = cv2.inRange(hsv, lower, upper)

    kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (7, 7))
    mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
    mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)

    return hsv, mask
