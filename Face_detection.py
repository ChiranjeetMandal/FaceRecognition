import pandas
import numpy
import cv2
#create a casecadeclassifier object 
face_casecade = cv2.CascadeClassifier("C:\\Users\\CR 7\\Downloads\\Compressed\\haarcascade_frontalface_default.xml")

#Reading an image
img = cv2.imread("C:\\Users\\CR 7\\Desktop\\2020\\elon_musk.jpg",1)

#converting into gray scale image
gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#searcg cordinate of the image
faces = face_casecade.detectMultiScale(gray_image,scaleFactor=1.02,minNeighbors=20)

print(type(faces))

print(faces)

for x,y,w,h in faces :
  img = cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3)

#resizing image
resize_img = cv2.resize(img,(int(img.shape[1]/2),int(img.shape[0]/2)))

#show image
cv2.imshow("Ledgend",resize_img)

#durationg of an image
cv2.waitKey(0)

#now distroy all command
cv.distroyAllWindows()