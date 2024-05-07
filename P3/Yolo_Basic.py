import cv2
import os
from ultralytics import YOLO

model = YOLO("yolov8n.pt")

img_path = "images/Child.jpg"
image = cv2.imread(img_path)  # Read the image
print(image.shape)  # Print the shape of the image

results = model(image)  # Perform object detection
  

# Wait for a key press
cv2.waitKey(0)
