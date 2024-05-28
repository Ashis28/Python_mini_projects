
#conditional formatting
#leap year
'''
year = int(input("Enter the year :"))
if(year % 4==0):
    if(year %100 != 0):
        print(f"{year} is a leap year")
    else:
        if(year % 400 == 0):
            print(f"{year}is a leap year")
        else:
            print(f"{year} is not a leap year")
else:
    print(f"{year} is not a leap year")'''


#for loop
'''
for x in range(1,10):
    print (x,end=" ")
for x in range(1,10,3):
    print(x,end=" ")
x = [x for x in range(1,5)]
print(x)

#multiplication table of any number
n = int(input("Enter number"))
for x in range(n,(n*10+1),n):
    print(x,end=" ")

#for loop with dictionary
print("Dictionary Iteration")
d = dict()
d['key1'] = "val1"
d['key2'] = 345
for i in d:
	print(i, d[i])

'''
#nested for loop

#Enumerate using For loop
'''
list1 = ["Data-Science","Power BI","Python"]
for index,sub in enumerate(list1):
    print(f"index:={index} , subj: {sub}")

for ind,sub in enumerate(list1,start=1):
    print(f"ind = {ind} , subj: {sub}")

#list comprehension
square = [x**2 for x in range (1,5)]
print(square)
'''

#Armstrong number
'''
def is_armstrong(num):
    str_num = str(num)
    no_dig = len(str_num)
    sum_dig = sum(int(digit) ** no_dig for digit in str_num)
    return sum_dig==num

num = int(input("Enter a number : "))
if(is_armstrong(num)):
    print(f"{num} is an Armstrong number")
else:
    print(f"{num} is not an Armstrong number")
    
'''    

#while loop
#nested while loop
"""
outer_counter = 1;
while outer_counter <= 3:
    inner_counter = 1
    while inner_counter <=2:
        print(f"outer={outer_counter} , inner={inner_counter} ")
        inner_counter+=1
    outer_counter+=1
    """

#while loop with continue statement
'''
counter =1
while counter <=5:
    if(counter==3):
        counter+=1
        continue
    print(counter,end=' ')
    counter+=1
'''
#with break statement
'''
counter =1
while counter <=5:
    if(counter==3):
        counter+=1
        break
    print(counter,end=' ')
    counter+=1
'''

#user input validation
'''
while True:
    price = int(input("Guess the min price :"))
    if(price >= 560):
        print("yes thats it")
        break
    else:
        print("Try again a bit more")
'''

#Game loops
'''
game_over = False
while not game_over:
    user_input = input("Continue playing (yes/no) ")
    if(user_input.lower() == "no"):
        game_over = True
'''

#challenge Galore
'''
Problem Statement - Create a Python program that prompts the user to enter positive numbers
continuously. The program should use a while loop to collect input data until the user enters
a non-positive number. Implement simple data validation to ensure entered values are valid
positive numbers. Finally, output the list of positive numbers entered by the user. The objec
tive is to create an interactive and error-tolerant program for collecting and handling user
input.'''

numbers =[]
while True:
    user_input = input("Enter a +ve number (Enter a -ve num to stop) :")
    if user_input.replace('.','',1).isdigit() and float(user_input)>0:
        numbers.append(float(user_input))
    elif user_input.replace('-','',1).isdigit() and float(user_input)<0:
            print([x for x in numbers])
            break
    else:
        print("Enter a valid input")

                          
