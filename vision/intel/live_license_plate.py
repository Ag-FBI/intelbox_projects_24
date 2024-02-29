# import the necessary packages
import cv2



# def main():
#     nPlateCascade = cv2.CascadeClassifier("haarclassifierplate.xml")
#     minArea = 500
#     color1 = (255, 0, 255)
#     color2 = (0, 255, 0)
#     cap = cv2.VideoCapture(0)
#     recording = False
#     while True:
#         # load the input image from disk and resize it
#         ret, img = cap.read()
#         img = imutils.resize(img, width=320)
#         imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#         numberPlate = nPlateCascade.detectMultiScale(imgGray, 1.1, 4)
        
#         for (x, y, w, h) in numberPlate:
#             area = w*h
#             if area > minArea:
#                 cv2.rectangle(img, (x,y), (x+w, y+h), color1, 2)
#                 cv2.putText(img, "Number Plate", (x,y-5),
#                             cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, color1, 2)
#                 imgNumberPlate= img[y:y+h, x:x+w]
#                 cv2.imshow("Number Plate", imgNumberPlate)
#                 if cv2.waitKey(1) == ord('q'):
#                     break
#         cv2.imshow(img)
 


# main()

import numpy as np
import cv2 as cv
cap = cv.VideoCapture(0)
nPlateCascade = cv2.CascadeClassifier("haarclassifierplate.xml")
color1 = (255, 0, 255)
color2 = (0, 255, 0)
if not cap.isOpened():
    print("Cannot open camera")
    exit()
while True:
    # Capture frame-by-frame
    ret, frame = cap.read()
    # if frame is read correctly ret is True
    if not ret:
        print("Can't receive frame (stream end?). Exiting ...")
        break
        # Our operations on the frame come here
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    numberPlate = nPlateCascade.detectMultiScale(gray, 1.1, 4)
    minArea = 500
    for (x, y, w, h) in numberPlate:
        area = w*h
        if area > minArea:
            cv2.rectangle(gray, (x,y), (x+w, y+h), color1, 2)
            cv2.putText(gray, "Number Plate", (x,y-5),
                        cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, color1, 2)
            imgNumberPlate= gray[y:y+h, x:x+w]
            cv2.imshow("Number Plate", imgNumberPlate)
            if cv2.waitKey(1) == ord('q'):
                break
    # Display the resulting frame
    cv.imshow('frame', gray)
    if cv.waitKey(1) == ord('q'):
        break
# When everything done, release the capture
cap.release()
cv.destroyAllWindows()