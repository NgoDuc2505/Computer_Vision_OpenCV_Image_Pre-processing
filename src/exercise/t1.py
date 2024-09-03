import cv2 as c

try:
    # img1 = c.imread('CV\src\exercise\image\meme2.png')
    # img2 = c.imread('CV\src\exercise\image\hwimg.webp')
    savePath = "image\savedImg.png"
    img1 = c.imread('image\meme.png')
    img2 = c.imread('image\meme3.png')
    img3 = c.imread('image\glare.jpg')
    img4 = c.imread('image\glare2.jpg')
    img5 = c.imread(f'{savePath}')
    img6 = c.imread('image\glare3.jpg')
    weightedImg = c.addWeighted(img1,0.5,img2,0.4,0)
    sub = c.subtract(img4,img3)
    sub2 = c.subtract(img4,img5)
    bitwise = c.bitwise_not(img6,img5, mask= None)
    c.imshow("Image",sub2)
    c.waitKey()
    # if(c.imread(savePath)):
    #     pass
    # else:
    #     c.imwrite(savePath,sub)
except Exception as e:
    print(e)


