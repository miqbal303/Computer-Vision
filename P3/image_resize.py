import cv2
from ultralytics import YOLO
import numpy as np

model = YOLO("yolov8n.pt")

# Load the image
img_path = "images/Family.jpg"
image = cv2.imread(img_path)

# Resize the image while preserving the aspect ratio
width = 640
height = 640
aspect_ratio = image.shape[1] / image.shape[0]
resized_width = width
resized_height = int(resized_width / aspect_ratio)
if resized_height > height:
    resized_height = height
    resized_width = int(resized_height * aspect_ratio)
resized_image = cv2.resize(image, (resized_width, resized_height))

# Create a black canvas with the desired size
canvas = 128 * np.ones((height, width, 3), dtype=np.uint8)

# Paste the resized image onto the canvas
start_x = (width - resized_width) // 2
start_y = (height - resized_height) // 2
canvas[start_y:start_y+resized_height, start_x:start_x+resized_width] = resized_image

# Perform object detection
results = model(canvas, show = True)


# Wait for a key press
cv2.waitKey(0)
