import cv2
from super_gradients.training import models

yolo_nas_s = models.get("yolo_nas_s", pretrained_weights="coco")

cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print("Cannot open camera")
    exit()

while True:
    ret, frame = cap.read()
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    res = yolo_nas_s.predict(frame, conf=0.25)

    for image_prediction in res:
        class_names = image_prediction.class_names
        labels = image_prediction.prediction.labels
        confidence = image_prediction.prediction.confidence
        bboxes = image_prediction.prediction.bboxes_xyxy

        for i, (label, conf, bbox) in enumerate(zip(labels, confidence, bboxes)):
            print("prediction: ", i)
            print("label_id: ", label)
            print("label_name: ", class_names[int(label)])
            print("confidence: ", conf)
            print("bbox: ", bbox)
            print("--" * 10)
