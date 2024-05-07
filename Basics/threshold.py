import cv2
import os

img = cv2.imread(os.path.join(".", "images", "Horse.jpeg"))

img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

ret, thresh = cv2.threshold(img_gray, 80, 255, cv2.THRESH_BINARY)

thresh2 = cv2.adaptiveThreshold(img_gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 21, 30)
#                                             ^^^^^^^^ Use img_gray here instead of img

cv2.imshow("image", img)
cv2.imshow("Thresh", thresh)
cv2.imshow("Thresh2", thresh2)
cv2.waitKey(0)
