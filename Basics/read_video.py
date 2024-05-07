import cv2
import os

# read video
video_path = os.path.join(".","Video","All Ironman suit-ups 2008-2019 in 4K-a971ed09.mp4")

webcame = cv2.VideoCapture(video_path)


#visualiza video

ret =True

while True:
    ret, frame = webcame.read()

    cv2.imshow("video", frame)
    if cv2.waitKey(40) & 0xFF == ord("q"):
        break

webcame.release()
cv2.destroyAllWindows()