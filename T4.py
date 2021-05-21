import cv2


image = cv2.imread(r"vegita.png",1)
#cv2.imwrite("GREYvegita.png", image)


image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
cv2.imshow("Image",image)
cv2.waitKey()
cv2.destroyAllWindows()




"""
colors = [i for i in vars(cv2) if "COLOR_BAYER" in i]
#output
print(colors)
['COLOR_BAYER_BG2BGR', 'COLOR_BAYER_BG2BGRA', 
'COLOR_BAYER_BG2BGR_EA', 'COLOR_BAYER_BG2BGR_VNG', 
'COLOR_BAYER_BG2GRAY', 'COLOR_BAYER_BG2RGB', 
'COLOR_BAYER_BG2RGBA', 'COLOR_BAYER_BG2RGB_EA', 
'COLOR_BAYER_BG2RGB_VNG', 'COLOR_BAYER_GB2BGR', 
'COLOR_BAYER_GB2BGRA', 'COLOR_BAYER_GB2BGR_EA', 
'COLOR_BAYER_GB2BGR_VNG', 'COLOR_BAYER_GB2GRAY', 
'COLOR_BAYER_GB2RGB', 'COLOR_BAYER_GB2RGBA', 
'COLOR_BAYER_GB2RGB_EA', 'COLOR_BAYER_GB2RGB_VNG', 
'COLOR_BAYER_GR2BGR', 'COLOR_BAYER_GR2BGRA', 
'COLOR_BAYER_GR2BGR_EA', 'COLOR_BAYER_GR2BGR_VNG', 
'COLOR_BAYER_GR2GRAY', 'COLOR_BAYER_GR2RGB', 
'COLOR_BAYER_GR2RGBA', 'COLOR_BAYER_GR2RGB_EA', 
'COLOR_BAYER_GR2RGB_VNG', 'COLOR_BAYER_RG2BGR', 
'COLOR_BAYER_RG2BGRA', 'COLOR_BAYER_RG2BGR_EA', 
'COLOR_BAYER_RG2BGR_VNG', 'COLOR_BAYER_RG2GRAY', 
'COLOR_BAYER_RG2RGB', 'COLOR_BAYER_RG2RGBA', 
'COLOR_BAYER_RG2RGB_EA', 'COLOR_BAYER_RG2RGB_VNG']
"""