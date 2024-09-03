
import numpy as np
import cv2 as c


savePath = "image\savedImg.png"
img5 = c.imread(f'{savePath}')

def isEqual(thresh, val):
    for i in range(thresh):
        if(val == i):
            return True
    return False

THRESH = 100
def rendomize(img: c.typing.MatLike):
    (row, col) = img.shape
    for i in range(row):
        for j in range(col):
            arrayBufferSpot = img[i,j]
            if(isEqual(THRESH,arrayBufferSpot)):
                print("arrayBuffer: ", arrayBufferSpot)
                img[i,j] = 0
                # pass
            else:
                img[i,j] = 255
                pass


img = c.imread("image\glare.jpg")
kernel = np.ones((5, 5), np.uint16) 
imgErcode = c.erode(img5,kernel)
gray = c.cvtColor(imgErcode, c.COLOR_BGR2GRAY)
rendomize(gray)
c.imshow("show", gray)
c.waitKey()