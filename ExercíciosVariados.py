#1-Faça um Programa que mostre a mensagem "Alo mundo" na tela.
x = ("Alo mundo")
print(x)

#2-Faça um Programa que peça um número e então mostre a mensagem O número informado foi [número].
num = float(input("Digite um número: "))
print("O número informado foi", num)

#3-Faça um Programa que peça dois números e imprima a soma.
num1 = float(input("Digite um número: "))
num2 = float(input("Digite um número: "))
sum = num1 + num2 
print(sum)

#4-Faça um Programa que peça as 4 notas bimestrais e mostre a média.

bim1 = float(input("Nota do 1° bimestre: "))
bim2 = float(input("Nota do 2° bimestre: "))
bim3 = float(input("Nota do 3° bimestre: "))
bim4 = float(input("Nota do quarto bimestre: "))
semestre1 = bim1 + bim2 
semestre2 = bim3 + bim4 
media = semestre1 + semestre2 / 2 
print(media)

#5-Faça um Programa que converta metros para centímetros.

metros = float(input("Digite metros: "))
centimetros = metros * 100 
print(centimetros)

#6-Faça um Programa que peça o raio de um círculo, calcule e mostre sua área.

r = float(input("Qual é o raio do círculo?"))
a = r * 3,14 
print(f"A área do círculo é {a}")

#7-Faça um Programa que calcule a área de um quadrado, em seguida mostre o dobro desta área para o usuário.

L = float(input("Digite um número: "))
A = L ** 2 
print("A área do quadrado é", A,"m²")

#8-Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês.

ganho_hora1 = int(input("Quanto você ganha por hora? "))
horas_trabalhadas = int(input("Quantas horas trabalha por mês? "))
salario1 = ganho_hora1 * horas_trabalhadas
print(salario1)


#8.1 O 15° exercício diz assim:Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para o Imposto de Renda, 8% para o INSS e 5% para o sindicato, faça um programa que nos dê:
'''salário bruto.453
quanto pagou ao INSS.
quanto pagou ao sindicato.
o salário líquido.
calcule os descontos e o salário líquido, conforme a tabela abaixo:
+ Salário Bruto : R$ - IR (11%) : R$ - INSS (8%) : R$ - Sindicato ( 5%) : R$ = Salário Liquido : R$
Obs.: Salário Bruto – Descontos = Salário Líquido”'''

valor = int(input('Quanto você ganha por hora: '))
horas = int(input('Número de horas trabalhadas no mês: '))
salario = valor * horas 
ir = (11/100 * salario)

print('Imposto de renda: ', ir)
inss = (8/100 * salario)
print('INSS: ', inss)
sind = (5/100 * salario)
print('Sindicato: ', sind)
desc = ir + inss + sind 
salarioL = salario - desc 
print('O desconto total do salario bruto(',salario,'R$)','foi',desc, '\nO salario liquido ficou, ', salarioL)
#9-Faça um Programa que peça a temperatura em graus Fahrenheit, transforme e mostre a temperatura em graus Celsius.
#C = 5 * ((F-32) / 9).


#10-Faça um Programa que peça a temperatura em graus Celsius, transforme e mostre em graus Fahrenheit.