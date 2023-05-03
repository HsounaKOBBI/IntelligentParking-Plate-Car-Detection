import cv2
import numpy as np

#car_cascade = cv2.CascadeClassifier('cars.xml')

def parking_lot_status(filename):
    parking_lot = cv2.imread(filename)
    gray= cv2.cvtColor(parking_lot, cv2.COLOR_BGR2GRAY)
    frameBlur=cv2.GaussianBlur(gray,(5,5),1)
    frameThreshold=cv2.adaptiveThreshold(frameBlur,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                                         cv2.THRESH_BINARY_INV,105,9)
    frameMedian=cv2.medianBlur(frameThreshold,5)
    kernel=np.ones((3,3),np.uint8)
    FrameDilate=cv2.dilate(frameMedian,kernel,iterations=1)


    count=cv2.countNonZero(FrameDilate)
    if count >1200:
        return "unavailable"


    else:
        return "available"
'''
    parking_lot = cv2.imread(filename)

    frame= cv2.resize(parking_lot, None, fx= 0.5, fy= 0.5, interpolation= cv2.INTER_LINEAR)


    gray= cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)



    detected_cars = car_cascade.detectMultiScale(gray,1.1,1)
     gray = cv2.cvtColor(parking_lot, cv2.COLOR_BGR2GRAY)

    detected_cars = car_cascade.detectMultiScale(gray, 1.01, 0) 

    if len(detected_cars) == 0:
    
        return "available"

    elif len(detected_cars) > 0:

        return "unavailable" '''
