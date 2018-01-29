import cv2
import sys
import os

# Get user supplied values
imagePath = sys.argv[1]
cascPath = "haarcascade_frontalface_default.xml"

# Create the haar cascade
faceCascade = cv2.CascadeClassifier(cascPath)

# Read the image
image = cv2.imread(imagePath)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Detect faces in the image
faces = faceCascade.detectMultiScale(
    gray,
    scaleFactor=1.3,
    minNeighbors=5,
    minSize=(30, 30)
    #flags = cv2.CV_HAAR_SCALE_IMAGE
)
print("Found {0} face!".format(len(faces)))

# Draw a rectangle around the faces
i = 0
for (x, y, w, h) in faces:
	crop_img = image[y:y+h, x:x+w]
	filename = 'founded/face{0}.png'.format(i)
	directory = os.path.dirname(filename)
	try:
	    os.stat(directory)
	except:
	    os.mkdir(directory) 
	
	cv2.imwrite(filename,crop_img)
	i+=1

cv2.waitKey(0)