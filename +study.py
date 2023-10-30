#######

def test():
    zzz = 1 
    print(zzz)
test()

######

x='test';print(x)

######

# Python is a dynamically typed language; no need to declare the type ofthe variable. 

i=500
u=50+500
print(i) 

a='5'
b="5"
print(a+b)

#######

a = 5.0
b = 3.0 
c = (a**2+b**2)**0.5
print("c=",c) 

a = 5.0
b = 3.0 
c = (a**2+b**2)**0.5
print(f"c= {c:.2f}")

#######

x=123
y=12.34
print(x+y)
x=123
y=10.0
print(x+y)
x=10+1j
y=10.0
print(x+y)

########

'''x="test"
y=10
print(x+y)

output: error (...)
TypeError: can only concatenate str (not "int") to str
'''

#########

'''
Explicit convertions

int(x[, base])        |  converts x to an integer and x is a string

long(x[, base])       | converts x to a long and x is a string

float(x)              | converts x to a flotaing-point number

complex(real[, imag]) | creates a complex number

tuple(x)              | converts x to tuple

set(x)                | converts x to set

list(x)               | converts x to list

dict(d)               | creates a dictionary

chr(x)                | converts an integer to characther

hex(x)                | converts an integer to hexadecimal value

oct(x)                | converts an integer to octal value

'''

x = "1010"
print("string=",x)
print("conversion to int=",int(x,2))
print("conversion to float=",float(x))
print("conversion complex",complex(x))
x = 10 
print("converting hexadecimal=",hex(x))
print("converting to octal=",oct(x))
print("conversion to Ascii=",chr(x))
x='test'
print("conversion to tuple=",tuple(x))
print("conversion to set=",set(x))

x = 1E7
print(x)

z = 1e-07
print(z) # not printing 0.0000001... 

######

print(0o13)
print(0x13)

######

print("this", "is", "to", "test", sep="$")
print("python language", end="...")

######

print("this", "is", "to", "test", sep="***")
print("python language", end="---")

######

print("this", "is", "to", "test", sep="*", end="\n")
print("python language", sep="#", end="---")

######
print()
print(True>False)
print(True<False)

######

bin_number = "1101"
decimal = int(bin_number, 2)
print(decimal)

#######

bin_number = '1001'
decimal = int(bin_number, 2)
print(decimal)

#######

bin_number = 1101
octal = oct(bin_number)
print(octal)

#######

bin_number = 145 
octal = oct(bin_number)
print(octal)

#######

decimal = 123 
hexadecimal = hex(decimal)
print(hexadecimal)

#########

a, b = 10,20
print(a if a>b else b)

a, b = 10,20; print(a if a>b else b)

#########

print("%5.3e"% (123.456789))
print("%10.3e"% (123.456789))
print("%15.3e"% (123.456789))
print("%-15.3e"%(123.3456789))
print("%5.3o"% (15))
print("%x"% (15))
print("%10x"% (15))
print("%10.3x"% (15))
print("%x%%"% (15))
print("%d"% (123456789))
print("%d,"% (123456789))
print("%d, "% (123456789))
print("{0:4,d}".format(123456789))
print("{0:06d}".format(123))
print("{0:4, .5f}".format(123456789.123456789))

###

print("this     book    costs       {0:.2f} only".format(150.99))
print("this     book    costs       {0:.3f} only".format(150.99))
print("this     book    costs       {0:.0f} only".format(150.99))
print("this     book    costs       {0:e} only".format(150.99))
print("this     book    costs       {0:1} only".format(150.99))
print("this     book    costs       {0:d} only".format(150.99))
print("this     book    costs       {0:8d} only".format(150.99))
print("this     book    costs       {0:o} only".format(150.99))
print("this     book    costs       {0:b} only".format(150.99))
print("this     book    costs       {0:b} only".format(150)) #binary
print("{:d}".format(-15))
print("{:=7d}".format(-15))
print("{:=7d}".format(15))

###

