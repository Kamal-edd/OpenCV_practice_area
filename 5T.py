import cv2


image = cv2.imread(r"vegita.png",0)
#cv2.imwrite("GREYvegita.png", image)

#Task 5. Get Image / Video Frame Size & Shape

#Code:

#image = cv2.imread("victory.png", cv2.IMREAD_COLOR)
print(image.shape(0)) #to print the shape of an image
print(image.size) #to display the size of an image