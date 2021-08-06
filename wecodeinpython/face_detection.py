# Before: pip install cv2
import cv2
import sys

# Get user supplied values:
imagePath = sys.argv[1]
cascPath = "haarcascade_frontalface_default.xml"

# Create the haar cascade:
faceCascade = cv2.CascadeClassifier(cascPath)

# Read the image:
image = cv2.imread(imagePath)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Detect faces in the image:
faces = faceCascade.detectMultiScale(
    gray,
    scaleFactor = 1.5,
    minNeighbors = 10,
    minSize = (45, 45),
    flags = cv2.cv.CV_HAAR_SCALE_IMAGE
)

print("Found {0} faces!".format(len(faces)))

# Draw a rectangle around the faces:
for(a, b, c, d) in faces:
    cv2.rectangle(image, (a, b), (a+c, b+d), (0, 255, 0), 2)

cv2.imshow("Faces found", image)
cv2.waitKey(0)