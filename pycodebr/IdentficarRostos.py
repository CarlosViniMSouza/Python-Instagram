# Before: pip install opencv-python&numpy&dlib

import cv2
import numpy as np
import dlib

cap = cv2.VideoCapture(0)
det = dlib.get_frontal_face_detector()

while True:
    ret, frame = cap.read()
    frame = cv2.flip(frame, 1)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    face = det(gray)

    i = 0

    for side in face:
        x, y = side.left(), side.top()
        x1, y1 = side.right(), side.bottom()
        cv2.rectangle(frame, (x, y), (x1, y1), (0, 255, 0), 2)
        i += i
        cv2.putText(frame, 'face num ' + str(i), (x-10, y-10),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)
        print(side, i)

    cv2.imshow()

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()