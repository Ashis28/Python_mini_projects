# LIST |  TUPLE  |  SET  | DICTIONARY
# 28-05-2024

#https://youtu.be/R-HLU9Fl5ug?si=ONCgH5PxjoXWLK7c
#source --  w3 school

"""
1.List - ordered & mutable
2.Tuple - ordered & immutable
3.Set - No duplicate and mutable & unordered
4.dict - Collection of data in key value pairs

-> Sequences (String,List,Tuple)
"""

#1ist intro
"""
list1=[]
print(type(list1))
list1=["apple",10,"C",-3.2]
print(list1)

#list() function
thelist = list(("apple","orange","banana"))
print(thelist)

#access items in list
list1[1]

#chagne item value in list
list1[1] = "orange"
print(list1)

thislist = ["apple", "banana", "cherry"]
thislist[1:2] = ["blackcurrant", "waterelon"]
print(thislist)
"""

#add items in the list
"""
#append
list1.append("orange")
print(list1)
#insert
list1.insert(2,"kiwi")
print(list1)
#extend   - combine two list
list2 = ["mango","papaya"]
list1.extend(list2)
print(list1)
#extend can also add tuple also
tup1 = ("kiwi","cherry")
list1.extend(tup1)
print(list1)
"""
#removing elements from list
"""
#remove()  - it remove the first occurance
list1.remove("kiwi")
print(list1)
#pop() - if index not given it remove the last item
list1.pop()
print(list1)
list1.pop(2)
print(list1)
#del keyword
del list1[2]
print(list1)
#delete whole list
del list1
#print(list1)
#clear - empty the list
print(list2)
list2.clear()
print(list2)
"""

#loops in list
"""
for i in thelist:
    print(i)
print("-"*5)

for i in range(len(list1)):
    print(list1[i])
#looping using list comprehension    
[print(x) for x in list1]
"""

#list comprehension
"""
fruits = list(("apple","banana","cherry","kiwi","mango"))
print(fruits)

mylist =[]
for x in fruits:
    if 'a' in x:
        mylist.append(x)
print(mylist)

mylist =[]
mylist = [x for x in fruits if "a" in x]
print(mylist)

numlist = []
numlist = [x for x in range(10) if x<5]
print(numlist)

mylist =[]
mylist = [x if x!="banana" else "orange" for x in fruits]
print(mylist)
"""

#sort in lists
'''
thelist = ["orange","mango","apple","kiwi","banana"]
thelist.sort()
print(thelist)

numlist = [10,29,40,8,20,10]
numlist.sort()
print(numlist)
numlist.sort(reverse=True)
print(numlist)

#customize sort function
#print he number how close is it to 50
def myfun(n):
    return abs(n-50)
numlist = [100,50,65,82,23]
numlist.sort(key = myfun)
print(numlist)

#case insensative sort
thelist = ["orange","mango","apple","Kiwi","Banana"]
thelist.sort()
print(thelist)
thelist.sort(key = str.lower)
print(thelist)

#reverse
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.reverse()
print(thislist)
'''

#copy a list
"""
#copy()
thelist = ["apple","banana",50,10]
mylist = thelist.copy()
print(mylist)

#list() method
list1 = ["ece","cse",7,20]
list2 = list(list1)
print(list2)
"""

#some methods
#count()
points = [1, 4, 2, 9, 7, 8, 9, 3, 1]
x = points.count(9)
print(x)
