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

#from os import sep
#from tkinter import END


#a = "Hello, World!"
#print(len(a))

#txt = "The best things in life are free!"
#print("free" in txt)

#txt = "The best things in life are free!"
#if "free" in txt:
#  print("Yes, 'free' is present.")

#print("expensive" not in txt)

#if "expensive" not in txt:
#  print("No, 'expensive' is NOT present.")

#b = "Hello, World!"
#print(b[2:5])
#print(b[:5])
#print(b[:13])

# cool alternative to print HW: 

#b = "Hello World!"
#print(b[:13])

#print(b[2:])
#print(b[0:])
#print(b[-5:-2])
#print(b[-1:])

#print(b.upper())
#print(b[-5:-2].upper())
#print(b[0:9].upper(), b[9:13].lower()) # how to eliminate the space when it prints? #atualização, 09/09/2022: a concatenação neste caso não está funcionando pelo operador ++, mas sim pelo operador +
#segue o exemplo de concatenação apenas com o operador + não-duplicado:
#print(b[0:9].upper()+b[9:13].lower())


#checagem de cálculo que estava resolvendo na mão:

#print(795078+74321-8808*5436) #primeira resposta não confere 

#x = 795078
#y = 743321
#z = 8808
#w = 5436
#m = z*w

#result = x+(y-m)
#print(result) #segunda resposta também não confere



#x = 795078
#y = 743321
#z = 8808
#w = 5436 
#result1 = x + y 
#result2 = -z*w
#a = result1
#b = result2
#result3 = a - b

#result = x+y-z*w #terceira resposta não confere (-46341889); adicionei mais cinco variáveis (res1...b)

#print(result1, result2, result3) 

# provavelmente resultado do cálculo à mão estava errado 

#print("Bem-vindo!")

# guess game forma 1: 

#g = input("Adivinhe o número: ")
#guess = int(g)
#if guess == 5: 
#       print("Você ganhou!", end='\n\n\n' "Parabéns!")
#if guess > 5:
#       print("Você perdeu!")
#       print ("Game over!", end='\n\n\n' "Tente outra vez!...")
#if guess < 5:
#       print("Você perdeu!")
#       print ("Game over!", end='\n\n\n' "Tente outra vez!...")

#x = float(1)
#y = int(2.8)
#z = complex(1)

#print(x)
#print(y)
#print(z)

#print(type(x))
#print(type(y))
#print(type(z))


#import random

#print(random.randrange(1, 10))
#print(random.randrange(1, 100))
#print(random.randrange(1, 1000))
#print(random.randrange(1, 1)) # -> raise ValueError("empty range for randrange() (%d, %d, %d)" % (istart, istop, width)) ValueError: empty range for randrange() (1, 1, 0)
#print(random.randrange(1,2))

#random = float # Como gerar random float?

# via https://www.w3schools.com/python/

# Get the first character of the string txt. 
# txt = "Hello World"
# x = txt[0]

# Get the characters from index 2 to index 4 (llo)
# txt = "Hello World"
# x = txt[2:5]

# Return the string without any whitespace at the beginning of the end
# txt = " Hello World "
# x = txt.strip()

# Convert the value of txt to upper case and lower case. 
# txt = "Hello World"
# txt = txt.upper()
# txt = txt.lower()

# Replace the characther H with a J 
# txt = "Hello World"
# txt = txt.replace("H", "J")

txt = "Números randômicos teste, testando randomicidade."
txt = txt.replace("Números randômicos teste,", "print(random.randrange()) para gerar números aleatórios...")
print (txt) 

import random

print(random.randrange(1, 100))

