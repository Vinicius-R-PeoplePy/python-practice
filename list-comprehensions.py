'''
Exercise 7

Let's say I give you a list in a variable: a [1, 4, 9, 16, 24, 36, 49, 64, 81, 100].

Write one line of Python that takes this list 'a' and makes a new list that has only
the even element of this list in it.

Discussion 

Concepts:

- List comprehensions

The idea of list comprehension is to make code more compact 
to accomplish tasks involving lists. 
Take for example this code:

years_of_birth = [1990, 1991, 1990, 1992, 1991]
ages = []
for year in year_of_birth:
    ages.append(2014 - year)
    
>>> [24, 23, 24, 24, 22, 23]

What this code did was translate the years of birth into ages,
and it took us a for loop and an append statement to a new list to do that. 

Compare to this piece of code:

years_of_birth = [1990, 1991, 1990, 1990, 1992, 1991]
ages = [2014 - year for year in years_of_birth]

The second line here - the line with ages is a list comprehension. 

It accomplishes the same thing as the first code sample - at the end, 
the ages variable has a list containing [24, 23, 24, 24, 22, 23],
the ages corresponding to all the birthdates.

The idea of the list comprehension is to condense the foor loop and the list
appending into one simple line. Notice that the for loop just shifted to the end
of the list comprehension, and the part before the for keyword is the thing to
append to the end of the new list.

You also embed if statements into the list comprehension - 
check: 
https://docs.python.org/3/tutorial/datastructures.html#list-comprehensions

5. Data Structures 

This chapter describes some things you've learned about already in more
detail, and adds some new things as well. 

5.1. More on Lists 

The list data type has some more methods. Here are all of the 
methods of list objects: 

list.append(x)
-> Add an item to the end of the list. Equivalent to a[len(a):] = [x].

list.extend(iterable)
-> Extend the list by appending all the items from the iterable. 
Equivalent to a[len(a):] = iterable.

list.insert(i, x)
-> Remove the first item at a given position. The first argument is 
the index of the element before which to insert,
so a.insert(0, x) inserts at the front of the list, and a.insert(len(a), x) is 
equivalent to a.append(x)

list.remove(x)
-> Remove the first item from the list whose value is equal to x.
It raises a ValueError if there is no such item.

list.pop([i])
-> Remove the item at the given position in the list, and return it. 
If no index is specified, a.pop() removes and returns the last item
in the list. It raises an IndexError if the list is empty or the index is
outside the list range. 

list.clear()
-> Remove all items from the list. Equivalent to del a[:].

list.index(x[, start[, end]])
-> Return zero-based index in the list of the first item whose value is 
equal to x. Raises a ValueError if there is no such item. 

The optional arguments 'start' and 'end' are interpreted as in the slice notation
and are used to limit the search to a particular subsequence of the list.
The returned index is computed relative to the beginning of the full 
sequence rather than start argument. 

list.count(x)
-> Return the number of times x appears in the list.

list.sort(*, key=None, reverse=False)
-> Sort the items of the list in place (the arguments can be used for 
sort customization, see sorted() for their explanation).

list.reverse()
-> Reverse the elements of the list in place.

list.copy()
-> Return a shallow copy of the list. Equivalent to a[:].

An example that uses most of the list methods:

>>> fruits = ['orange', 'appple', 'pear', 'banana', 'kiwi', 'apple', 'banana']
>>> fruits.count('apple')
2
>>> fruits.count('tangerine')
0
>>> fruits.count('banana')
3
>>> fruits.index('banana',4) # Find next banana starting at position 4
6
>>> fruits.reverse()
>>> fruits 
['banana', 'apple', 'kiwi', 'banana', 'pear', 'apple', 'orange']
>>> fruits.append('grape')
>>> fruits
['banana', 'apple', 'kiwi', 'banana', 'pear', 'apple', 'orange', 'grape']
>>> fruits.sort()
>>> fruits
['apple', 'apple', 'banana', 'banana', 'grape', 'kiwi', 'orange', 'pear']
>>> fruits.pop()
'pear'

You might have noticed that methods like insert, remove or sort that only modify
the list have no return value printed - they return the default 
None. This is a design orinciple for al mutable structures in Python. 

Another thing you might notice is that not all data can be sorted or compared.
For instance, [None, 'hello', 10] doesn't sort because integers 
can't be compared to strings and None can't be compared to other types. 
Also, there are some types that don't have a defined ordering relation.
For example, 3+4j < 5+7j isn't a valid comparasion. 

5.1.1. Using Lists as Stacks 

the list methods make it very easy to use a list as a stack, where
the last element added is the first element retrieved  ('last-in, first-out')
(LIFO). To add an item to the top of the stack, use append(). 
To retrieve an item from the top of the stack, use pop() without 
an explicit index. For example: 

>>> stack = [3, 4, 5]
>>> stack.append(6)
>>> stack.append(7)
>>> stack 
[3, 4, 5, 6, 7]
>>> stack.pop
7
>>> stack.pop()
6
>>> stack.pop()
5
>>> stack 
[3, 4]

5.1.2. Using Lists as Queues 

It is also possibleto use a list as a queue, where the first element
added is the first element retrieved ('first-in, first-out'),
(FIFO).However, lists are not efficient for this purpose. 
While appends and pops from the end of  list are fast, doing 
inserts or pops from the beginning of a list is slow
(because all of the other elements have to be shifted by one).

To implement a queue, use collections.deque # https://docs.python.org/3/library/collections.html#collections.deque

which was designed to have fast appends and pops from both ends. Ex.:

>>> from collections import deque
>>> queue = deque(["Eric", "John", "Michael"])
>>> queue.append("Terry") # Terry arrives
>>> queue.append("Graham") # Graham arrives
>>> queue.popleft() # The first to arrive now leaves
'Eric'
>>> queue.popleft() # The second to arrive now leaves
'John'
>>> queue   # Remaining queue in order of arrival 
deque(['Michael', 'Terry', 'Graham'])

5.1.3. List Comprehensions 

List comprehensions provide a concise way to create lists.
Common applications are to make new lists where each element
is the result of some operations applied toeach member 
of another sequence or iterable, or to create a subsequence
of those elements that satisfy a certain condition. 

>>> squares = [] 
>>> for x in range(10):
        squares.append(x**2)
        
>>> squares
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
# 0**1=1, 1**1=2, 2**2=4, 4**4=16, 5**5=25, 6**6=36, 7**7=49, 8**8=64, 9**9=81...

# nota: não consulte ChatGPT... Pare para entender a lógica. (Levei ~40segundos para entender.)
# princípio fundamental: queime neurônios. ChatGPT é rodinha de bicicleta. De vez em quando um bom trampolim, entretanto.

Note that this creates (or overwrites) a variable named x that still exists
after the loop completes. We can calculate the list of squares
without any side effects using:

squares = list(map(lambda x: x**2, range(10))) # sintaxe lambda (!)

or, equivalently:

squares = [x**2 for x in range(10)]

which is more concise and readable.

A list comprehension consists of brackets containing an expression
followed by a for clause, then zero or more for or if clauses.
The result will be a new list resulting from evaluating the expression
in the context of the for and if clauses which follow it. 
For example, this listcomp combines the elements of two lists
if they are not equal:

>>> [(x, y) for x in [1,2,3] for y in [3, 1, 4] if x != y]
[(1, 2), (1, 4), (2, 3), (2, 1), (2, 4), (3, 1), (3, 4)]

and it's equivalent to:

>>> combs = []
>>> for x in [1,2,3]:
        for y in [3,1,4]:
            if x != y:
                combs.append((x, y))
                
>>> combs
[(1, 2), (1, 4), (2, 3), (2, 1), (2, 4), (3, 1), (3, 4)]

Note how the order of the for and if statements is the same in both
these snippets.

If the expressionj is a tuble (e.g. the (x, y) in the previous example), 
it must be parenthesized.

>>> vec = [-4, -2, 0, 2, 4]
>>> # create a new list with the values doubled
>>> [x*2 for x in vec]
[-8, -4, 0, 4, 8]
>>> # filter the list to exclude negative numbers
>>> [x for x in vec if x >= 0]
[0, 2, 4]
>>> # apply a function to all the elements 
>>> [abs(x) for x in vec]
[4, 2, 0, 2, 4]
>>> # call a method on each element 
>>> freshfruit = [' banana', '  loganberry', 'passion fruit ']
>>> [weapon.strip() for weapon in freshfruit]
['banana', 'loganberry', 'passion fruit']
>>> # create a list of 2-tuples like (number, square)
>>> [(x, x**2) for x in range(6)]
[(0, 0), (1, 1), (2, 4), (3, 9), (4, 16), (5, 25)]
>>> # the tuple must be parenthesized, otherwise an error is raised
>>> [x, x**2 for x in range[6]]
File "<stdin>", line 1
    [x, x**2 for x in range(6)]
    ^^^^^^^^
SyntaxError: did you forget parentheses around the comprehension target?
>>> # flatten a list using a listcomp with two 'for'
>>> vec = [[1,2,3], [4,5,6], [7,8,9]]
>>> [num for elem in vec for num in elem]
[1, 2, 3, 4, 5, 6, 7, 8, 9]

List comprehensions can contain complex expressions and nested functions:

>>> from math import pi 
>>> [str(round(pi, i)) for i in range(1, 6)] # 5 elementos
['3.1', '3.14', '3.142', '3.1416', '3.14159']

5.1.4. Nested List Comprehensions

The initial expression in a list comprehension can be any
arbitrary expression, including another list comprehension. 

>>> matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
]

The followiung list comprehension will transpose rows and columns:

>>> [[row[i] for row in matrix] for i in range(4)]
[[1, 5, 9], [2, 6, 10], [3, 7, 11], [4, 8, 12]]

As we saw in the previous section, the inner list comprehension 
is evaluated in the context of the for that follows it,
so this example is equivalent to:

>>> transposed = []
>>> for i in range(4):
        transposed.append([row[i] for row in matrix])
        
>>> transposed
[[1, 5, 9], [2, 6, 10], [3, 7, 11], [4, 8, 12]]

Which, in turn, is the same as:

>>> transposed = [] 
>>> for i in range(4):
        # the following 3 lines implement the nested listcomp 
        transposed_row = [] 
        for row in matrix:
            transposed_row.append(row[i])
        transposed.append(transposed_row)
        
>>> transposed 
[[1, 5, 9], [2, 6, 10], [3, 7, 11], [4, 8, 12]]

In the real world, you should prefer built-in functions to complex
flow statements. The zip() function would do a great job for this
use care:

>>> list(zip(*matrix))
[[1, 5, 9], [2, 6, 10], [3, 7, 11], [4, 8, 12]]


See Unpacking Arguments Lists for details on the asterisk in this line.
https://docs.python.org/3/tutorial/controlflow.html#tut-unpacking-arguments

5.2. The del statement 

There is a way to remove an item from a list given its index
of its value: the del statement. This differs from the pop()
method which returns a value. The del statement can also be used
to remove slices from a list or clear the entire nlist
(which we did earlier by assignment of an empty list to the slice).
For example:

>>> a = [-1, 1, 66.25, 333, 333, 1234.5]
>>> del a[0]
>>> a 
[1, 66.25, 333, 333, 1234.5]
>>> del a[2:4]
>>> a
[1, 66.25, 1234.5]
>>> del a[:]
>>> a
[] 

del can also be used to delete entire variables:

>>> del a 

Referencing the name a hereafter is an error (at least until 
another value is assigned to it). We'll find other uses 
for del later. 


5.3 Tuples and Sequences 

We saw that lists and strings have many common properties, 
such as indexing and slicing operations. 
They are two examples of sequence data types 
(see Sequence Types --- list,tuple,range) # https://docs.python.org/3/library/stdtypes.html#typesseq

Since Python is an evolving language, other sequence data types may be added. 
There is also another standard sequence data type: the tuple. 

A tuple consists of a number of values separated by commas, 
for instance:

>>> t = 12345, 54321, 'hello!'
>>> t[0]
12345 
>>> t 
(12345, 54321, 'hello!')
>>> # Tuples may be nested: 
    u = t, (1, 2, 3, 4, 5)
>>> u 
(12345, 54321, 'hello!'), (1, 2, 3, 4, 5)
>>> # Tuples are immutable:
    t[0] = 88888
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'tuple' object does not support item assignment 
>>> # but they can contain mutable objects
    v = ([1, 2, 3], [3, 2, 1])
>>> v
([1, 2, 3], [3, 2, 1])

As you see, on output tuples are always enclosed in parentheses,
so that nested tuples are interpreted correctly;
they may be input with or without surrounding parentheses,
although often parentheses are necessary anyway (if the tuple
is part of a larger expression). It is not possible to assing 
to the individual items of a tuple, however it is possible to 
create tuples which contains mutable objects, such as lists.

Though tuples may seem similar to lists, they're often used in
different situations and for different purposes.
Tuples are immutable, and usually contain 
a heterogenerous sequence of elements that are accessed via unpacking 
or indexing (or even by attribute in the case of namedtuples).
# https://docs.python.org/3/library/collections.html#collections.namedtuple

Lists are mutable #https://docs.python.org/3/glossary.html#term-mutable

Their elements are usually homogeneous and are accessed by iterating
over the list.

A special problem is the construction of tuples containing 0 or 1 items:
the syntax has some extra quirks to acommodate these.
Empty tuples are constructed by an empty pair of parentheses;
a tuple with one item is constructed by following a value with a comma
(it is not sufficient to enclose a single value in parentheses). 
For example:

>>> empty = ()
>>> singleton = 'hello', # <- note trailing comma
>>> len(empty)
0 
>>> singleton
('hello', )

The statement t = 12345, 54321, 'hello!' 
is an example of tuple packing:
the values 12345, 54321 and 'hello!' are packed together
in a tuple. The reverse operation is also possible:

>>> x, y, z = t 

This is called, appropriately enough, 'sequence unpacking' and
works for anysequence on the right-hand side.
Sequence unpacking requires that there are
as many variables on the left side of the equals sign as there are
elements in the sequence. Note that multiple assignment is really
just a combination of tuple packing and sequence unpacking. 

5.4 Sets

Python also includes a data type for sets. A set is an unordered 
collection with no duplicate elements. Basic uses include 
membership testing and elimanating duplicate entries. 
Set objects also support mathematical operations like union,
intersection, difference, and symmetric difference.

Curly braces or the set() function can be used to create sets.
Note: to create an empty set you have to use set(),
not {}; the latter creates an empty dictionary. 

Here's a brief demonstration:

>>> basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
>>> print(basket) # show that duplicates have been removed 
{'orange', 'banana', 'pear', 'apple'}
>>> 'orange' in basket
True
>>> 'crabgrass' in basket
False 

>>> # Demonstrate set operations on unique letters from two words
...
>>> a = set('abracadabra')
>>> b = set('alacazam')
>>> a       # unique letters in a 
{'r', 'd', 'b', 'c', 'd'}
>>> a - b 
{'r', 'd', 'b'}     # letters in a but not in b 
>>> a | b           # letters in a or b or both
{'a', 'c', 'r', 'd', 'b', 'm', 'z', 'l'}
>>> a && b          # letters in both a and b 
{'a', 'c'}         
>>> a ^ b           # letters in a or b but not both 
{'r', 'd', 'b', 'm', 'z', 'l'}

Similarly to list comprehensions, set comprehensions are also supported:

>>> a = {x for x in 'abracadabra' if x not in 'abc'}
>>> a
{'r', 'd'}





'''