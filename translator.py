from dictionary import digit_to_letter, letter_to_digit
import sys

import numpy as np
import cv2
    
#######   training part    ############### 
samples = np.loadtxt('generalsamples.data',np.float32)
responses = np.loadtxt('generalresponses.data',np.float32)
responses = responses.reshape((responses.size,1))

model = cv2.KNearest()
model.train(samples,responses)

############################# testing part  #########################
digit_to_letter[7.4000001] = 'thu'
im = cv2.imread('samples/7.jpg')
out = np.zeros(im.shape,np.uint8)
gray = cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
blur = cv2.GaussianBlur(gray,(5,5),0)
thresh = cv2.adaptiveThreshold(blur,255,1,1,11,2)

contours,hierarchy = cv2.findContours(thresh,cv2.RETR_LIST,cv2.CHAIN_APPROX_SIMPLE)

for cnt in contours:
    if cv2.contourArea(cnt)>50:
        [x,y,w,h] = cv2.boundingRect(cnt)
        if  h>28:
            cv2.rectangle(im,(x,y),(x+w,y+h),(0,255,0),2)
            roi = thresh[y:y+h,x:x+w]
            roismall = cv2.resize(roi,(10,10))
            roismall = roismall.reshape((1,100))
            roismall = np.float32(roismall)
            retval, results, neigh_resp, dists = model.find_nearest(roismall, k = 1)
            tamilCode = (results[0][0]).round(1)
            print tamilCode,
            try:
                tamil = digit_to_letter[tamilCode]
                print tamil
                cv2.putText(out,tamil,(x+100,y),0,1,(0,255,0))
            except:
                cv2.putText(out,'thu',(x+100,y),0,1,(0,255,0))

cv2.imshow('im',im)
cv2.imshow('out',out)
cv2.waitKey(0)
