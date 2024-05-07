import os
import cv2

# Read the image
img = cv2.imread(os.path.join(".", "images", "bird.jpeg"))

# Convert the image to grayscale
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Apply thresholding
ret, thresh = cv2.threshold(img_gray, 127, 255, cv2.THRESH_BINARY_INV)

# Apply Canny edge detection
img_edge = cv2.Canny(img_gray, 100, 200)

# Find contours
contours, _ = cv2.findContours(img_edge, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Draw bounding boxes around contours with area larger than 200
img_with_contours = img.copy()
for cnt in contours:
    if cv2.contourArea(cnt) > 200:
        x, y, w, h = cv2.boundingRect(cnt)
        cv2.rectangle(img_with_contours, (x, y), (x + w, y + h), (0, 255, 0), 2)

# Display the image with contours and thresholded image
cv2.imshow("original", img)
cv2.imshow("Image with Contours", img_with_contours)
cv2.imshow("Thresholded Image", thresh)
cv2.waitKey(0)
