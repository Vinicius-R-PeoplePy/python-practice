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

#txt = "Números randômicos teste, testando randomicidade."
#txt = txt.replace("Números randômicos teste,", "print(random.randrange()) para gerar números aleatórios...")
#print (txt) 

# Ideias para dicionário. 
# Texto base https://metrologia.org.br/wpsite/wp-content/uploads/2019/07/Cartilha_O_novo_SI_29.06.2029.pdf
# O dicionário conterá medidas do SI (Sistema Internacional de Unidades), como, por exemplo, a definição de que kilograma é a massa de um dl cúbico de água, ou 1 milésimo de 1 metro cúbico de água. 
# SI -> Sistema Internacional de Medidas, criado após a revolução frances, pela Convenção do Metro, durante a 11ª Conferência Geral de Pesos e Medidas (CGPM), realizada em 1960.
# CGPM -> Conferência Geral de Pesos e Medidas
# Para a definição de SI: possui sete unidades de base: o metro (comprimento), o kilograma (massa), o segundo (tempo), o ampere (corrente elétrica), o kelvin (temperatura termodinâmica), o mol (quantidade de substância) e a candela (intensidade luminosa)
# www.bipm.org/en/about-us/member-states/.
# Antigo kilograma -> definido a partir de um protótipo internacional, um cilindro de uma liga de platina e irídio e essa era a unidade utilizada para determinar a massa de um próton, de um elétron ou de outras partículas elementares.
# Curiosidade -> Em 1900, Max Planck, ao formular sua lei da radiação, já trazia as ideias de "constantes" e de "unidades naturais de medida" que seriam válidas para "todos os tempos e para todas as civilizações, mesmo extraterrestres e não-humanas"...
# Para a definição de segundo -> é relacionado a um número exato de oscilações na camada eletrônica do átomo de césio (relógio atômico).
# Sobre o relógio atômico -> https://super.abril.com.br/mundo-estranho/como-funciona-o-relogio-atomico/
# Para definição de Césio -> O Césio é um elemento químico de símbolo Cs e número atômico 55, com massa atômica de 132,9 u. É obtido por fissão nuclear de outros radioisótopos de urânio ou plutônio. 
# Para definição de urânio e plutônio... 



 

