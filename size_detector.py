import cv2

def detect_size(mask):
    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    if not contours:
        return "Unknown"

    c = max(contours, key=cv2.contourArea)
    area = cv2.contourArea(c)

    if area < 3000:
        return "Small"
    elif area < 12000:
        return "Medium"
    else:
        return "Large"
