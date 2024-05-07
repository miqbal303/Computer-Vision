# resizing

import os
import cv2

img = cv2.imread(os.path.join(".","images","Squirrel.jpeg"))

resize_image = cv2.resize(img,(640,480))

print("original_Size",img.shape)
print("resize_image", resize_image)

cv2.imshow("img", img)
cv2.imshow("resize_image", resize_image)
cv2.waitKey(0)