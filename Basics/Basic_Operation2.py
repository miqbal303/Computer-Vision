import os
import cv2

img = cv2.imread(os.path.join(".", "images", "Squirrel.jpeg"))

# Resize using INTER_AREA for downscaling
resize_image_area = cv2.resize(img, (640, 480), interpolation=cv2.INTER_AREA)

# Resize using INTER_CUBIC for upscaling
resize_image_cubic = cv2.resize(img, (640, 480), interpolation=cv2.INTER_CUBIC)

print("Original Size:", img.shape)
print("Resized Image (INTER_AREA):", resize_image_area.shape)
print("Resized Image (INTER_CUBIC):", resize_image_cubic.shape)

cv2.imshow("Original Image", img)
cv2.imshow("Resized Image (INTER_AREA)", resize_image_area)
cv2.imshow("Resized Image (INTER_CUBIC)", resize_image_cubic)
cv2.waitKey(0)
