import cv2

vid = cv2.VideoCapture(0)

ret, frame = vid.read()
cv2.imshow('frame', frame)

if cv2.waitKey(1) & 0xFF == ord('q'):
    print("Session Stopped")

vid.release()
cv2.destroyAllWindows()