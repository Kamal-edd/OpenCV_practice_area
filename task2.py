import cv2
#import numpy as np

#Task 2. To save/write the image in the system

#We will use:

#Code:
image = cv2.imread(r"vegita.png", cv2.IMREAD_GRAYSCALE)
cv2.imwrite("GREYvegita.png", image)

"""
In the first argument, we give a filename with an image extension. Extensions can be:

    jpg
    png
    jpeg
    tiff

You can also specify the full path to store the image at a different location but must add the r prefix.

Example: r”C:/scripts/filename.png”

The second argument is the image (variable of the image) that you want to save in the system.
"""