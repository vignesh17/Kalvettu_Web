import os
import cv2
import numpy as np
import matplotlib.pyplot as plt

from time import time
from datetime import datetime
from flask import Flask, request, redirect, url_for, send_from_directory, render_template, jsonify
from dictionary import digit_to_letter, letter_to_digit
from werkzeug import secure_filename


UPLOAD_FOLDER = 'static/uploads/'
OUTPUT_FOLDER = 'static/translated/'
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg'])

a = Flask(__name__)
a.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
	return '.' in filename and \
		filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS

@a.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(a.config['UPLOAD_FOLDER'],
                               filename)

@a.route('/', methods = ['GET', 'POST'])
def index():
	return render_template('index.html')

@a.route('/upload', methods = ['GET', 'POST'])
def upload_file():

	if request.method == 'POST':

		file = request.files['file']

		if file and allowed_file(file.filename):

			now = datetime.now()
			filename = now.strftime('%Y-%m-%d-%H-%M-%S') + '_' + secure_filename(file.filename) 
			file.save(os.path.join(UPLOAD_FOLDER, filename))
			
			#load image
			dir = os.curdir
			img = filename
			path = os.path.join(UPLOAD_FOLDER,img)
			print path
			print 'siva'
			raw_image = cv2.imread(path)
			print raw_image

			#######   training part    ############### 
			samples = np.loadtxt('generalsamples.data',np.float32)
			responses = np.loadtxt('generalresponses.data',np.float32)
			responses = responses.reshape((responses.size,1))

			model = cv2.KNearest()
			model.train(samples,responses)

			############################# testing part  #########################
			digit_to_letter[7.4000001] = 'thu'
			out = np.zeros(raw_image.shape,np.uint8)
			print 'sss'
			print out
			gray = cv2.cvtColor(raw_image, cv2.COLOR_BGR2GRAY)
			blur = cv2.GaussianBlur(gray,(5,5),0)
			thresh = cv2.adaptiveThreshold(blur,255,1,1,11,2)

			contours,hierarchy = cv2.findContours(thresh, cv2.RETR_LIST,cv2.CHAIN_APPROX_SIMPLE)


			############################# testing part  #########################
			for cnt in contours:
			    if cv2.contourArea(cnt)>50:
			        [x,y,w,h] = cv2.boundingRect(cnt)
			        if  h>28:
			            cv2.rectangle(raw_image,(x,y),(x+w,y+h),(0,255,0),2)
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
			                cv2.putText(out,tamil,(x, y+h),0,1,(0,255,0))
			            except:
			                cv2.putText(out,'thu',(x, y+h),0,1,(0,255,0))

			cv2.imwrite(os.path.join(OUTPUT_FOLDER, filename), out)
			
			return jsonify({
				'original': url_for('uploaded_file', filename=filename),
				'error': 0,
				'url': 'static/translated/'+filename,
			})

	else:
		return jsonify({'error': 1})

if __name__ == "__main__":
	a.run(debug=True, host='0.0.0.0', port=5000)