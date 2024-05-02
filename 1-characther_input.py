'''

From https://www.practicepython.org/

Create a program that asks the user to enter their name and their age. 
Print out a message addressed to them that tells them the year that they will turn 100 years old. Note:
for this execise, the expectation is that you explicitly write out 
the year (and therefore be out of date the next year). 
If you want to do this in a generic way...

Extras:

1. Add on to the previous program by asking the user for another 
and printing out that many copies of the previous message. 
(Hint: order of operations exists in Python)

2. Print out that many copies of the previous message
on separate lines. (Hint: the string "\n" is the same as pressing the ENTER button)

Discussion 

Concepts: 

- Getting user input 
- Manipulating strings (a few ways). 

User input in Python 

To get user input in Python (3), the command you use is input(). 
Store the result in a variable, and use it to your heart's content. 
Remember that the result you get from the user will be a string, even if they enter a number. 
For example,

name = input("Give me your name: ")
print("Your name is " + name)

What this will print in the terminal (or the shell, whatever you are running Python in) will be:

>>> Give me your name: Michele 
Your name is Michele. 

What happens at the end of input() is that it waits for the user to type something and press ENTER.
Only after the user presses ENTER does the program continue. 

Manipulating strings (a few ways)

What you get from the input() function is a string. What can you do with it? 

First: Make the string into a number. Let's say you are 100%
positive that the user entered a number. You can turn 
the string into an integer with the function int(). 
(In a later exercise or two or three there will be questions
about what to do when the user does NOT enter a number
and you try to do this; for now don't worry about that problem)
Here is what this looks like: 

age = input("Enter your age: ")
age = int(age)

(or, if you want to be more compact with your code)

age = int(input("Enter your age: "))

In both cases, age will hold a variable that is an integer,
and how you can do math with it. 

(Note, you can also turn integers into strings exacly in 
the opposite way, using str() function)

Second: Do math with strings. What do I mean by that? 
I mean, if I want to combine (concatenate 
is the computer science word for this) strings,
all I need to do is add them:

print("Were" + "wolf")
print("Door" + "man")
print("4" + "chan")
print(str(4) + "chan")

The same works for multiplication:

print(4 * "test")

but division do not work like this. In terms of multiplication,
the idea of multiplying two strings together is not well-defined. 
What does it mean to multiply two strings in the first place? 
However, it makes sense in a way to specify multiplying 
a string by a number - just repeat that string that number of times. 
Try this in your own program with all the arithmetic operations with 
numbers and strings - the best way to get a feel for 
what works and what doesn't is to try it!"
'''

'''

Wrong try: 

from datetime import date

name = input("enter your name: ")
age = int(input("enter your age: "))
age_future = (100) - age 
year_hundred = (date.today) + age_future
print("Your name is {name}, you have {age} years old and will be 100 years old in {age_future} years on {year_hundred} age.")'''

name = input("What if your name: ")
age = int(input("How old are you: "))
year = 2024 - age + 100 
print(name + ", you will be 100 years old in the year " + str(year))

# another way of doing it:

from datetime import date

name = input("what is your name? ")
age = int(input("Enter your age: "))
year = int(date.today().strftime('%Y'))
print(name, ", in", year + (100-age), "you will turn 100")