# Ideias para dicionário. 
# Texto base https://metrologia.org.br/wpsite/wp-content/uploads/2019/07/Cartilha_O_novo_SI_29.06.2029.pdf
# O dicionário conterá medidas do SI (Sistema Internacional de Unidades), como, por exemplo, a definição de que kilograma é a massa de um dl cúbico de água, ou 1 milésimo de 1 metro cúbico de água. 
# SI -> Sistema Internacional de Medidas, criado após a revolução francesa, pela Convenção do Metro, durante a 11ª Conferência Geral de Pesos e Medidas (CGPM), realizada em 1960.
# CGPM -> Conferência Geral de Pesos e Medidas
# Para a definição de SI: possui sete unidades de base: o metro (comprimento), o kilograma (massa), o segundo (tempo), o ampere (corrente elétrica), o kelvin (temperatura termodinâmica), o mol (quantidade de substância) e a candela (intensidade luminosa)
# www.bipm.org/en/about-us/member-states/.
# Antigo kilograma -> definido a partir de um protótipo internacional, um cilindro de uma liga de platina e irídio e essa era a unidade utilizada para determinar a massa de um próton, de um elétron ou de outras partículas elementares.
# Curiosidade -> Em 1900, Max Planck, ao formular sua lei da radiação, já trazia as ideias de "constantes" e de "unidades naturais de medida" que seriam válidas para "todos os tempos e para todas as civilizações, mesmo extraterrestres e não-humanas"...
# Para a definição de segundo -> é relacionado a um número exato de oscilações na camada eletrônica do átomo de césio (relógio atômico).
# Sobre o relógio atômico -> https://super.abril.com.br/mundo-estranho/como-funciona-o-relogio-atomico/
# Para definição de Césio -> O Césio é um elemento químico de símbolo Cs e número atômico 55, com massa atômica de 132,9 u. É obtido por fissão nuclear de outros radioisótopos de urânio ou plutônio. 
# Para definição de urânio e plutônio...

txt = "xxx, yyy"
txt = txt.replace("xxx", "zzz")
print(txt)

#28-09-2022

a = "Hello, World!"
b = "      Hello            World      "
c = a.split(",")
d = a.split("e")
e = "Hello"
f = "World"
g = e + f 
h = e + " " + f 
i = e + "\n" + f 

print(a.upper())
print(a.lower())
print(b.strip()) #not stripping (?)
print(c)
print(d)
print(g)
print(h)
print(i)


# age = 175
#txt = "My name is Abraham, I am" + age 
#print(txt) #-> this will give error, due to the impossibility of combining strings and numbers in such a way. 

age = 175 
txt = "My name is Abraham, I am {}"
print(txt.format(age))

quantity = 3 
itemno = 555
price = 77.77
myorder = "I want {} pieces of item {} for {} dollars"
print(myorder.format(quantity, itemno, price))

quantity = 5 
itemno = 188 
price = 50 
myorder2 = "I want to pay {2} dollars for {0} pieces of item {1}"
print(myorder2.format(quantity, itemno, price))

txt2 = "We are the so-called \"Vikings\" from the north."
print(txt2)

txt3 = 'It\'s alright.' 
print(txt3)

txt5 = "This will insert one \\ (backslash)."
print(txt5)

txt6 = "Hello\rWorld!"
print(txt6)

txt7 = "Hello\tWorld!"
print(txt)

txt8 = "Hello \bWorld!"
print(txt8)

txt9 = "\110\145\154\154\157" # A backslash followed by three integers will result in a octal value in this case. 
print(txt9)

txt10 = "\x48\x65\x6c\x6c\x6f" # A backslash followed by an 'x' and a hex number represents a hex value.
print(txt10)

#check-> https://www.sciencebuddies.org/science-fair-projects/references/ascii-table

k = "diskpart list disk select disk x clean convert gpt create part efi size=500 format fs=fat32 assign letter w create part primary format fs=ntfs quick assign letter c exit"
l = "UNIVERSAL SERIAL BUS"
m = "                  cd/d D:\sources"

print(k.capitalize())
print(l.casefold())
#print(m.center()) #????
print(k.count("a"))
print(k.count("d"))
print(k.encode(encoding="ascii", errors="replace")) 

#encode not functioning. check-> https://www.w3schools.com/python/ref_string_encode.asp

print(l.endswith("s"))
print(l.endswith("S"))

#n = "TRINTA\POR\CENTO\DE\CEM\É\IGUAL\A\TRINTA\DIVIDIDO\POR\CEM\VEZES\CEM\QUE\VAI\DAR\O RESULTADO 30\APÓS OPERAÇÃO\PELA REGRA DE 3\OU POR FRAÇÕES EQUIVALENTES"
#o = n.expandtabs(5)
#print(o) #expandtabs not functioning as in w3schools. Might be due to different python versions?(...)

print(l.find("BUS"))
print(l.find("U")) #found just U string in index 0; not also the U in penultimate index 
print(l.find("L")) 

txt11 = "For only {price:.2f} dollars!"
print(txt11.format(price = 49))

txt12 = "My name is {fname}, I'm {age}".format(fname = "Knuckles", age = 20)
txt13 = "My name is {0}, I'm {1}".format("Obi-Wan", 35)
txt14 = "My name is {}, I'm {}".format("Wally", 36)
print(txt12, txt13, txt14, sep = '\n')














