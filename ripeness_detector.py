import cv2

def detect_ripeness(hsv, mask):
    saturation = cv2.mean(hsv[:,:,1], mask=mask)[0]

    if saturation < 70:
        return "Unripe"
    elif saturation < 140:
        return "Ripe"
    else:
        return "Overripe"
