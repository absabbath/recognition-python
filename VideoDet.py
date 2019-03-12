import cv2, time
from tkinter import *

window=Tk()	

def videoFaceDet():

	video = cv2.VideoCapture("cam.wmv")
	# Trainign
	faceCascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

	#Puntos para crear rectangulo a analizar
	upper_left = (30, 80)
	bottom_right = (300, 300)

	while True:
		
		# Lectura del video
		check, frame = video.read()
		
		#Parte del video a analizar
		fr = frame[upper_left[1] : bottom_right[1], upper_left[0] : bottom_right[0]]

		#Grayscale conversion of the frame
		grayImg=cv2.cvtColor(fr,cv2.COLOR_BGR2GRAY)
		
		## Scale  Cascade Classifiers factor: aqui se ajusta la presicion con la que se analizan las imagenes
		faces=faceCascade.detectMultiScale(grayImg, scaleFactor=1.05, minNeighbors=3)
		
		#detect faces and draw rentangle
		cv2.rectangle(frame, (upper_left[0], upper_left[1]), (bottom_right[0], bottom_right[1]), (255,0,0), 2)
		for x, y, w, h in faces:
			fr=cv2.rectangle(fr, (x,y), (x+w, y+h), (0,255,0), 2)
			

		font = cv2.FONT_HERSHEY_SIMPLEX
		cv2.putText(fr,'Rostros '+str(len(faces)),(40,100), font, 1,(255,0,0),1,cv2.LINE_AA)

		

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