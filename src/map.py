def maps(func, list):
    listResult = []
    for i in list:
        listResult.append(func(i))
    return listResult

# def callback(item):
#     print(item)
#     return item + " ||| "

listItem = ["a","b","c","d","e","f","g"]

listMain = maps(lambda item: item + " |_| ", listItem)
# for i in listMain:
#     print("Key: ",i)
print(listMain)
print("all: ",all(listMain))
k = [1, 3, 7, 0]  
print(all(k))  
k2 = [0, False, 5]  
print(all(k2))  

dec = 10
print("Bin: ",bin(dec))
print("Hex: ",hex(dec))
binVal = 0b1010 << 1
binShifLeft = 0b10100
print("Dec: ",binVal)
print("Dec2: ",binShifLeft)

# vietnamese = "ngô minh đức"
# print(ascii(vietnamese))
# print('ng\xf4 minh \u0111\u1ee9c')
# print(vietnamese)

def spreadPram(*spread):
    castedList = list(spread)
    castedList.append("top")
    print(castedList)

spreadPram("hi","hello","ngo")