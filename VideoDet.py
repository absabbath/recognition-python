import cv2, time
from tkinter import *

window=Tk()	

def videoFaceDet():

	video = cv2.VideoCapture("cam.wmv")
	# Trainign
	faceCascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

	while True:
		
		check, frame = video.read()
		
		#Grayscale conversion of the frame
		grayImg=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
		
		## Scale  Cascade Classifiers factor
		faces=faceCascade.detectMultiScale(grayImg, scaleFactor=1.05, minNeighbors=5)
		
		#detect faces and draw rentangle
		cv2.rectangle(frame, (100, 100), (600, 400), (255,0,0), 2)
		for x, y, w, h in faces:
			frame=cv2.rectangle(frame, (x,y), (x+w, y+h), (0,255,0), 3)
			

		font = cv2.FONT_HERSHEY_SIMPLEX
		cv2.putText(frame,'Rostros '+str(len(faces)),(10,500), font, 2,(255,0,0),3,cv2.LINE_AA)

		cv2.imshow("Video", frame)

		#exit press q
		key=cv2.waitKey(1)
		if key==ord('q'):
			break
	
	#Close video window
	cv2.destroyAllWindows()
	video.release()

b1=Button(window, text="Iniciar", command=videoFaceDet, bg="blue")
b1.grid(row=0, column=0)

#GUI widget label
l1=Label(window, text="Presiona q para detener analisis")
l1.grid(row=0, column=1)

window.mainloop()