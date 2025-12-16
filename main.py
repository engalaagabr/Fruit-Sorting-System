import cv2
from utils import preprocess_image
from color_detector import detect_color
from size_detector import detect_size
from ripeness_detector import detect_ripeness

cap = cv2.VideoCapture(0)
print("Hold ONE fruit in front of the camera | Press Q to quit")

while True:
    ret, frame = cap.read()
    if not ret:
        break

    hsv, mask = preprocess_image(frame)

    color = detect_color(hsv, mask)
    size = detect_size(mask)
    ripeness = detect_ripeness(hsv, mask)

    # SORTING LOGIC
    if color == "Red" and ripeness == "Ripe":
        bin_id = "BIN 1"
    elif color == "Yellow":
        bin_id = "BIN 2"
    else:
        bin_id = "BIN 3"

    text = f"{color} | {size} | {ripeness} → {bin_id}"

    cv2.putText(frame, text, (20, 40),
                cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0,255,0), 2)

    cv2.imshow("Automated Fruit Sorting", frame)
    cv2.imshow("Fruit Mask", mask)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
