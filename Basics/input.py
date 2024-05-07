import cv2
import os

# read image
image_path = os.path.join(".", "images", "Horse.jpeg")

img = cv2.imread(image_path)

# write image

# cv2.imwrite(os.path.join(".", "images", "Horse_out.jpeg"), img)

# visualiza image
cv2.imshow("image", img)
cv2.waitKey(200000)  # number is milisecond