import cv2 as c

def createPatternImg(imgSrc: c.typing.MatLike):
    pattern = imgSrc.copy()
    (row, col, part) = pattern.shape
    for i in range(row):
        for j in range(col):
            pattern[i,j] = [255,255,255]
    return pattern

def sepLightSource(path: str):
    PATTERN_WHITE = "image/glare2.jpg"
    imgOrin = c.imread(path,1)
    # imgPatt = c.imread(PATTERN_WHITE, 1)
    imgPatt = createPatternImg(imgOrin)
    # subImg = c.subtract(imgOrin,imgPatt)
    subImg = c.subtract(imgPatt,imgOrin)
    return subImg

def sepLightImg(img: c.typing.MatLike):
    imgPatt = createPatternImg(img)
    subImg = c.subtract(imgPatt,img)
    return subImg


def grayScaleImg(img: c.typing.MatLike):
    return c.cvtColor(img, c.COLOR_BGR2GRAY)

def grayScaleImgPath(path: str):
    img = c.imread(path,1)
    return c.cvtColor(img, c.COLOR_BGR2GRAY)

def isEqual(thresh, val):
    for i in range(thresh):
        if(val == i):
            return True
    return False

def isEqualRange(start, end, val):
    for i in range(start, end):
        if(val == i):
            return True
    return False


def lightSourceSeparator(imgInGray: c.typing.MatLike, threshold: int):
    (row, col) = imgInGray.shape
    for i in range(row):
        for j in range(col):
            spot = imgInGray[i,j]
            if(isEqual(threshold, spot)):
                imgInGray[i,j] = 0
            elif(isEqualRange(threshold+1,50,spot)):
                imgInGray[i,j] = 200
            elif(isEqualRange(51,70,spot)):
                imgInGray[i,j] = 230
            elif(isEqualRange(71,150,spot)):
                imgInGray[i,j] = 245
            else:
                imgInGray[i,j] = 255
    return imgInGray