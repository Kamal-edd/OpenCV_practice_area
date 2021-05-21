import cv2


image = cv2.imread(r"vegita.png",0)

#Task 6. Resize the Image

image = cv2.resize(image, (300,600)) #resizing method/function
cv2.imshow("IMAGE",image)

cv2.waitKey()
cv2.destroyAllWindows()