#INTRO , DATA TYPES , OPERATORS , TYPECASTRING , STRING , VARIABLES

print("Hello world")  #27-05-2024 gfg data Science and ai course


#2 Data types
"""
# int
print(1000)
print(-10)
print(type(29))

#float
print(0.0)
print(-4.0)
print(type(1.0))

#string
print("A")
print('a')
print('abcd efg')
print(type('b'))

#Boolean
print(True)
print(type(True))
print(type("True"))

#functionalities in printing
print('a',"b",1.0,-3)
#end to print in same line
print("hii",end=' ')
print("how are",end='-')
print("you")
#separator
print("a","b","c ",end = "*")
print("hello","world",1,sep="|")
"""

#3 operators
#1. ARITHMATIC  2.COMPARISON  3.LOGICAL 
"""
print(True+True)
print("string"+"Concatination")
print(3/5)
#floor division
print(32.453//7)    #4.0
#modulo (to get he reminder)
print(32.453%7)
#abs to make -ve to +ve , round , pow ->
print(abs(-43.2))
print(round(32.453/7,2))
print(pow(2,5))

#2 comparison operator
print("Ash"=="ash")
print(1.0==1)
print(True == 1)

"""

#4 TypeCasting
"""
#int
print(int(3.1323))
print(int(True))
print(int("100"))
#print(int(" 10 10 ")) #error bcz it take one int inside string to convert

#float
print(float(13))
print(float(False))
print(float("  10  "))

#String
print(str(10))
print(str(-4.3))
print(str(True))

#boolean
print(bool(1))
print(bool(0))
print(bool(""))
print(bool("abc"))
print(bool(0.0))

#for 2 step convertion directly it give error
#print(int("3.14"))
print(int(float("3.14")))
"""

#5 String
"""
#1 concat
print("Hello"+" "+"World")
#2 replicate
print("Ab" * 5)
#3 length
print(len("world length"))

#4 string slicing
print("Ashish Jangra"[0])
#(String index is 0 from left (0 : len-1) and index is -1 from ri8 (len to -1)
print("Ashish Jangra"[0:len("Ashish Jangra")-1])  #Ashish Jangr
print("Ashish Jangra"[0:])
print("Ashish"[-2]) #s
print("Ashish Jangra"[-10:-1]) #ish Jangr

#print("Ashish Jangra"[-1:-10]) #error not possible
print("Ashish Jangra"[:-1])  #Ashish Jangr
print("Ashish Jangra"[-14: ]) #Ashish Jangra

#5 Case conversion
print("Ashis".upper())
print("Ashis".lower())
#6 Stripping - (removing extra spaces)
print("  ashi s     ".strip())  #it dont remove inbetween spaces

#6 replace
print("Ashish Jangra".replace('sh','-'))

#7 count
print("Ashish Jangra".count('A'))
print("Ashish Jangra".lower().count('a'))

#8 find
print("Ashish Jangra".find('h'))  #2
print("Ashish Jangra".find('h ')) #5

#9 Strign Check
print("alphabets".isalpha())
print("123".isdigit())
print('lowercase'.islower())
print('UPPER'.isupper())

#10 capitalize , title
print('hello world'.capitalize())  #1st letter becomes capital
print('hello world'.title())

#11 starts with and endswith
print("Ravindra Jadeja".startswith('Rav'))
print('M Dhoni'.endswith('ni'))

#12  center,ljust,rjust
print('Ashis Jangra'.center(22,'*'))
print('Ashis Jangra'.ljust(22,'*'))
print('Ashis Jangra'.rjust(22,'*'))
"""

#6 variables
"""
x=y=z =0
print(x,y,z)

a,b,c,d = 1,2,3,4
print(a,b,c,d)

data = [11,12,13,14]
a,b,c,d = data
print(a,b,c,d)
print(data)

#taking input
n = input()
print(type(n))

n=input("Enter first number: ")
print(n)

#typecast string input to int
n = int(input("Enter num: "))
print(type(n))
"""
s="Hello"
print(s.replace(s[0],s[0].upper()),"\n",s.upper())
