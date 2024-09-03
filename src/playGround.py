from imgLoader import loader

imgPath = "D:/PersonProject/Project_with_Py/CV/src/imgSrc/meme.png"

def runImg():
    img = loader(imgPath)
    img.show()

runImg()
