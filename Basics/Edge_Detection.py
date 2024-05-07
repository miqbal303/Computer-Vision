import cv2
import os
import numpy as np

img = cv2.imread(os.path.join(".", "images", "Family.jpg"))

# Convert the image to grayscale
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Apply Canny edge detection
img_edge = cv2.Canny(img_gray, 100, 200)

# Perform dilation to enhance edges
kernel = np.ones((5,5), np.uint8)
img_dilated = cv2.dilate(img_edge, kernel, iterations=1)

# Perform erosion to refine edges
kernel = np.ones((3, 3), np.uint8)
img_eroded = cv2.erode(img_edge, kernel, iterations=1)

# Display the original image, Canny edges, and dilated edges
cv2.imshow("image", img)
cv2.imshow("img_edge", img_edge)
cv2.imshow("img_dilated", img_dilated)
cv2.imshow("img_eroded", img_eroded)
cv2.waitKey(0)
