import torch
import cv2
from super_gradients.training import models

DEVICE = 'cuda' if torch.cuda.is_available() else 'cpu'
MODEL_ARCH = 'yolo_nas_s'

model = models.get(MODEL_ARCH, pretrained_weights="coco").to(DEVICE)

CONFIDENCE_TRESHOLD = 0.35

image = cv2.imread("bus.jpg")

results = model.predict(image, conf=CONFIDENCE_TRESHOLD)

for result in results:
    print(result.prediction)