'''
Exercise 5 

Take two lists, say for example these two:

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 13]

and write a program that returns a list 
that contains only the elements 
that are common between the lists
(without duplicates).
Make sure your program works on two lists
of different sizes. 

Extras: 
1. Randomly generate two lists to test this 
2. Write this in one line of Python
(don't worry if you can't figure this out at this point)

List properties 

In other words, "things you can do with lists".

One of the interesting things you can
do with lists in Python
is figure out whether something 
is inside the list or not. 
For example: 

>>> a = [5, 10, 15, 20]
>>> 10 in a 
True 
>>> 3 in a 
False 

You can of course use this in loops,
conditionals, 
and many other programming constructs. 

list_of_students = ["Michele", "Sara", "Cassie"]

name = input("Type name to check: ")
if name in list_of_students:
   print("This student is enrolled.")
else:
   print("This student isn't enrolled.")
'''

listRange = list(range(1, 21))
listRange2 = list(range(1, 31))
finalList = set(listRange) | set(listRange2)
print(finalList)

### in one line: 

print("In one line of code:\n", list(set(listRange).intersection(set(listRange2))))
