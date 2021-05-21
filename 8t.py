import numpy as np
import cv2

#Task 7. Create Blank Black/White Image using numpy

image1 = cv2.imread(r"vegita.png", 1)
image2 = cv2.imread(r"vegita.png", 1)

cv2.imshow("White Image",image1)
cv2.imshow("Black Image", image2)
"""
cv2.imwrite("White Image.png",image1)
cv2.imwrite("Black Image.png", image2)
"""
#Task 8. How to Add Two Images together using the Add function



#Need to set the same size for both loaded images.
#Both images size should be the same before using the add method
#image1 = cv2.resize(image1, (250,250))
#image2 = cv2.resize(image2, (250,250))

#add method
"""												addedImage = cv2.add(image1, image2)
												cv2.imshow("Added Image", addedImage)
									
												cv2.waitKey()
												cv2.destroyAllWindows()
									"""

#Task 9. How to add two together using the cv2.addWeighted method

#Code:


#Need to set the same size for both loaded images.
#Both images size should be the same before using the add method
#image1 = cv2.resize(image1, (250,250))
#image2 = cv2.resize(image2, (250,250))

#add method
addedImage = cv2.addWeighted(image1, 0.8, image2, 0.2, 0)
cv2.imshow("Added Image", addedImage)

cv2.waitKey()
cv2.destroyAllWindows()