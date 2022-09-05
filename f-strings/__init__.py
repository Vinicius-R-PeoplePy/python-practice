#Nome= "Vinícius"
#Idade= 23
#Peso= 60
#Altura= 1.80
#IMC= Peso/(Altura**2)

#print(f"{Nome} tem {Idade} anos, e seu IMC é de {IMC:0.2f}") # 0.2f -> 2 casas decimais
#print("{} tem {} anos, e seu IMC é de {:0.2f}".format(Nome, Idade, IMC))
#print("{0}, {0} tem IMC de {1:0.2f}".format(Nome, IMC)) #repetir pelo índice {0}, {1}, {2}...
#print("{n} tem {i} anos, e seu IMC é de {IM}".format(n=Nome, i=Idade, IM=IMC)) #outro modo, porém redundante
#print("{0} tem {1} anos, e seu IMC é de {2:0.2f}".format(Nome, Idade, IMC))
#print("Olá Mundo", type("Olá Mundo"))
#Ano_Nascimento=Ano_Atual-Idade -> Calcular idade pela operação de subtração #(+ hora, minutos...)

#ENTRADA DE DADOS DO USUÁRIO:

Nome=input("Qual é o seu nome?")
Idade=input("Qual é a sua idade?")
Peso=int(input("Qual é o seu peso?"))
Altura=float(input("Qual é a sua altura?"))
Altura=float(Altura)

IMC=Peso/(Altura**2)

print(f"{Nome} tem {Idade} anos, e seu IMC é de {IMC:0.2f}")

# Naive solution to count the total number of set bits in 'n'
#def countSetBits(n):

#    count = 0
#    while n:
#        count += (n & 1)   # check last bit
#        n >>= 1
#        return count
#
#x
# if __name__ == '__main__':
#n = 1024
#print(f'The total number of set bits in {str(n)} ({bin(n)}) is {countSetBits(n)}')


