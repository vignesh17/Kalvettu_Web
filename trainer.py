# Based on http://stackoverflow.com/a/9620295/3638128

from dictionary import digit_to_letter, letter_to_digit
import sys

import numpy as np
import cv2

for number in range(0, 11):
	filename =  '7.jpg'
	print 'Opening %s' % filename
	im = cv2.imread('samples/' + filename)
	im2 = im.copy()


	gray = cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
	blur = cv2.GaussianBlur(gray,(5,5),0)
	thresh = cv2.adaptiveThreshold(blur,255,1,1,11,2)

	contours,hierarchy = cv2.findContours(thresh,cv2.RETR_LIST,cv2.CHAIN_APPROX_SIMPLE)

	samples =  np.empty((0,100))
	responses = []
	keys = [i for i in range(48, 58)]

	for cnt in contours:
	    if cv2.contourArea(cnt) > 50:
	        [x,y,w,h] = cv2.boundingRect(cnt)
	        im = cv2.imread('samples/' + filename)

	        if h > 20:
	            cv2.rectangle(im,(x,y),(x+w,y+h),(0,0,255),2)
	            roi = thresh[y:y+h,x:x+w]
	            roismall = cv2.resize(roi,(10,10))
	            cv2.imshow('norm',im)    
	            key = cv2.waitKey(0)
	            key = raw_input('Enter...')
	            if key == 27:  # (escape to quit)
	                sys.exit()
	            else:
	                key = letter_to_digit[key]
	                responses.append(float(key))
	                sample = roismall.reshape((1,100))
	                samples = np.append(samples,sample,0)
	                im = im2
	            

	responses = np.array(responses,np.float32)
	responses = responses.reshape((responses.size,1))
	print "training complete"

	s = raw_input('save?')
	if (s == 'y'): 
	    with open('generalsamples.data', 'a') as file:
	        np.savetxt(file, samples)
	        
	    with open('generalresponses.data', 'a') as file:
	        np.savetxt(file, responses)
	else:
	    pass
	break
