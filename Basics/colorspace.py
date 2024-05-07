import os
import cv2

img = cv2.imread(os.path.join(".", "images", "Squirrel.jpeg"))

# Split the image into its color channels
b, g, r = cv2.split(img)

# Display each color channel separately
cv2.imshow("Blue Channel", b)
cv2.imshow("Green Channel", g)
cv2.imshow("Red Channel", r)

cv2.waitKey(0)
