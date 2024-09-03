from PIL import Image
a = 10
b = 20
c = a + b
print(c)
dir = 'D:\PersonProject\Project_with_Py\CV\public\image'
dirPartcularPath = dir + "\meme.png"
print(dirPartcularPath)
img1 = Image.open(dirPartcularPath)
# img1.show()
print(img1.size)
newPath =  dir + "\meme2.png"
img1.save(newPath)
img1.close()