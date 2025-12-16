import cv2

def detect_color(hsv, mask):
    mean_hue = cv2.mean(hsv, mask=mask)[0]

    if mean_hue < 20:
        return "Red"
    elif mean_hue < 35:
        return "Yellow"
    else:
        return "Green"
