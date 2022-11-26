def roman_numbers(num):
    if num>3999:
        print("Enter a number less then 3999!")
        return
    value=[1000,900,500,400,100,90,50,40,10,9,5,4,1]
    symbol=["M","CM","D","CD","C","XC","L","XL","X","IX","V","IV","I"]
    roman=""
    i=0
    while num>0:
        div=num//value[i]
        num=num%value[i]
        while div:
            roman=roman+symbol[i]
            div=div-1
        i+=1
    return roman


num=int(input("Enter an integer number:"))
print("roman numerals of",num,"is:",roman_numbers(num))

#PROJECT no-17
#CONVERTER TO CONVERT GIVEN ROMAN TO INTEGER:-->
'''
ROLL NO.:-   NAME:-              REG.NO
32.          Ashis Kumar Dash    12213968
38.          Himanshu Kumar      12214259
48.          Babul Kumar         12213016
'''
