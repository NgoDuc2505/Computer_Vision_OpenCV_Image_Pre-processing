
from ownLib import *
import cv2 as c



thresholdLevel = {
    "SOFT" : 100,
    "MED" : 50,
    "HARD" : 10,
    "S_HARD" : 5
}

testPath = "image\homeGlare.jpg"

# img = sepLightSource("image\carGlare2.webp")
# img = sepLightSource("image\carGlare3.jpeg")
homeImg = c.imread(testPath)
resizedImg = c.resize(homeImg,(0,0),fx= 0.2, fy=0.2)
imgSepHomeGlare = sepLightImg(resizedImg)
grayHomeGlare = grayScaleImg(imgSepHomeGlare)
result2 = lightSourceSeparator(grayHomeGlare,thresholdLevel["S_HARD"])

img = sepLightSource("image\carGlare2.webp")
gray = grayScaleImg(img)
result = lightSourceSeparator(gray,thresholdLevel["S_HARD"])

# img = c.imread("image\glare.jpg")
# result = createPatternImg(img)
c.imshow("test",result2)
# c.imshow("test",result)
c.waitKey()
