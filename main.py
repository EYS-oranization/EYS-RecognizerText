from PIL import Image
import pytesseract
import cv2
import os
import datetime
from time import sleep

# pytesseract.pytesseract.tesseract_cmd = 

cam1 = cv2.VideoCapture(2)

while 1:
	frame1 = cam1.read()[1]
	gray_picture = cv2.cvtColor(frame1, cv2.COLOR_BGR2GRAY)

	now = datetime.datetime.now()
	foto_name = now.strftime('/tmp/%M%S.jpg')
	cv2.imwrite(foto_name, frame1)

	text = pytesseract.image_to_string(gray_picture, lang='rus')
		
	if text:
		print(text)
	else:
		print("Ничего не распознал")

	# sleep(0.03)


