str1= "this is a string.\nwe are creating it in python."
print(str1)
str2= "this is a string.\twe are creating it in python."
print(str2)
str3= "uditi"
str4= "agrawal"
print(str3+str4)#### concatenation combine 2 seprate string (uditiagrawal)
print(len(str3))### leanth of string (5)
print(str3[2])#### indexing it start from 0 (i)
print(str3[1:3]) ##### slicing (di)
print(str3[ :5]) ##### slicing
print(str3[-5:])##### slicing
print(str3.endswith("ti")) ### string function 
print (str3.capitalize())  ### string function 
print(str3.replace("i","o"))  ### string function 
print(str3.find("i"))  ### string function 
print(str3.count("i")) ### string function 
Name= input("first name:")### practics
print(len(Name)) ### practics
str5= "my name  is $$$$" ### practics 
print(str5.count("$"))### practics
marks= int(input("enter marks")) #### conditional statement
if(marks>= 90):
    grade = "A"
elif(marks>=80 and marks<90):
    grade = "B"
elif(marks>=70 and marks<80):
    grade = "C"
else:
    grade = "D"
print("grade of the student->", grade)
age= int(input("enter the age:"))  ### Nesting
if(age>=18):
    if(age>=80):
        print("cannot drive")
    else:
        print("can drive")
else:
    print("cannot drive")

number= int(input("enter first number"))
if(number%2==0):
    print("even")
else:
    print("odd")
a= 4
b= 5
c= 7
if(a>b and a>c):
    print("greatest")  
number
if(number%2==0):
    print("even")
else:
    print("odd")
