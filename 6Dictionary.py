#29-05-2024

#initialize a dictionary
dict = {1:"Ashis",2:"Archana",3:"Laksh",4:"lamin",2:"Ayushi"}
print(dict)
#it dont allow duplicasy of key if present the latest will taken

#access the element
print(dict[1])
print(dict.get(3))

#add , update and del value
'''
dict[5]="varun"
print(dict)
dict[5]="Arpit"
print(dict)
del dict[5]
print(dict)

#clear
dict.clear()
print(dict)
'''
#find all keys
'''
dict = {1:"Apple",2:"orange",4:"Pineapple",3:"avocardo"}
print(dict.keys())
print(dict.values())
print(dict)

#iterate over for loop
for x in dict.keys():
    print(dict.get(x),end=" ")
print("-"*5)
print(dict.items())

print(dict.get(1))
print(dict.get(10,'unknown'))

for x in dict.items():
    print(x)

for k,v in dict.items():
    print(k,v)

#check if key is present or not
print(1 in dict)
print('1' in dict)
'''
#append or merge multiple dict
#update a dictionary
dct_1 = {1:'A', 2:'B' , 3:'C'}
dct_2 = {1:'a', 2:'b' , 3:'c'}

dct_1.update(dct_2)
#
print(dct_2)

#iterating through a dictionary
'''
my_dict = {'name':'Rose','age':24, 'gender':'Female'}
for key in my_dict:
    print(key, end=' ')
print('\n')
# Iterating through values
for value in my_dict.values():
    print(value, end=' ')
print('\n')
# Iterating through key-value pairs
for key, value in my_dict.items():
    print(key, value, end = ' ')
    '''

#dictionary methods;
#1. dict.clear()  2.dict.copy() 3.dict.get(key,default="none") 4.dict.items()
#5. dict.keys()   6.dict.update(dict2)  7.dict.values()  8.pop()  9.popItem()
#10 dict.setdefault(key,default="none")  11.ict.has_key(key)
#12 dict.get(key,default = "none")
