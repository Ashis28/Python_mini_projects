#1/june/2024
dict = {1 : {'name' : 'ashis','ph_no' : 123},
        2 : {'name' : 'arpit','ph_no' : 456},
        3 : {'name' : 'muskan','ph_no' : 789} }

#accessin elements from multidimDict
'''
print(dict[1])
print(dict[2]['name'])
print(dict[3]['name'],dict[3]['ph_no'])
'''

#adding , updating , deleting elements
'''
#update
dict[1]['name'] = 'Varun'
#add
dict[4] = {'name':'Vansh' , 'ph_no':101112}
print(dict)
#delete
del dict[4]
print(dict)
'''

#iteration
'''
for i in dict.keys():
    print(i,dict[i]['name'],dict[i]['ph_no'])
'''

#going a level deeper
dct = {1 : {'name' : 'ashis','ph_no' : 123,'marks':{'eng':20,'geo':22,'sci':25}},
        2 : {'name' : 'arpit','ph_no' : 456,'marks':{'eng':22,'geo':20,'sci':15}},
        3 : {'name' : 'muskan','ph_no' : 789,'marks':{'eng':18,'geo':28,'sci':22}} }

#iterating
'''
for i in dct.keys():
    for j in dct[i].keys():
        print(dct[i][j])
#print name and marks
for i in dct.keys():
    print(i , dct[i]['name'], dct[i]['marks'])
#print marks of science
for i in dct.keys():
    print(dct[i]['name'],dct[i]['marks']['sci'])
'''

#try again (practise_5 added also))
'''
def count_word_freq_from_corpus(corpus):
    word_freq = {}
    for sentence in corpus:
        words = sentence.split()
        for word in words:
            if word in word_freq:
                word_freq[word]['total_count']+=1
                if sentence in word_freq[word]['documents']:
                    word_freq[word]['documents'][sentence]+=1
                else:
                    word_freq[word]['documents'][sentence] = 1
            else:
                word_freq[word] = {'total_count' :1 ,'documents': {sentence:1}}
    return word_freq

corpus = [
    "This is the multidimensional dictionary.",
    "This dictionary stores the sub dictionary.",
    "And this is the third containing the word and count.",
    "Is this the first level of dictionary?"
]
word_frequencies = count_word_freq_from_corpus(corpus)

# Displaying word frequencies
for word, info in word_frequencies.items():
    print(f"Word: {word}")
    print(f"  Total Count: {info['total_count']}")
    print("  Document Occurrences:")
    for document, count in info['documents'].items():
        print(f"    {document}: {count}")
    print()
'''

#dictionary comprehension

dic = {i:i**2 for i in range(1,7) if i%2==0}
print(dic)

#alist to dictionary
ls = ['apple','banana','orange']
dic = {fruits:len(fruits) for fruits in ls}
print(dic)

#separate key with strigs
dic = {'num_'+str(i) : i for i in range(1,7)}
print(dic)
dic = {k:v for k,v in dic.items() if v%3==0 }
print(dic)

ls1 = ['a','b','c','d']
ls2 = [1,2,3,4,5]
dic = {ls1[i]:ls2[i] for i in range(0,len(ls1))}

keys = ['a', 'b', 'c']
values = [1, 2, 3]
result = {k: v for k, v in zip(keys, values)}
print(result)

#nested dictionary comprehenssion
dictionary = {
    k1: {k2: k1 * k2 for k2 in range(2, 6)} for k1 in range(5, 7)
}
print(dictionary)


#not understood
def find_common_elements(lists):
    common_elements = {element: min(lst.count(element) for lst in lists) for element in set.intersection(*map(set, lists))}
    return common_elements

list1 = [1, 2, 2, 3, 4]
list2 = [2, 3, 4, 4, 5]
list3 = [3, 4, 5, 5, 6]

result = find_common_elements([list1, list2, list3])

for element, frequency in result.items():
    print(f"Element: {element}, Frequency: {frequency}")

print(dic)

matrix = [[1,2,3],[4,5,6],[7,8,9]]  #rem it'a list
dic = {(i,j):matrix[i][j] for i in range(3) for j in range(3) }
print(dic)
