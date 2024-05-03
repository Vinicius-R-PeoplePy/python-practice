'''
Exercise 6

Ask the user for a string and print out
whether this string is a palindrome
or not. (A palindrome is a string
that reads the same forwards and backwards).

Discussion 

Concepts:

- List indexing 
- Strings are lists 

List indexing 

In Python (and most programming in general), 
you start counting lists from 
the number 0. The first element 
in a list is "number 0",
the second is "number 1", etc. 

As a result, when you want to get
single elements out of a list,
you can ask a list for
that number element:

>>> a = [5, 10, 15, 20, 25]
>>> a[3]
20 
>>> a[0]
5

There is also a convenient way to get
sublists between two indices: 

>>> a = [5, 10, 15, 20, 25, 30, 25, 40]
>>> a[1:4]
[10, 15, 20]
>>> a[:6]
[35, 40]
>>> a [:-1]
[5, 10, 15, 20, 25, 30, 35]

The first number is the "start index" and 
the last number is the "end index". 

You can also include a third number
in the indexing, 
to count how often you should read from the list:

>>>a = [5, 10, 15, 20, 25, 30, 35, 40]
>>> a[1:5:2]
[10, 20]
>>> a[3:0:-1]
[15, 10, 5]

To read the whole list,
just use the variable name
(in the above examples, a),
or you can also use [:]
at the end of the variable
name (in the above examples,
a[:]).

Strings are lists 

Because strings are lists,
you can do to strings everything 
that you do to lists. 
You can iterate through them: 

strin = "example"
for c in string:
  print "one letter: " + c 

Will give the result: 

one letter: e
one letter: x
one letter: a
one letter: m
one letter: p
one letter: l
one letter: e

You can take sublists:

>>> string = "example"
>>> s = string[0:5]
>>> print s 
examp

'''
# wrong try: 

'''word = input("enter a word: ")
for letter in word: 
    if word[:-1] == word[:1]:
        print("Is palindrome.")
    else:
        print("Is not palindrome.")'''

# another wrong try: 

'''word = input("enter a word: ")
palindrome = word(reverse=True)
if word == palindrome:
    print(f"Word {word} is palindrome ({palindrome})")
else:
    print(f"Word {word} isn't palindrome ({palindrome}).")'''

'''
Explanation: 

1. The 'reverse=True' argument
doesn't work with the 'input()'
function. Instead, you need to 
reverse the string using slicing
or other methods. 
2. The 'palindrome = word(reverse=True)' line should be 
corrected to properly reverse the string. 
3. There's a missing '[::-1]' slice 
syntax for reversing the string.
4. You need to convert 'palindrome'
to lowercase to compare it correctly. '''

word = input("enter a word: ")
palindrome = word[::-1]
if word.lower() == palindrome.lower():
    print(f'Word {word} is a palindrome ({palindrome})')
else:
    print(f"Word {word} isn't a palindrome ({palindrome})")

