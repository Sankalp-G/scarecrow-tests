from ultralytics import YOLO
import numpy as np
import cv2

# Load a model
model = YOLO("best.pt")  # load a pretrained model (recommended for training)

# results = model.predict('bus.jpg')

cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print("Cannot open camera")
    exit()

while True:
    ret, frame = cap.read()
    # frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    results = model.predict(frame, conf=0.25, classes=0)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

    for result in results:
        print(result.boxes.conf)
        print(result.boxes.cls)
        print(result.boxes.xyxy)

        conf = result.boxes.conf
        cla = result.boxes.cls
        xyxy = result.boxes.xyxy

        for i, (c, cl, xy) in enumerate(zip(conf, cla, xyxy)):
            print("prediction: ", i)
            print("label_id: ", cl)
            print("label_name: ", result.names[int(cl)])
            print("confidence: ", c)
            print("bbox: ", xy)
            print("--" * 10)

            cv2.rectangle(frame, (int(xy[0]), int(xy[1])), (int(xy[2]), int(xy[3])), (0, 255, 0), 2)
            cv2.putText(frame, f"{model.names[int(cl)]} {c}", (int(xy[0]), int(xy[1])), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

        cv2.imshow("frame", frame)

cap.release()

cv2.destroyAllWindows()
