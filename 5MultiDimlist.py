#multi dimenssional list  28-05-2024
'''
lst = [[1,2,4],[4,5,6],[7,8,9]]
print(lst)
#accessing element
print(lst[0])
print(lst[0][1])

#modifying values
lst[1][1] = 9
print(lst)

lst[1] = ["ashis",122,21]
print(lst)
print(lst[1])

#slice
#access first 2 list  (Doubt)
print(lst[:2])
#print(lst[[1]]:2])

#append
lst.append([9,10,11])
print(lst)

#delete the index
del(lst[0])
del lst[2]
print(lst)

#length of the list
print(len(lst))
print(len(lst[0]))

#Reverse
lst.reverse()
print(lst)

lst = [[1,2,3],[4,5,6],[7,8,9]]
lst.reverse()
print(lst)
lst[1].reverse()
print(lst)

#access all elements of list
for i in lst:
    for j in i:
        print(j,end=" ")
    print("\n")  
'''

#list comprehension
'''
lst = [i for i in range(1,20) if i%2==0 ]
print(lst)

lst = [i*2 for i in lst]
print(lst)

#multidimlist comprehension
print([[j for i in range(1,4)] for j in range(4)])
#print(lst)

lst2 = [[1,2,3],[4,5,6],[7,8,9]]
print([j for i in lst2 for j in i] )
'''

#flattening a Multidumenssional List:
matrix = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
    ]
flattened_list = [element for i in matrix for element in i]
print(flattened_list)
#searching in a multidimenssional list
element = 5
position = [(index,row.index(element)) for index,row in enumerate(matrix) if element in row]
print(position)
