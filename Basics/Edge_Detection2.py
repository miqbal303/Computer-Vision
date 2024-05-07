import cv2
import os
import numpy as np

# Read the image
img = cv2.imread(os.path.join(".", "images", "1.jpg"))

# Check if the image is loaded successfully
if img is None:
    print("Error: Unable to load image.")
else:
    # Resize the image if necessary to fit it into display
    # Let's resize it to fit within a 1000x1000 window
    max_display_dim = 1000
    height, width = img.shape[:2]
    if height > max_display_dim or width > max_display_dim:
        if height > width:
            img = cv2.resize(img, (max_display_dim, int(max_display_dim * height / width)))
        else:
            img = cv2.resize(img, (int(max_display_dim * width / height), max_display_dim))

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

    # Display the original image, Canny edges, dilated edges, and eroded edges
    cv2.imshow("Original Image", img)
    cv2.imshow("Canny Edges", img_edge)
    cv2.imshow("Dilated Edges", img_dilated)
    cv2.imshow("Eroded Edges", img_eroded)

    # Wait for a key press and then close all windows
    cv2.waitKey(0)
    cv2.destroyAllWindows()
