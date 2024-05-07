import os
import cv2

img = cv2.imread(os.path.join(".", "images", "Squirrel.jpeg"))

# Apply average blur with a kernel size of 5x5
k_size = 15
#blurred_img = cv2.blur(img, (5, 5))
blurred_img = cv2.blur(img, (k_size, k_size))
# Display the original and blurred images
cv2.imshow("Original Image", img)
cv2.imshow("Average Blurred Image", blurred_img)

# Apply Gaussian blur with a kernel size of 5x5 and standard deviation of 0
blurred_img = cv2.GaussianBlur(img, (5, 5), 0)

# Display the original and blurred images
cv2.imshow("Original Image", img)
cv2.imshow("Gaussian Blurred Image", blurred_img)

# Apply median blur with a kernel size of 5x5
blurred_img = cv2.medianBlur(img, 5)

# Display the original and blurred images
cv2.imshow("Original Image", img)
cv2.imshow("Median Blurred Image", blurred_img)

# Apply bilateral filter with a diameter of 9, sigma color of 75, and sigma space of 75
blurred_img = cv2.bilateralFilter(img, 9, 75, 75)

# Display the original and blurred images
cv2.imshow("Original Image", img)
cv2.imshow("Bilateral Blurred Image", blurred_img)

cv2.waitKey(0)
