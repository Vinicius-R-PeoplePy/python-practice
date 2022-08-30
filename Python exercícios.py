#29-08-2022, Segunda-feira, exercícios

#from typing import Dict


#x = 5
#y = 7.0
#z = "sim" 
#t = 10>8
#u = ('John, Jen, Ju')
#r = ["1, 2, 3"]
#q = {"1, 2, 3"}
#umatuple = tuple(("maçã, uva, abacate"))

#myDict = {
#  "print(type())": "printa o tipo de variável (str, int, bool, tuple, list, dict...)",
#  "index": "relativo aos caracteres, indica o número, por exemplo: a palavra bolo tem 4 letras, cujo index vai de 0(b) até 4(segundo e último << o >>)",
#  "caractere": "vide unicode (pesquisar!!!!!)"
#}

#print(type(x))
#print(type(y))
#print(type(z))
#print(type(t))
#print(type(u))
#print(type(r))
#print(type(q))
#print(z[1])
#print(z[2], z[1], z[0])
#print(type(umatuple))
#print(myDict)

#for x in "banana":
#    print(x)

#Terça-feira 30-08-2022

# Naive solution to count the total number of set bits in 'n'
#def countSetBits(n):
#
#    count = 0 
#    while n:
#        count += (n & 1)   # check last bit 
#        n >>= 1 
#    return count
#
#if __name__ == '__main__':
#
#  n = 1024
#  print(f'The total number of set bits in {str(n)} ({bin(n)}) is {countSetBits(n)}')

a = "Hello, World!"
print(len(a))

txt = "The best things in life are free!"
print("free" in txt)

txt = "The best things in life are free!"
if "free" in txt:
  print("Yes, 'free' is present.")

print("expensive" not in txt)

if "expensive" not in txt:
  print("No, 'expensive' is NOT present.")

b = "Hello, World!"
print(b[2:5])
print(b[:5])
print(b[:13])

# cool alternative to print HW: 

b = "Hello, World!"
print(b[:13])

print(b[2:])
print(b[0:])
print(b[-5:-2])
print(b[-1:])

print(b.upper())
print(b[-5:-2].upper())
print(b[0:9].upper(), b[9:13].lower()) # how to eliminate the space when it prints?

#checagem de cálculo que estava resolvendo na mão:

#print(795078+74321-8808*5436) #primeira resposta não confere 

#x = 795078
#y = 743321
#z = 8808
#w = 5436
#m = z*w

#result = x+(y-m)
#print(result) #segunda resposta também não confere



x = 795078
y = 743321
z = 8808
w = 5436 
result1 = x + y 
result2 = -z*w
a = result1
b = result2
result3 = a - b

#result = x+y-z*w #terceira resposta não confere (-46341889); adicionei mais cinco variáveis (res1...b)

print(result1, result2, result3) 

# provavelmente resultado do cálculo à mão estava errado 