'''
Function                            Description

min(x1, x2...)                 The smallest of all its arguments
max(x1, x2...)                 The largest of all its arguments 
pow(x,y)                       The value of x**y, i.e. (2**3=8) (2³=8)
round(x[,n])                   X rounded to n digits from the decimal points 
sqrt(x)                        The square root of x 
abs(x)                         The absolute value of x 
ceil(x)                        The smallest integer not less than x 
floor(x)                       The largest integer not greater than x 
exp(x)                         The exponent of x (e**x)
log(x)                         The natural logarithm of x 
log10(x)                       The base 10 logarithm of x 
fabs(x)                        The absolute value of x 

'''

import math
x,y,z=10,20,30
print("min=",min(x,y,z))
print("max=",max(x,y,z))
print("sqrt of ",x,"=",math.sqrt(x))
print("round=",round(0.5))
print("power=",pow(2,3))
f=1.5
print("ceil=",math.ceil(f))
print("floor=",math.floor(f))
x=2
print("exponent=",math.exp(x))
print("log=",math.log(x))
print("log10=",math.log10(x))
print("absolute=",abs(x))
print("absolute=",math.fabs(x))

###

import math
print("exp(5)",math.exp(5))
print("Pi",math.pi)
print("Exponent",math.e)
print("factorial(5)",math.factorial(5))
print("ceil(-5)",math.ceil(-5))
print("ceil(5)",math.ceil(5))
print("ceil(5.8)",math.ceil(5.8))
print("floor(-5)",math.floor(-5))
print("floor(5)",math.floor(5))
print("floor(5.8)",math.floor(5.8))
print("trunc(-5.43)".math.trunc(-5.43))
print("pow(3,4)".math.pow(3,4))
print("pow(3,4,5)".math.pow(3,4.5))
print("pow(math.pi,4)",math.pow(math.pi,4))
print("log(4)",math.log(4))
print("log(3,4)",math.log(3,4))
print("log(math.pi,4)",math.log(math.pi,4))
print("sqrt(8)",math.sqrt(8))

###

import cmath 
print("cmath.pi",cmath.pi)
print("cmath.e",cmath.e)
print("sqrt(4+j5)",cmath.sqrt(4+5j))
print("cos(4+5j)",cmath.cos(4+5j))
print("sin(4+5j)",cmath.tan(4+5j))
print("tan(4+5j)",cmath.asin(4+5j))
print("acos(4+5j)",cmath.acos(4+5j))
print("atan(4+5j)",cmath.sinh(4+5j))
print("tanh(4+5j)",cmath.cosh(4+5j))
print("rect(3,4)",cmath.rect(3,4))
print("log(1+2j)",cmath.log(1+2j))
print("exp(1+2j)",cmath.exp(1+2j))

###

from scipy.stats import describe 
import numpy as np 
x=np.random.normal(size=50)
r=describe(x)
print(r)

###

a = 5 
a = 1, 2, 3 
print(a)

i = 10 
print(i!=i>5)

x=int(input("enter number: "))
y=int(input("enter number: "))
test={"add":x+y,"sub":x-y,"mul":x*y,"div":x/y}
op=input("enter operation: ")
print(test.get(op, "wrong option"))

###

print(3**2)
print(3. **2)
print(3**2.)
print(3. **2.)

print(3*2)
print(3. *2)
print(3*2)
print(3. *2.)

print(8/2)
print(8. /2)
print(8/2.)
print(8. /2.)

