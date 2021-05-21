import cv2
#Task 3. To Read Videos

#We will use:

#To use cam or read the video
cam = cv2.VideoCapture(r"Orewa_Super_Vegeta.mp4")  
while True:
	ret, frame = cam.read()
	#it will read the cam response/feed
	cv2.imshow("F",frame)   
	if cv2.waitKey(17) == ord("q"):
		break
cam.release() 
#it will release the camera
cv2.destroyAllWindows()