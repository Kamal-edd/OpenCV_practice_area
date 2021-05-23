import numpy as np
import cv2
###################
#Task 7. Create Blank Black/White Image using numpy

white_img = np.ones((512,512,3), dtype=np.uint8) * 255
black_img = np.ones((512,512,3), dtype=np.uint8) * 0
cv2.imshow("White Image",white_img)
cv2.imshow("Black Image", black_img)
cv2.waitKey()
cv2.destroyAllWindows()