print(8//2)
print(8. //2)
print(8//2.)
print(8. //2.)

print(-8//2)
print(8. //-2)
print(-8//2.)
print(-8. //2.)

print(8%2)
print(8.5%2)
print(8%2.5)
print(8.5%2.5)

print(8+2)
print(-8.5+2)
print(-8+2.5)
print(8.+2.5)

print(8-2)
print(-8.5-2)
print(-8-2.5)
print(8.-2.5)

print((4%2),5**2,(5+4**3))

x = 11
y = 33
print("sum =", x+y)

print(5==5)
print(5==5.)

x,y,z=5,6,7
print(x>y)
print(x>z)

x,y,z=1,2,3
print(x>y)
print((z-2) == x)

x=5
y=5.0
z="5"
if(x==y):
    print(x)
if(x==int(z)):
    print(x)

############

a,b=10,5
if(a<b):
    print(" a is smaller than b")
if(b<a):
    print(" b is smaller than a")

###########

def maximum(a, b):
    if a >= b:
        return a 
    else:
        return b 
#main code
a = 2 
b = 4 
print(maximum(a, b))

############

num1 = int(input("Enter the num1: "))
num2 = int(input("Enter the num2: "))
# printing the maximum value 
print("The maximum of all values is", (num1 if num1 >= num2 else num2))

############


year = 2000 
if (year % 4) == 0:
    if (year % 100) == 0:
        if (year % 400) == 0:
            print("{0} is a leap year".format(year))
    else:
        print("{0} is not a leap year.".format(year))
else:
    print("{0} is not a leap year".format(year))

############

#Calculating Grade 
m1=int(input("enter m1: "))
m2=int(input("enter m2: "))
m3=int(input("enter m3: "))
p=(int)(m1+m2+m3/3)
if(p>90):
    print("Grade-A")
elif(p>80 and p<=90):
    print("Grade B")
elif(p>60 and p <= 80):
    print("Grade-c")
elif(p>60 and p<=45):
    print("Pass")
else:
    print("Fail")

##############

# find smallest of three integers without comparison operators

def smallest(x,y,z):
    c = 0 
    while(x and y and z):
        x = x-1
        y = y-1
        z = z-1
        c = c+1
        return c 
x = 12 
y = 15 
z = 5 
print("Minimum of 3 numbers is", smallest(x,y,z))

################

# multiplication table

num = int(input("Enter the number: "))
i = 1 
# for loop to iterate multiplication 10 times 
print("Multiplication Table of: ")
while i<10:
    num = num * 1 
    print(num, '*', i, '=', num*i)
    i += 1 

#####

for seq in range(10):
    print(seq)

#####

for seq in range(50,1000,100):
    print(seq)

####

for seq in range(100, 10, -10):
    print(seq)

####

for i in range(-1, -11, -1):
    print(i, end=', ')


####

n = int(input("enter number: "))
for i in range(1,n+1):
    for j in range(1,i+1):
        print(i, end=" ")
    print() 

####

n = int(input("enter a number: "))
for i in range(1,n+1):
    for j in range(1,i+1):
        print(j, end=" ")
    print() 

####

n=int(input("enter number: "))
t=n
sum=0
while(n!=0):
    i,f=1,1
    r=n%10
    while(i<=r):
        f*=i
        i+=1
        sum+=f
        n//=10
        if(t==sum):
            print(t, "is strong number")
        else:
            print(t, "is not strong number")

####

# multiplication table using nested while 

n=2
while 1:
    i=1;
    while i<=10:
        print("%d x d = %d\n"%(n,i,n*i));
        i = i+1;
        choice = int(input("Do you want to continue printing the table, press 0 for no?"))
        if choice == 0:
            break;
n=n+1 

####

for i in range(1, 5):
    print(i)
else:
    print("No Break")

####

for val in sequence:
    pass 

for i in "this is to test":
    if i=="e" or i=="o":
        pass
    else:
        print(i,end=" ")

####

for val in "string":
    if val == "i":
        break 
        print(val)

####

n = 1 
while n < 5:
    n += 1 
    if n == 3:
        break 
    print(n)

####

for i in range(3):
    for j in range(2):
        if j == i: 
            break 
        print(i, j)

####

# break inner loop while
while True:
    print("In outer loop")
    i = 0 
    while True:
        print("In inner loop")
        if i >= 5:
            break 
        i += 1 
        print("Got out of inner loop, still inside outer loop")~
        break 

####

for val in "string":
    if val == "i":
        continue 
    print(val)

####

i = 1 
while i <= 5:
    i = i+1 
    if(i==3):
        continue 

####

first = [1,2,3]
second = [4,5]
for i in first:
    for j in second: 
        if i == j:
            continue 
    print(i, '*', j, '=', i * j)

####

for i in "test":
    if i == "s":
        break 
print(i)

####

n=int(input("enter number: "))
sum=0 
t=n
C=0
while t>0:
    c=c+1
    t=t//10
    t=n
    while t>0:
        r=t%10
        sum+=(r**c)
        t//=10
        if n==sum:
            print(n, "is amstrong number")
        else:
            print(n, "is not amstrong number")

####

n = int(input("enter number"))
f=1
for i in range(1,n+1):
    f*=i
print("factorial is",f)

####

n=int(input("enter number: "))
rev=0
while(n>0):
    r=n%10
    rev=rev*10+r
    n=n//10
print("reverse number",rev)

####

# Palindrome Number 
n=int(input("enter number: "))
rev=0
t=n
while(n>0):
    r=n%10
    rev=rev*10+r
    n=n//10
    if(t==rev):
        print(t," is palindrome")
    else:
        print(t, " is not palindrome")

####

# printing first max and the second max number

n=int(input("enter range: "))
fbig,sbig=0,0
for i in range(0,n,1):
    num=int(input("enter number: "))
    if(num>fbig):
        sbig=fbig
        fbig=num
        if(num>sbig and num<fbig):
            sbig=num
            print("first max:",fbig)
            print("second max":,sbig)
    
####

# perfect number 
n=int(input("enter number: "))
sum=0
for i in range(1,n):
    if(n%i==0):
        sum+=i
        if(n==sum):
            print(n, "is perfect number")
        else:
            print(n, "is not perfect number")

####

n=int(input("enter number: "))
for i in range(n,0,-1):
    for j in range(1, i+1):
        print(j,end=" ")
    print()

####

n=int(input("Enter number: "))
for i in range(n,0,-1):
    for j in range(i, 0, -1):
        print(j, end=" ")
    print()

####

def minimum(a, b):
    if a <= b:
        return a 
    else:
        return b 
a = 2 
b = 4 
print(minimum(a, b))

####

def calculate_gross_salary(basic_salary):
    hra=0
    da=0
    if(basic_salaru < 2500):
        hra = (basic_salary * 10) / 100
        da = (basic_salary * 90) / 100 
    else:
        hra = 1000 
        da = (basic_salary + hra + da)
    if __name__ == "__main__":
        basic_salary = float(input("Enter basic salary: "))
        gross_salary = calculate_gross_salary(basic_salary)
        print("Gross Salary us: %f" % gross_salary)

###

# max of 3 numbers using while loop 
numbers = [1,2,5,8,4,99,3]
x = 0 
lar = numbers[x]
while x < len(numbers):
    if numbers[x] > lar:
        lar = numbers[x]
        x = x+1
        print(lar)

#
#infinite loop using while:
while True: 
    num = int(input("Enter an integer: "))
    print("The double of", num, "is", 2 * num)

# program to display the multiplication table:
num = int(input("Enter the number: "))
print("Multiplication Table of: ")
for i in range(1, 11):
    print(num, 'x', i, '=', num*i)

#####

#infinite loop using for

import itertools
for i in itertools.count():
    print(i)

#####

#Pascal triangle 
n=int(input('enter range: '))
for i in range(0,n):
    for s in range(0,n-i):
        print(end=" ")
        for j in range(0, i+1):
            if(j==0 or i==0):
                c=1
            else:
                c=(int)(c*(i-j+1)/j)
                print(c,end=" ")
                print()

# check even or odd using ternary operator 
x=int(input("enter number: "))
s="even" if x x%2==0 else "odd"
print(x,"is",s)

#####
# Max of three numbers using ternary operator 

x=int(input("enter number: "))
y=int(input("enter number: "))
z=int(input("enter number: "))
max = x if x>y and x>z else y if y>z else z 
print("max:",max)

# Max of four numbers using ternary operator

p=int(input("enter number: "))
q=int(input("enter number: "))
r=int(input("enter number: "))
s=int(input("enter number: "))
max = p if p>q and p<r and p>s else q if q>r and q>s else r if r>s else s 
print("max:",max)

############
# Python program to find the largest number among the three numbers

def maximum(a,b,c):
    if(a>=b) and (a>=c):
        largest = a 
    elif (b>=a) and (b>=c):
        largest = b 
    else:
        largest = c 
        return largest 

a = 10 
b = 14 
c = 2 
print(maximum(a, b, c))

###########

# Python program to find smallest of three integers using division operator to find
# minimum of three numbers 

def smallest(x, y, z):
    if(not(y/x)):
        return y if(not(y/z)) else z
        return x if (not(x/z)) else z 

if __name__ == "___main__":
    x = 78 
    y = 88 
    z = 68 
print("Minimum of 3 numbers is", smallest(x,y,z))

####
# even inclusive range()
step = 2 
for i in range(2, 20 + step, step):
    print(i, end=' ')

# range() indexing and slicing 
range1 = range(0,10)
#first number (start number) in range 
print(range1[0])
# access 5th number in range
print(range[5])
# access last number 
print(range1[range1.stop - 1])

# Negative indexing range 
# negative indexing access last number
print(range(10)[-1])
# access second last number 
print(range(10)[-2])

# slicing range 
for i in range(10)[3:8]:
    print(i, end=' ')
# reverse range 
for i in reversed(range(10, 21, 2)):
    print(i, end=' ')

# One-Line while loops 
n = 5 
while n>0: n-=1; print(n)

# Use of break statement inside the loop 
for val in "string":
    if val == "i":
        break
    print(val)

# concatenate two of more range functions using the itertools
from itertools import chain 
a1 = range(10,0.-2)
a2 = range(30,20,-2)
a3 = range(50,40,-2)
final = chain(a1,a2,a3)
print(final)

# 1. Write a Python program. Use the while loop and continuosly 
# ask the programmer to enter the word unless the programmer enters
# the word "quit". By entering the word "quit", the loop should terminate.

# 2. Write a Python program to read an input from the user and separate
# the vowels an consonants in the entered word. 

# 3. Write a Python program to read an input from the user and to print
# the uppercase of the entered word. 

# //////////////////////

s="this is to test"
print(s[0])
print(s[13])
print(s[0:])
print(s[5:10])
print(s[-3])
print(s[-7:-3])
print(s)
print("s[:6]--",s[:6])
print("s[4:]--",s[4:])
print("s[-1]",s[-1])
print("s[-2:5]--",s[-2:5])
print("s[5:2]--",s[5:-2])
print("s[::-1]--",s[::-1])
print("s[-14]--",s[-14])
print("s[-15]--",s[-15])
print("s[:-1]--",s[-1])
print("s[5:-1]--".s[5:-2])
print("s[5:-2]--",s[5:-2])
print("s[5:-2]--",s[5:-2])
print("s[-5:-2]--",s[-5:-2])

# //////////////////////

s = 'india'
print(s)

s = 'this is to test'
print(s[0:])
print("updated string:- ", s[:6] + 'Python')

s = "Vijayawada"
print(s)
s="python"
s="string example"
print(s)
s="this is to test"
print(s)

#######

print("\\")

s = "python"
print(s+s)
print(s+s+s)
print(s*4)
print('t' in s)
print('t' not in s)
print('12345'*3)

#######

'''
%c -> Characther 
%i -> String convertion 
%s -> Signed integer 
%d -> Unsigned integer
%u -> unsigned integer 
%o -> octal integer 
%x -> hexadecimal integer - lowercase 
%X -> hexadecimal integer - uppercase 
%e -> exponent notation - lowercase 
%E -> Exponent notation - uppercase 
%f -> Floating point
%g -> Shorter form %f and %e
%G -> Shorter form %f and %E
'''

s = "{}{}{}".format('this', 'is', 'for', 'test')
print(s)
s = "{}  {}  {}  {}".format('this', 'is', 'for', 'test')
print(s)
s="{3}{2}{1}{0}".format('this', 'is', 'for', 'test')
print(s)
s="{t}{i}{f}{e}".format(t='this',i='is',f='for',e='test')
s="{},      string      format      example".format("python")
print(s)
s="this example is  for {}, string".format("python")
print(s)

s = "this is to test"
print(s)
s1 = "this is to test"
print(s1)
s2 = "this is to test"
print(s2)
s3 = "this is to test"
print(s3)
s4 ='''this is
to
test'''
print(s4)
s5 = "this is \n to test"
print(s5)
print("'{}'".format("this is to test"))
print('"{}"'.format("this is to test"))
st="this is to test"
print("%s"%s)
print("\\%s\\"%st)
print("\"%s\" "%st)
print("It\'s python \'String\' testing")
print("\"Python\"String example")
print(r"\"Python\"      String example")
print("{:.7}".format("this is to test"))

print("this     {0:10}   is to test {1:10}      {2:10}}".format('example','python','string'))
print("this {0:>10} is to test {1:>10}      {2:>10}".format('example', 'python', 'string'))
print("this {:^10} is to test {1:^10}   {2:^10}".format('example', 'python', 'string'))
print("this { 0:@>10} is to test {2:*>10}   {2:&>10}".format('example', 'python', 'string'))
print("this {0:$<10} is to test {1:%<10}    {2:~<10}".format('example', 'python', 'string'))

s="Vijayawada"
print(s)
print("\"Python\"String example")
print(r"\"Python\"  String example")
print("{:.7}".format("this is to test"))
print("this {0:10}  is to test {1:10}   {2:10}".format('example', 'python', 'string'))
print("this {0:>10}  is to test {1:>10}     {2:>10}".format('example', 'python', 'string'))
print("this    {0:@>10} is to test {1:*>10}     {2:&>10}".format('example', 'python', 'string'))
print("this  {0:$<10} is to test {1:%<10}   {2:~<10}".format('example', 'python', 'string'))

print(u'test') #string as unicode 16-bit values.

s='Vijayawada'
print(s)
s[0] = 'b'
print(s.replace('V', 'B'))

s="this is to test"
print(s.capitalize())
print(s.lower())
print(s.swapcase())
print(s.title())
print(s.upper())
print(s.count('t'))
print(s.find('s'))
print(s.index('is'))
print(s.rfind('is'))
print(s.rindex('is'))
print(s.startswith('this'))
print(s.endswith('t'))
print(" this is to test ".lstrip())
print(" this is to test ".rstrip())
print(" this is to test ".strip())
print(s.partition('@'))
print(s.rpartition('@'))
print(s.split())
print(s.rsplit())
print(s.splitlinbes())
print("this \t  is  \v  to  \b  test".splitlines())
print("this is to test".casefold())
print("THIS IS TO TEST".casefold())
print(s.encode())
s="python"
print("the given string is: ", s)
del s 
print(s)
s ="this is to test"
del s[1]

#######


# 1. write a Python program using the new line and the escape characters
# to match the expected result as follows:
# "This is"
# "to test"
# "Python language"

# 2. Write a program to count the number of the characters in the 
# string (Do not use the predefined method)

# 3. Access the first three characthers and the last two characters 
# from the given string. 

# 4. Count the number of ocurrences of the first character in the given string. 

# 5. Access the longest word in the given sentence. 

# 6. Exchange the first and the last characters of each word in a sentence. 

# 7. Insert the character <> in the middle of each word in a sentence. 

# 8. Access the words whose length is less than 3. 

# 9. Reverse the words in a sentence. 

# 10. Print the index of the characthers of the string. 

# 11. Replace the vowel with a specified character.

# 12. Remove the duplicate characters from the string. 

r = range(2, 20, 3)
l = list()
for x in r:
    l.append(x)
    print(l)

#####

l1 =[1, 3, 5, 7, 9]
l = len(l1)
i = 0
while i < l:
    print(l1[i])
    i += l 

# l1 is the list, which consists of five integer elements. Using the while loop to print the list l1 elements. The variable i is used as the index variable. The while condition is i<l, that is, the loop repeats for the length of the list. If the c