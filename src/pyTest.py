import sys
import keyword
# print(sys.version)

def sum():
    global a
    a = 10
    b = 20
    c = a + b
    print(c)

sum()
print(a)

list = [1,2,3,4,5,6]
list2 = ["ngo","minh","duc"]

for i in list2:
    print("Value: ",i)
    print("Index: ",list2.index(i))

dictionary = {
    1: 'ngo',
    2: '22'
}



print (dictionary.keys())    
# print("1st index: ",list2.index("ngo"))

set2 = {'James', 2, 3,'Python'}  
  
#Printing Set value  
print(set2)

print("keyword set: ", keyword.kwlist)
help("keywords")  

student = {
    "name":"Duc",
    "class": "23ce1",
    "age": 22
}

print(student["class"])

list3 = ["a","b","c","d","e","f"]

def forEach(array):
    for i in array:
        print(array.index(i)," : ",i)

forEach(list3)



def maps(cb,list):
    for i in list:
        print(i)
        cb(i)

def func(item):
    return item + " helo"

list4 = maps(func, list3)

for i in list4:
        print(i)
        