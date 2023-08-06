import cv2

cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print("Cannot open camera")
    exit()

while True:
    ret, frame = cap.read()
    # frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

    cv2.imshow("frame", frame)

cap.release()

cv2.destroyAllWindows()