--------------------------------------------------------------------------------------------------------------------
#program 1: print simple message 
print ("Hello world")
--------------------------------------------------------------------------------------------------------------------
#program 2: print message in different line 
print ("My name is Tarab Tausif")
print ("I'm 19 years old")
--------------------------------------------------------------------------------------------------------------------
#program 3: print message in same line 
print ("I live in India.","I'm persuing B.Tech CSE")
--------------------------------------------------------------------------------------------------------------------
#program 4: printing of numbers 
print (23) #you don't have to put those commas while printing number 
print (23+48) #this line will print 71
--------------------------------------------------------------------------------------------------------------------
#program 5: defining variables 
name = "Tarab" #string
age = 19 #integer(int)
price = 60.57 #float

print (name)
print (age)
print (price)
--------------------------------------------------------------------------------------------------------------------
#program 6: printing variables in sentence 
name = "Tarab"
age = 19
price = 60.57
age2 = age 

print ("my name is:",name,".")
print ("I'm",age,"years old.")
print ("price of that book is:",price,".") #this line will print: price of that book is 60.57.
print (age2) #this line will print 19
--------------------------------------------------------------------------------------------------------------------
#program 7: printing of data type assigned to varibles
name = "Tarab"
age = 19
price = 59.88
old = False 
a = None


print (type(name)) #this line result in <class 'str'>
print (type(age)) #this line result in <class 'int'>
print (type(price)) #this line result in <class 'float'>
print (type(old)) #this line results in <class 'bool'>
print (type(a)) #this line results in <class 'None type'>
--------------------------------------------------------------------------------------------------------------------
#program 8: Data type (string)
name = 'Tarab'
name1 = "Tarab"
name2 = '''Tarab'''

print (name)
print (name1)
print (name2)
--------------------------------------------------------------------------------------------------------------------
#program 9: OPERATORS
# arithmetic operators 
a = 4 
b = 2

print (a+b) #6
print (a-b) #2
print (a*b) #8
print (a/b) #2.0
print (a%b) #(modulu for remainder) =>0
print (a**b) #(power operator) a^b =>16
--------------------------------------------------------------------------------------------------------------------
#program 10: OPERATORS 
# relational operators 
a = 50
b = 20

print (a == b) #False
print (a != b) #True
print (a >= b) #True 
print (a > b) #True
print (a <= b) #False
print (a < b) #False
--------------------------------------------------------------------------------------------------------------------
#program 11: OPERATORS 
#assignment operators 
num = 10
num = num + 10 # 10+10=20
num += 10 #20
num -= 10 #0
num *= 10 #100
num /= 5 #2
num %= 5 #0
num **= 5 #1,00,000
print ("num:",num)
--------------------------------------------------------------------------------------------------------------------
#program 12: OPERATORS 
#logical operators
a = 50
b = 30
print (not False) #True
print (not (a>b)) #False

val1 = True 
val2 = True 
print ("AND operator:", val1 and val2) #True
print ("OR operator:", val1 or val2) #True

val1 = False
val2 = True
print ("AND operator:", val1 and val2) #False
print ("OR operator:", a==b or a>b) #True

val1 = False
val2 = False
print ("AND operator:", val1 and val2) #False
print ("OR operator:", val1 or val2) #False
--------------------------------------------------------------------------------------------------------------------
#program 13: Type conversion 
a = 2
b = 4.25

sum = a + b #python will convert int to superior value i.e. float => 2.0+4.25
print (sum) # implicit conversion 
--------------------------------------------------------------------------------------------------------------------
#program 14: type casting 
a = int("2")
b = 4.25

print (type(a))
print (a+b)
--------------------------------------------------------------------------------------------------------------------
#program 15: input in python 
name = input ("enter your name:")
print ("welcome",name) 
print (type(name),name) #type will be string string always weather it'll float/int,so here we need type casting

int ("5")
val = int (input ("enter some value:"))
print (type(val),val)
--------------------------------------------------------------------------------------------------------------------





















































