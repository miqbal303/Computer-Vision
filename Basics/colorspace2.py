import os
import cv2

img = cv2.imread(os.path.join(".", "images", "Family.jpg"))

# Convert image to grayscale
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# Convert image to HSV color space
img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

# Convert image to LAB color space
img_lab = cv2.cvtColor(img, cv2.COLOR_BGR2LAB)

# Display the original image and the converted images
cv2.imshow("Original Image", img)
cv2.imshow("Grayscale Image", img_gray)
cv2.imshow("RGB Image", img_rgb)
cv2.imshow("HSV Image", img_hsv)
cv2.imshow("LAB Image", img_lab)

cv2.waitKey(0)
