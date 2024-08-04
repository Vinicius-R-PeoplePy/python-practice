'''
Exercise 6

Ask the user for a string and print out whether this string
is a palindrome or not. (A palindrome is a string that reads the same forwards and backwards).

Discussion

Concepts:

- List indexing 
- Strings are lists 

List indexing 

In Python (and most programming in general), you start
counting lists from the number 0. The first element in
a list is "number 0", the second is "number 1", etc.

As a result, when you want to get single elements out
of a list, you can ask a list for that number element:

>>> a = [5, 10, 15, 20, 25]
>>> a[3]
20 
>>> a[0]
5

There's also a convenient way to get sublists between 
two indices:

>>> a = [5, 10, 15, 20, 25, 30, 35, 40]
>>> a[1:4]
[10, 15, 20]
>>> a[:-1]
[5, 10, 15, 20, 25, 30, 35]

The first number is the "start index" and the last number
is the "end index".

You can also include a third number in the indexing, to count
how often you should read from the list:


>>> a = [5, 10, 15, 20, 25, 30, 35, 40]
>>> a[1:5:2] #salta de 2 em dois, de 10 à 20, no caso. 
[10, 20]
>>> a[3:0:-1]
[15, 10, 5]

To read the whole list, just use the variable name
(in the above examples, a), or you can also use [:]
at the end of the variable name (in the above examples
a[:])

Strings are lists 

Because strings are lists, you can do to strings everything that you do to lists.
You can iterate through them:

string = "example"
for c in string:
    print("one letter: " + c)
    
>>>
one letter: e
one letter: x
one letter: a
one letter: m
one letter: p
one letter: l
one letter: e


ou em uma linha:

print(''.join(f"one letter: {c}\n for c in "example")) # linhas múltiplas
print(''.join(f"one letter: {c}" for c in "example)) # letras em única linha

You can take sublists:

>>> string = "example"
s = string[0:5]
print s 
>>> examp 
'''

# Agora o palíndromo. 

#print(''.join(f"palíndromo: {pa} for pa in "zazas" if "zazas"(reverse=True) else #print("Não é palíndromo)))

#pa = ("zazas")
#if pa == pa(reversed=True):
#    print(f"palíndromo: {pa}")
#else: 
#    print("Não é um palíndromo.")
    
'''
if pa == pa(reversed=True):
             ^^^^^^^^^^^^^^^^^
TypeError: 'str' object is not callable
'''

pa = "zazas"
if pa == pa[::-1]:
    print(f"A palavra {pa} forma palíndromo: {pa}")
else:
    print(f"A palavra {pa} não forma palíndromo")
    
pa = "zazaz"
if pa == pa[::-1]:
    print(f"A palavra {pa} forma palíndromo: {pa}")
else:
    print(f"A palavra {pa} não forma palíndromo")
    print(f"palíndromo: ")
    
# em uma única linha: 

print(f"A palavra {pa} forma o palíndromo: {pa}" if pa == pa[::-1] else f"A palavra {pa} não forma palíndrome")

### com função:

def inverte(palavra):
    x = ''
    for i in range(len(palavra)):
        x += palavra[len(palavra)-1-i]
    return x 

palavra = input('digite uma palavra:\n')
x = inverte(palavra)
if x == palavra:
    print(f'A palavra {palavra} forma o palíndromo: {palavra}')
else:
    print(f'A palavra {palavra} não forma o palíndromo {palavra}')
    
