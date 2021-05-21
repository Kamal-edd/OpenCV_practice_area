import cv2
#import numpy as np

#Task 1. Read Image & Show Output of the Image

#Code

"""
image1 = cv2.imread(r"vegita.png", 1)
cv2.imshow("image1", image1) 
cv2.waitKey()

image2 = cv2.imread(r"vegita.png", 2)
cv2.imshow("image2", image2) 
cv2.waitKey()


image0 = cv2.imread(r"vegita.png", 0)
cv2.imshow("image0", image0) 
cv2.waitKey()

image4 = cv2.imread(r"vegita.png", 4)
cv2.imshow("image4", image4) 
cv2.waitKey()
"""
image4 = cv2.imread(r"vegita.png", cv2.IMREAD_UNCHANGED)
cv2.imshow("image4", image4) 

if cv2.waitKey(5000) == ord("q"):	
	cv2.destroyAllWindows()
else:
	cv2.waitKey(10000) #10000ms = 10 s maybe

"""
imread = [i for i in vars(cv2) if "IMREAD" in i]
#output
print(imread)
['IMREAD_ANYCOLOR', 'IMREAD_ANYDEPTH', 'IMREAD_COLOR',
 'IMREAD_GRAYSCALE', 'IMREAD_IGNORE_ORIENTATION',
 'IMREAD_LOAD_GDAL', 'IMREAD_REDUCED_COLOR_2', 
 'IMREAD_REDUCED_COLOR_4', 'IMREAD_REDUCED_COLOR_8', 
 'IMREAD_REDUCED_GRAYSCALE_2',  'IMREAD_REDUCED_GRAYSCALE_4',
 'IMREAD_REDUCED_GRAYSCALE_8', 'IMREAD_UNCHANGED']
"""

cv2.destroyAllWindows()