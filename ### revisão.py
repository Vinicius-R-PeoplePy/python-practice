### revisão 

print(len("A"))
print(len("AB"))
print(len(""))
print(len("O rato roeu a roupa"))

a = "ABCDEF"
print(a[0])
print(a[1])
print(a[5])
#print(a[6])
#print(len[a])

s = "ABC"
print(s + 'C')
print(s + "D" * 4)
print("X" + "-" * 10 + "X")

idade = 22
print("[%d]" %  idade)
print("[%03d]" % idade)
print("[%3d]" % idade)

print("%5f" % 5)
print("%5.2f" % 5)
print("%10.5f" % 5)

nome = "João"
idade = 22
grana = 51.34
print("%s tem %d anos e R$%f no bolso" % (nome, idade, grana))
print("%12s tem %03d anos e R$%5.2f no bolso." % (nome, idade, grana))
print("%-12s tem %-3d anos e R$%-5.2f no bolso." % (nome, idade, grana))

s = "ABCDEFGHI"
print(s[0:2])
print(s[1:2])
print(s[2:4])
print(s[0:5])
print(s[1:8])
print(s[:2])
print(s[1:])
print(s[0:-2])
print(s[:])
print(s[-1])
print(s[-5:7])
print(s[-2:-1])

########

dívida = 0 
compra = 100 
dívida = dívida + compra 
compra = 200 
dívida = dívida + compra 
compra = 300 
dívida = dívida + compra 
compra = 0 
print(f'O valor da dívida é: {dívida}')

########

nome = input("Digite seu nome: ")
print("Você digitou %s" % nome)
print("Olá, %s!" % nome)

########

while True:
    try:
        anos = int(input("Anos de serviço: "))
        valor_por_ano = float(input("Valor por ano: "))
        bônus = anos * valor_por_ano
        print("Bônus de R$ %5.2f" % bônus)
        break 
    except ValueError:
        print("Entrada inválida. Tente novamente.")

########
while True:
    try:
        n1 = int(input("Digite o primeiro número: "))
        n2 = int(input("Digite o segundo número: "))
        soma = (n1) + (n2) 
        print(f"A soma de {n1} e {n2} é igual a {soma}")
        break 
    except ValueError:
        print("Entrada inválida. Tente novamente.")

##########
while True:
    try:
        metros = float(input("Digite um valor em metros: "))
        centímetros = metros*100
        print(f"O valor {metros}m informado, convertido para centímetros, é igual a {centímetros}cm")
        break
    except ValueError:
        print("Entrada inválida. Tente novamente.")

##########
def calcular_segundos(dias, horas, minutos, segundos):
    total_segundos = (dias * 24 * 60 * 60) + (horas * 60 * 60) + (minutos * 60) + segundos
    return total_segundos 

dias = int(input("Digite a quantidade de dias: "))
horas = int(input("Digite a quantidade de horas: "))
minutos = int(input("Digite a quantidade de minutos: "))
segundos = int(input("Digite a quantidade de segundos: "))
               
total_segundos = calcular_segundos(dias, horas, minutos, segundos)

print(f"O total em segundos é: {total_segundos} segundos")

#######
while True:
    try:
        salario_atual = float(input("digite o valor do salaŕio atual : R$ "))
        percentual_aumento = float(input("Digite a porcentagem de aumento: "))

        aumento = salario_atual * (percentual_aumento / 100)
        novo_salario = salario_atual + aumento 

        print(f"Valor do aumento: R$ {aumento:.2f}")
        print(f"Novo salário: R$ {novo_salario:.2f}")
        break 
    except ValueError:
        print("Entrada inválida. Tente novamente.")

#########
while True:
    try:
        preco_mercadoria = float(input("Digite o preço da mercadoria: R$"))
        percentual_desconto = float(input("Digite o percentual de desconto: "))

        valor_desconto = preco_mercadoria * (percentual_desconto / 100)
        preco_a_pagar = preco_mercadoria - valor_desconto 

        print(f"Valor do desconto: R$ {valor_desconto:.2f}")
        print(f"Preço a pagar: R$ {preco_a_pagar:.2f}")
        break 
    except ValueError:
        print("Entrada inválida. Tente novamente.")

#######
while True:
    try:
        distancia = float(input("Digite a distância a percorrer (em km): "))
        velocidade_media = float(input("Diite a velocidade média esperada (em km): "))

        tempo_viagem = distancia / velocidade_media 

        print(f"O tempo estimado de viagem é de {tempo_viagem:.2f} horas.")
        break
    except ValueError:
        print("Entrada inválida. Tente novamente.")

#######
while True:
    try:
        temperatura_celsius = float(input("Digite a temperatura em graus Celsius: "))

        # Converte a temperatura para Fahrenheit usando a fórmula
        temperatura_fahrenheit = (9/5) * temperatura_celsius + 32

        print(f"A temperatura em graus Fahrenheit é: {temperatura_fahrenheit:.2f}")
        break
    except ValueError:
        print("Entrada inválida. Tente novamente.")

########
while True:
    try:
        km_percorridos = float(input("Digite a quantidade de km percorridos: "))
        dias_aluguel = int(input("Digite a quantidade de dias de aluguel: "))

        custo_por_dia = 60
        custo_por_km = 0.15

        preco_a_pagar = (dias_aluguel * custo_por_dia) + (km_percorridos * custo_por_km)

        print(f"O preço a pagar pelo aluguel do carro é: R$ {preco_a_pagar:.2f}")
        break
    except ValueError:
        print("Entrada inválida. Tente novamente.")


###############
while True:
    try:
        cigarros_por_dia = int(input("Digite a quantidade de cigarros fumados por dia: "))
        anos_fumados = int(input("Digite a quantidade de anos que vocẽ já fumou: "))

        perda_de_vida_por_cigarro = 10 

        reducao_tempo_vida_minutos = cigarros_por_dia * perda_de_vida_por_cigarro
        reducao_tempo_vida_dias = reducao_tempo_vida_minutos / (24* 60)

        print(f"Um fumante perderá aproximadamente {reducao_tempo_vida_dias:.2f} dias de vida.")
        break 
    except ValueError:
        print("Entrada inválida. Tente novamente.")

###########
while True:
    try:
        # Solicita o saldo da conta bancária ao usuário 
        saldo = float(input("Digite o saldo da sua conta bancária: "))
        print(f"Saldo da conta bancária: {saldo}")
        break
    except ValueError:
        # Trata o caso em que a conversão para float falha
        print("Entrada inválida. Tente novamente.")

# O programa continua a execução após o bloco try-except
# Aqui você pode usar o valor de 'saldo' se a conversão for bem-sucedida
        

#######
while True:
    try:
        a = int(input("Primeiro valor: "))
        b = int(input("Segundo valor: "))
        if a > b:
            print("O primeiro número é o maior!")
            break
        elif b > a:
            print("O segundo número é o maior")
            break
        else:
            print("Os valores são iguais.")
            break
    except ValueError:
        # Trata o caso em que a conversão para float falha
        print("Entrada inválida. Tente novamente.")

########
while True:
    try:
        idade = int(input("Digite a idade do seu carro: "))
        if idade <= 3:
            print("Seu carro é novo")
        if idade > 3:
            print("Seu carro é velho")
            break
    except ValueError:
        # Trata o caso em que a conversão para float falha
        print("Entrada inválida. Tente novamente.")

# Escreva um programa que pergunte a velocidade do carro de um usuário. Caso ultrapasse 80km/h, exiba uma mensagem dizendo que o usuário foi multado. Nesse caso, exiba o valor da multa, cobrando R$5 por km acima de 80km/h.
while True:
    try:
        velocidade_carro = float(input("Digite a velocidade do carro (em km/h): "))

        # Verifica se a velocidade ultrapassa o limite de 80 km/h
        limite_velocidade = 80
        valor_multa_km_excedido = 5 

        if velocidade_carro > limite_velocidade:
            # Calcula a quantidade de km acima do limite
            km_excedidos = velocidade_carro - limite_velocidade 

            # Calcula o valor da multa 
            valor_multa = km_excedidos * valor_multa_km_excedido

            # Exibe a mensagem de multa e o valor 
            print(f"Você foi multado! Velocidade acima de {limite_velocidade} km/h.")
            print(f"Valor da multa: R$ {valor_multa:.2f}")
        else:
            # Exibe uma mensagem se a velocidade estiver dentro do limite
            print("Velocidade dentro do limite. Dirija com segurança!")
            break
    except ValueError:
        # Trata o caso em que a conversão para float falha
        print("Entrada inválida. Tente novamente.")


########
while True:
    try:
        salário = float(input("Digite o salário para cálculo do imposto: "))
        base = salário 
        imposto = 0 
        if base > 3000:
            imposto = imposto + ((base - 3000)) *0.35
            base = 3000 
        if base > 1000:
            imposto = imposto + ((base - 1000) * 0.20)
        print("Salário: R$%6.2f Imposto a pagar: R$%6.2f" % (salário, imposto))
        break
    except ValueError:
        # Trata o caso em que a conversão para float falha
        print("Entrada inválida. Tente novamente.")

#######
while True:
    try:
        n1 = int(input("Digite o primeiro número: "))
        n2 = int(input("Digite o segundo número: "))
        n3 = int(input("Digite o terceiro número: "))

        if n1 > n2 and n1 > n3:
            print(f'O maior número é {n1}')
            break
        elif n2 > n1 and n2 > n3:
            print(f'O maior número é {n2}')
            break
        elif n3 > n1 and n3 > n2:
            print(f'O maior número é {n3}')
            break
    except ValueError:
        # Trata o caso em que a conversão para float falha
        print("Entrada inválida. Tente novamente.")

#######

# Solicita o salário do funcionário ao usuário 
while True:
    try:
        salario = float(input("Digite o salário do funcionário: R$"))

        # Define as taxas de aumento 
        taxa_aumento_superior = 0.10 # 10% de aumento para salários superiores a R$ 1.250.0
        taxa_aumento_inferior = 0.15 # 15% de aumento para salários iguais ou inferiores a R$1.250.0

        # Verifica o salário e calcula o aumento correspondente
        if salario > 1250.00:
            aumento = salario * taxa_aumento_superior
        else:
            aumento = salario * taxa_aumento_inferior 

        # Calcula o novo saário
        novo_salario = salario + aumento 

        # Exibe os resultados
        print(f"Salário anterior: R$ {salario:.2f}")
        print(f"Valor do aumento: R$ {aumento:.2f}")
        print(f"Novo salário: R$ {novo_salario:.2f}")
        break 
    except ValueError:
        # Trata o caso em que a conversão para float falha
        print("Entrada inválida. Tente novamente.")

#####

# Escreva um programa que pergunte a distância que um passageiro deseja percorrer em km. Calcule o preço da passagem, cobrando R$0,50 por km para viagens de até 200km, e R$ 0,45 para viagens mais longas.

viagem_200 = 200 
preço_viagem_200 = 0.50 # por km 
preço_viagem_maior = 0.45 # por km 
while True:
    try:
        distancia = float(input("Digite a distância que irá percorrer (em km): "))
        if distancia <= viagem_200:
            preço_viagem = distancia * preço_viagem_200
            print(f"O preço da viagem com distância de {distancia}km é de R${preço_viagem}")
            break
        elif distancia > viagem_200:
            preço_viagem = distancia * preço_viagem_maior
            print(f"O preço de viagem com distância de {distancia}km é de R${preço_viagem}")
            break
    except ValueError:
        # Trata o caso em que a conversão para float falha
        print("Entrada inválida. Tente novamente.")


#############

# conta de telefone com três faixas de preço 
while True:
    try:
        minutos = int(input("Quantos minutos você utilizou este mês: "))
        if minutos < 200:
            preço = 0.20
        else:
            if minutos < 400:
                preço = 0.18
            else:
                preço = 0.15
        print("Você vai pagar este mês: R$%6.2f" % (minutos * preço))
        break 
    except ValueError:
        # Trata o caso em que a conversão para float falha
        print("Entrada inválida. Tente novamente.")


#######
while True:
    try:
        categoria = int(input("Digite a categoria do produto: "))
        if categoria == 1:
            preço = 10 
        elif categoria == 2:
            preço = 18  # Fix: Use '=' for assignment, not '=='
        elif categoria == 3:
            preço = 23 
        elif categoria == 4:
            preço = 26 
        elif categoria == 5:
            preço = 31 
        print("O preço do produto é: R${0:.2f}".format(preço))  # Fix: Correct format string placeholder
        break

    except ValueError:
        print("Categoria inválida, digite um valor entre 1 e 5!")

##############


while True:
    try:
        n1 = float(input("Digite um número: "))
        n2 = float(input("Digite outro número: "))
        calc = int(input("""Qual operação deseja realizar?
                        [1] soma
                        [2] subtração
                        [3] multiplicação
                        [4] divisão
                        
                        => """))
        if calc == 1:
            print(n1+n2)
            break
        elif calc == 2:
            print(n1-n2)
            break
        elif calc == 3:
            print(n1*n2)
            break
        elif calc == 4:
            print(n1/n2)
            break
    except ValueError:
        # Trata o caso em que a conversão para float falha
        print("Entrada inválida. Tente novamente.")

####

# Solicita informações ao usuário 
while True:
    try:
        valor_casa = float(input("Digite o valor da casa a comprar: R$ "))
        salario = float(input("Digite o salário: R$"))
        anos_a_pagar = int(input("Digite a quantidade de anos a pagar: "))

        meses_a_pagar = anos_a_pagar * 12

        # Calcula o valor da prestação mensal 
        valor_prestacao = valor_casa / meses_a_pagar 

        # Calcula o limite de 30% do salário para a prestação 
        limite_prestacao = salario * 0.3

        # Verifica se a prestação mensal é inferior ou igual ao limite
        if valor_prestacao <= limite_prestacao:
            print("Empréstimo aprovado!")
            print(f"Valor da prestação mensal: R$ {valor_prestacao:.2f}")
            break
        else:
            print("Empréstimo não aprovado. Valor da prestação excede 30% /do salário.")
            print(f"Limite permitido: R$ {limite_prestacao:.2f}")
            break
    except ValueError:
        # Trata o caso em que a conversão para float falha
        print("Entrada inválida. Tente novamente.")

##########
while True:
    try:
        kwh_consumidos = float(input("Digite a quantidade de kWh consumidos: "))
        tipo_instalacao = input("Digite o tipo de instalação (R para residências, I para indústrias, C para comércios): ")

        preco_residencial = 0.6
        preco_industrial = 0.5
        preco_comercial = 0.7

        # Calcula o preço a pagar de acordo com o tipo de instalação 
        if tipo_instalacao.lower() == 'r':
            preco_total = kwh_consumidos * preco_residencial
            tipo_instalacao_descricao = "Residencial"
        elif tipo_instalacao.lower() == 'i':
            preco_total = kwh_consumidos * preco_industrial
            tipo_instalacao_descricao = "Industrial"
        elif tipo_instalacao.lower() == 'c':
            preco_total = kwh_consumidos * preco_comercial  # Fix: Calculate the total price for commercial installation
            tipo_instalacao_descricao = "Comercial"
        else:
            print("Tipo de instalação inválido. Tente novamente.")
            continue

        # Exibe o resultado
        print(f"\nTipo de instalação: {tipo_instalacao_descricao}")
        print(f"Quantidade de kWh consumidos: {kwh_consumidos} kWh")
        print(f"Preço a pagar: R$ {preco_total:.2f}")
        break
    except ValueError:
        # Trata o caso em que a conversão para float falha
        print("Entrada inválida. Tente novamente.")



#####
x=1
while x<=3:
    print(x)
    x = x + 1

#####

x=100
while x<=100:
    print(x)
    x = x + 1 

######

from time import sleep
print("Contador:")
x=100
while x<100 and x>=50:
    print(x)
    sleep(1)
    x = x + 1 

#####

import time

for i in range(10, 0, -1):
    print(i)
    time.sleep(0.3)

print("Fogo!")

######

import time
x = 50 
while x <= 100:
    print(x)
    time.sleep(0.2)
    x = x + 1 


#####

import time 

def print_numbers():
    while True:
        try:
            fim = int(input("Digite o último número a imprimir: "))
            x = 1 
            while x <= fim:
                print(x)
                time.sleep(1)
                x = x + 1 
        except ValueError:
            print("Entrada inválida. Tente novamente")

        
def print_even_numbers():
    while True:
        try:
            fim = int(input("Digite o último número a imprimir: "))
            x = 0 
            while x <= fim:
                if x % 2 == 0:
                    print(x)
                x = x + 1 
            break 
        except ValueError:
            print("Entrada inválida. Tente novamente")

######

nums = 10
x = 1  
contador_multiplos = 0 

while contador_multiplos < nums:
    if x % 3 == 0:
        print(x)
        contador_multiplos += 1
    x += 1

#####

while True:
    try:
        n = int(input("Tabuade de: "))
        x = 1 
        while x<= 10:
            print(n+x)
            x=x+1
        break
    except ValueError:
        print("Entrada inválida. Tente novamente")

#####
while True:
    try:
        n = int(input("Tabuada de: "))
        x = 1 
        while x <= 10:
            print('=>',n*x)
            x=x+1
        break
    except ValueError:
        print("Entrada inválida. Tente novamente")

####
while True:
    try:
        inicio = int(input("Digite o início da tabuada: "))
        fim = int(input("Digite o fim da tabuada: "))
        x = 1
        while x <= fim:
            print('=>', inicio*x)
            x=x+1
        break
    except ValueError:
        print("Entrada inválida. Tente novamente")

#####
while True:
    try:
        n1= int(input("Digite o primeiro número: "))
        n2= int(input("Digite o segundo número: "))

        resultado = 0 

        for _ in range(n2):
            resultado += n1 

        print(f"O resultado da multiplicação é: {resultado}")
        break
    except ValueError:
        print("Entrada inválida. Tente novamente")

#####
while True:
    try:
        dividendo = int(input("Digite o dividendo (número a ser dividido): "))
        divisor = int(input("Digite o divisor (número pelo qual será dividido): "))

        quociente = 0 
        resto = dividendo

        while resto >= divisor:
            resto -= divisor 
            quociente += 1 

        print(f"A divisão inteira é {quociente}")
        print(f"O resto da divisão é: {resto}")
        break
    except ValueError:
        print("Entrada inválida. Tente novamente")

####

pontos = 0
questão = 1

while questão <= 3:
    resposta = input("Resposta da questão %d: " % questão).lower()

    if questão == 1 and resposta == 'b':
        pontos += 1
    elif questão == 2 and resposta == 'a':
        pontos += 1
    elif questão == 3 and resposta == "d":
        pontos += 1

    questão += 1

print("O aluno fez %d ponto(s)" % pontos)


####

x = 1 
soma = 0 
while x <= 5:
    while True:
        try:
            x = int(input("%d Digite o número:" % x))
            soma = soma + n 
            x = x + 1 
            print("Média: %5.2f" % (soma/5))
            break
        except ValueError:
            print("Entrada inválida. Tente novamente")

####

# Escreva um programa que pergunte o depósito inicial e a taxa de
#juros de uma poupança. Exiba os valores mês a mês para os 24 primeiros meses.
#Escreva o total ganho com juros no período.


while True:
        try:
            deposito_inicial = float(input("Digite o depósito inicial na poupança: R$ "))
            taxa_juros = float(input("Digite a taxa de juros (em %): "))

            taxa_juros_decimal = taxa_juros / 100 

            saldo = deposito_inicial
            total_ganho_juros = 0 

            for mes in range(1, 25):
                juros_mensais = saldo * taxa_juros_decimal

                saldo += juros_mensais 

                print(f"Mês {mes}: Saldo: R$ {saldo:.2f} (Juros: R$ {juros_mensais:.2f})")

                total_ganho_juros += juros_mensais 

            print(f"\nTotal ganho com juros em 24 meses: R$ {total_ganho_juros:.2f}")
            break
        except ValueError:
            print("Entrada inválida. Tente novamente")

######
while True:
        try:
            deposito_inicial = float(input("Digite o depósito inicial na poupança: R$ "))
            taxa_juros = float(input("Digite a taxa de juros (em %): "))
            valor_deposito_mensal = float(input("Digite o valor depositado mensalmente: R$ "))

            taxa_juros_decimal = taxa_juros / 100

            saldo = deposito_inicial 
            total_ganho_juros = 0 

            for mes in range(1, 25):
                saldo += valor_deposito_mensal 

                juros_mensais = saldo * taxa_juros_decimal

                saldo += juros_mensais 

                print(f"Mês {mes}: Saldo: R$ {saldo:.2f} (Juros: R$ {juros_mensais:.2f})")

                total_ganho_juros += juros_mensais 

            print(f"\nTotal ganho com juros em 24 meses: R$ {total_ganho_juros:.2f}")
            break
        except ValueError:
            print("Entrada inválida. Tente novamente")

######
while True:
    try:
        valor_inicial = float(input("Digite o valor inicial da dívida: R$ "))
        juro_mensal = float(input("Digite o juro mensal (em %): "))
        pagamento_mensal = float(input("Digite o valor mensal a ser pago: R$ "))

        juro_mensal_decimal = juro_mensal / 100

        saldo_devedor = valor_inicial
        total_pago = 0
        total_juros_pago = 0
        meses = 0

        while saldo_devedor > 0:
            # Calcula os juros do mês
            juros_mensais = saldo_devedor * juro_mensal_decimal

            # Verifica se o pagamento mensal é insuficiente para cobrir os juros
            if pagamento_mensal <= juros_mensais:
                print("Pagamento mensal insuficiente para cobrir os juros. Ajuste o valor.")
                break

            # Atualiza o saldo devedor com o pagamento mensal antes de juros
            saldo_devedor -= pagamento_mensal

            # Atualiza o saldo devedor com os juros
            saldo_devedor += juros_mensais

            # Garante que o saldo devedor não seja negativo
            saldo_devedor = max(0, saldo_devedor)

            # Atualiza o total pago e total de juros
            total_pago += pagamento_mensal
            total_juros_pago += juros_mensais

            # Incrementa o número de meses
            meses += 1

        # Exibe os resultados
        print(f"\nNúmero de meses para pagar a dívida: {meses} meses")
        print(f"Total pago: R$ {total_pago:.2f}")
        print(f"Total de juros pagos: R$ {total_juros_pago:.2f}")
        break
    except ValueError:
        print("Entrada inválida. Tente novamente")



#######

s = 0 
while True:
    try:
        v = int(input("Digite um número a somar ou 0 para sair: "))
        if v == 0:
            break 
        s = s + v 
        print(s)
    except ValueError:
        print("Entrada inválida. Tente novamente")


######

soma = 0 
quantidade_numeros = 0 

while True:
    try:
        numero = int(input("Digite um número (0 para sair): "))

        if numero == 0:
            break 

        soma += numero 
        quantidade_numeros += 1 

        if quantidade_numeros > 0:
            media = soma / quantidade_numeros
        else:
            media = 0 

        print(f"\nQuantidade de números digitados: {quantidade_numeros}")
        print(f"Soma dos números digitados: {soma}")
        print(f"Média aritmética dos números digitados: {media:.2f}")
        break
    except ValueError:
            print("Entrada inválida. Tente novamente")

#####

total_compras = 0 

while True:
    try:
        codigo_produto = int(input("Digite o código do produto (ou 0  para encerrar): "))

        if codigo_produto == 0:
            break 

        quantidade_comprada = int(input("Digite a quantidade comprada: "))

        if codigo_produto == 1:
            preco_unitario = 0.50
        elif codigo_produto == 2:
            preco_unitario = 1.00
        elif codigo_produto == 3:
            preco_unitario = 4.00
        elif codigo_produto == 5:
            preco_unitario = 7.00
        elif codigo_produto == 9:
            preco_unitario = 8.00 
        else:
            print("Código inválido!")
            continue 

        total_item = quantidade_comprada * preco_unitario 

        total_compras += total_item

        print(f"\nTotal das compras: R$ {total_compras:.2f}")
        break 
    except ValueError:
            print("Entrada inválida. Tente novamente")



####

# listagem de cédulas
while True:
    try:
        valor = int(input("Digite o valor a pagar: "))
        cédulas = 0
        atual = 50

        while valor > 0:
            if atual <= valor:
                valor -= atual
                cédulas += 1
            else:
                print("%d cédula(s) de R$%d" % (cédulas, atual))
                atual = 20 if atual == 50 else 10 if atual == 20 else 5 if atual == 10 else 1

        if valor == 0:
            break

    except ValueError:
        print("Entrada inválida. Tente novamente")





#####

# impressão tabuadas
tabuada = 1
while tabuada <= 10:
    número = 1  
    while número <= 10:
        print("%d x %d = %d" % (tabuada, número, tabuada * número))
        número+=1
    tabuada+=1 

######
# impressão de tabuadas sem repetições aninhadas 

tabuada = 1 
número = 1 
while tabuada <= 10:
    print("%d x %d = %d" % (tabuada, número, tabuada * número))
    número += 1 
    if número == 11:
        número = 1 
        tabuada+=1 

#######

tabuada = 1 

while True:
    numero = 1 

    while numero <= 10:
        print("%d x %d = %d" % (tabuada, numero, tabuada * numero))
        numero += 1 
    try: 
        tabuada = int(input("\nDigite a tabuada desejada (ou 0 para sair): "))

        if tabuada == 0:
            break 
    except ValueError:
            print("Entrada inválida. Tente novamente")

####

while True:
    print("\nEscolha a operação: ")
    print("1. Adição")
    print("2. Subtração")
    print("3. Multiplicação")
    print("4. Divisão")
    print("5. Sair")

    escolha = input("Digite o número da operação desejada (ou '5' para sair): ")

    if escolha == '5':
        print("Programa encerrado.")
        break 
    elif escolha in ('1', '2', '3', '4'):
        try:
            numero = int(input("Digite o número para exibir a tabuada: "))

            for i in range(1, 11):
                if escolha == '1':
                    resultado = numero + i
                    operacao = 'Adição'
                elif escolha == '2':
                    resultado = numero - i 
                    operacao = 'Subtração'
                elif escolha == '3':
                    resultado = numero * i 
                    operacao = 'Multiplicação'
                elif escolha == '4':
                    resultado = numero / i 
                    operacao = 'Divisão'

                print(f"{numero} {operacao} {i} = {resultado}")
        except ValueError:
            print("Entrada inválida. Tente novamente")
    else:
        print("Opção inválida. Por favor, escolha uma opção válida.")

#######

def eh_primo(numero):
    if numero < 2:
        return False 
    elif numero == 2:
        return True 
    elif numero % 2 == 0:
        return False 
    else:
        for i in range(3, int(numero**0.5) + 1, 2):
            if numero % i == 0:
                return False 
        return True 

while True:
    try:  
        numero = int(input("Digite um número para verificar se é primo: "))

        if eh_primo(numero):
            print(f"{numero} é um número primo.")
        else:
            print(f"{numero} não é um número primo.")
        
        break  # Move the break outside of the if-else block

    except ValueError:
        print("Entrada inválida. Tente novamente")



#####

def eh_primo(numero):
    if numero < 2:
        return False
    elif numero == 2:
        return True 
    elif numero % 2 == 0:
        return False 
    else:
        for i in range(3, int(numero*0.5) + 1, 2):
            if numero % i == 0:
                return False
        return True  

try:
    n = int(input("Digite a quantidade de números primos a serem impressos: "))
    numeros_primos = []
    numero = 2
    while len(numeros_primos) < n:
        if eh_primo(numero):
            numeros_primos.append(numero)
        numero += 1  # Move the increment outside the if block

except ValueError:
    print("Entrada inválida. Tente novamente")


########
while True:
    try:
        def raiz_quadrada_aproximada(numero):
            p = 2.0

            while abs(numero - p**2) >= 0.0001:
                p = (p + numero/p) / 2.0 

            return p 

        numero = float(input("Digite um número para calcular a raiz quadrada: "))

        resultado_aproximado = raiz_quadrada_aproximada(numero)

        print(f"A raiz quadrada aproximada de {numero} é {resultado_aproximado:.4f}")
        break
    except ValueError:
        print("Entrada inválida. Tente novamente")



#######
while True:
    try:
        def resto_divisao_inteira(dividendo, divisor):
            while dividendo >= divisor:
                dividendo -= divisor 
            return dividendo 

        dividendo = int(input("Digite o dividendo: "))
        divisor = int(input("Digite o divisor: "))

        resto = resto_divisao_inteira(dividendo, divisor)

        print(f"O resto da divisão inteira de {dividendo} por {divisor} é {resto}")
        break
    except ValueError:
        print("Entrada inválida. Tente novamente")


########
while True:
    try:
        def eh_palindromo(numero):
            numero_str = str(numero)

            return numero_str == numero_str[::-1]

        numero = int(input("Digite um número para verificar se é palíndromo: "))

        if eh_palindromo(numero):
            print(f"{numero} é um número palíndromo.")
            break
        else:
            print(f"{numero} não é palíndromo.")
            break
    except ValueError:
        print("Entrada inválida. Tente novamente")

#####
# Cálculo da média
notas=[6,7,5,8,9]
soma=0
x=0
while x<5:
    soma += notas[x]
    x+=1
print("Média: %5.2f" % (soma/x))

####
# Cálculo da média com notas digitadas

'''notas=[0,0,0,0,0]
soma=0
x=0
while x<5:
    notas[x]=float(input("Nota %d:" % x))
    soma += notas[x]
    x+=1
x=0
while x<5:
    print("Nota %d: %6.2f" % (x, notas[x]))
    print("Média: %5.2f" % (soma/x)) ## erro float division by zero'''

#####

# apresentação de números 

'''números=[0,0,0,0,0]
x=0
while x<5:
    números[x]=int(input("Número %d:"e
     % (x+1)))
    x+=1
while True:
    escolhido=int(input("Que posição você quer imprimir (0 para sair: )"))
    if escolhido == 0:
        break 
    print("Você escolheu o número: %d" % (números[escolhido-1]))'''

#####

# cópia de listas

L=[1,2,3,4,5]
V=L[:]
V[0]=6
print(L)
print(V)

#####

# Fatiamento de listas

L=[1,2,3,4,5]
print(L[0:5])
print(L[:5])
print(L[:-1])
print(L[1:3])
print(L[1:4])
print(L[:3])
print(L[-1])
print(L[-2])

######

L=[12,9,5]
print(len(L))

V = []
print(len(V))

####

L=[1,2,3]
x=0
while x < 3:
    print(L[x])
    x+=1

######

L=[1,2,3]
x=0
while x <len(L):
    print(L[x])
    x+=1

######

L=[]
L.append("a")
print(L)
L.append('b')
print(L)
L.append("c")
print(L)
print(len(L))

# Adição de elementos à lista
while True:
    try:
        L=[]
        n=int(input("Digite um número (0 sai): "))
        if n == 0:
            break 
        L.append(n)
        x=0
        while x < len(L):
            print(L[x])
            break
            x=x+1
    except ValueError:
        print("Entrada inválida. Tente novamente")

####

L=[]
L=L+[1]
print(L)
L+=[2]
print(L)
L+=[3,4,5]
print(L)

#####

# adição de elementos e listas

L=['a']
L.append('b')
print(L)
L.extend(['c'])
print(L)
L.append(['d', 'e'])
print(L)
L.extend(['f','g','h'])
print(L)

# adição de elementos e listas com append

L=['a']
L.append(['b'])
L.append(['c', 'd'])
print(len(L))
print(L[1])
print(L[2])
print(len(L[2]))
print(L[2][1])


###
# Faça um programa que leia duas listas e que gere uma terceira com
#os elementos das duas primeiras

def gerar_terceira_lista(lista1, lista2):
    terceira_lista = lista1 + lista2 
    return terceira_lista 

entrada_lista1 = input("Digite os elementos da primeira lista separados por espaço: ")
lista1 = [int(elemento) for elemento in entrada_lista1.split()]

entrada_lista2 = input("Digite os elementos da segunda lista separados por espaço: ")
lista2 = [int(elemento) for elemento in entrada_lista2.split()]

terceira_lista = gerar_terceira_lista(lista1, lista2)

print("Terceira lista gerada: ", terceira_lista)

#####

def gerar_terceira_lista_sem_repeticao(lista1, lista2):
    terceira_lista = list(set(lista1 + lista2))
    return terceira_lista

lista1 = input("Digite os elementos da primeira lista separados por espaço: ").split()
lista2 = input("Digite os elementos da segunda lista separados por espaço: ").split()

lista1 = [int(elemento) for elemento in lista1]
lista2 = [int(elemento) for elemento in lista2]

terceira_lista_sem_repeticao = gerar_terceira_lista_sem_repeticao(lista1, lista2)

print("Terceira lista sem elementos repetidos:", terceira_lista_sem_repeticao)


#####

# Remoção de elementos da lista

L=['a' ,'b', 'c']
del L[1]
print(L)
del L[0]
print(L)

####

L=list(range(101))
del L[1:99]
print(L) # [0, 99, 100]

#######

# Simulação de uma fila de banco

último = 10 
fila = list(range(1, último+1))
while True:
    print("\nExistem %d clientes na fila" % len(fila))
    print("Fila atual", fila)
    print("Digite F para adicionar um cliente ao fim da fila,")
    print("ou A para realizar o atendimento. S para sair. ")
    operação = input("Operação(F, A ou S): ")
    if operação == 'A':
        if(len(fila))>0:
            atendido = fila.pop(0)
            print("Cliente %d atendido" % atendido)
        else:
            print("Fila vazia! Ninguém para atender.")
    elif operação == 'F':
        último+=1 # Incrementa o ticket do novo cliente
        fila.append(último)
    elif operação == "S":
        break 
    else:
        print("Operação inválida! Digite apenas F, A ou S!")

# Em uma fila, o primeiro elemento é retirado primeiro.
# Já em pilhas, retira-se a partir do último elemento. 
# (utilizando pop(-1))

prato = 5
pilha = list(range(1,prato+1))
while True:
    print("\nExistem %d pratos na pilha" % len(pilha))
    print("Pilha atual:", pilha)
    print("Digite E para empilhar um novo prato,")
    print("ou D para desempilhar, S para sair.")
    operação = input("Operação (E, D ou S):")
    if operação == "D":
        if(len(pilha))>0:
            lavado = pilha.pop(-1)
            print("Prato %d lavado" % lavado)
        else:
            print("Pilha vazia! Nada para lavar.")
    elif operação == "E":
        prato+=1 # novo prato
        pilha.append(prato)
    elif operação == "S":
        break
    else:
        print("Operação inválida!Digite apenas E, D ou S!")


######
'''User
Faça um programa que leia uma expressão com parênteses. Usando
pilhas, verifique se os parênteses foram abertos e fechados na ordem correta.
Exemplo:
(()) OK
()()(()()) OK
()) Erro'''

def verifica_parenteses(expressao):
    pilha = []

    for caractere in expressao:
        if caractere == '(':
            pilha.append(caractere)
        elif caractere == ')':
            if not pilha:
                return False
            pilha.pop()

    return not pilha # Se a pilha estiver vazia, todos os parênteses foram fechados corretamente

expressao = input("Digite a expressão com parênteses: ")

# Chama a função para verificar se os parênteses estão correntos 
if verifica_parenteses(expressao):
    print("Os parênteses estão na ordem correta.")
else:
    print("Erro na ordem dos parênteses")

'''Neste programa, uma pilha é utilizada para rastrear os parênteses abertos. Para cada parêntese de abertura encontrado, é adicionado à pilha. Para cada parêntese de fechamento encontrado, é verificado se há um parêntese de abertura correspondente na pilha. Se a pilha estiver vazia no final do processamento, todos os parênteses foram abertos e fechados corretamente. '''

###
# pesquisa sequencial 
'''while True:
    try:
        L=[15,7,27,39]
        p=int(input("Digite o valor a procurar: "))
        achou=False 
        x=0
        while x<len(L):
            if L[x]==p:
                achou=True 
                break 
            x+=1
        if achou:
            print("%d achado na posição %d" % (p, x))
            break
        else:
            print("%d não encontrado" % p)
            break
    except ValueError:
        print("Entrada inválida. Tente novamente.")'''

#####

'''L = [15, 7, 27, 39]

while True:
    try:
        p = int(input("Digite o valor a procurar: "))

        if p in L:
            position = L.index(p)
            print("%d achado na posição %d" % (p, position))
            break 
        else:
            print("%d não encontrado. Tente novamente." % p)
            break
    except ValueError:
        print("Entrada inválida. Tente novamente.")'''


#######

'''L = [15, 7, 27, 39]
while True:
    try:
        p = int(input("Digite o valor a procurar: "))

        x = 0 
        while x < len(L) and L[x] != p:
            x +=  1

        if x < len(L):
            print("%d achado na posição %d" % (p, x))
            break
        else:
            print("%d não encontrado" % p)
            continue 
    except ValueError:
        print("Entrada inválida. Tente novamente.")'''


######

'''L = [15, 7, 27, 39]

while True:
    try:
        p = int(input("Digite o valor a procurar: "))

        for index, value in enumerate(L):
            if value == p:
                print("%d achado na posição %d" % (p, index))
                break
        else:
            print("%d não encontrado. Tente novamente." % p)
            continue

        break  # Break out of the outer loop if a valid value is found

    except ValueError:
        print("Entrada inválida. Tente novamente.")'''


'''Pesquisar dois valores. Em vez de apenas
p, leia outro valor v que também será procurado. Na impressão, indique qual dos
dois valores foi achado primeiro. Com loop.
'''
L = [15, 7, 27, 39]

while True:
    try:
        p = int(input("Digite o primeiro valor a procurar: "))
        v = int(input("Digite o segundo valor a procurar: "))
        x = 0 

        while x < len(L):
            if L[x] == p:
                print("%d achado na posição %d primeiro." % (p, x))
                break 
            elif L[x] == v:
                print("%d achado na posição %d primeiro." % (v, x))
                break
            elif L[x] == v:
                print("%d achado na posição %d primeiro." % (v, x))
                break 
            x += 1 
        else:
            print("Nenhum dos valores encontrados. Tente novamente.")
            continue 

        break 
    except ValueError:
        print("Entrada inválida. Tente novamente.")

####

L = [15, 7, 27, 39]

while True:
    try:
        p = int(input("Digite o valor 'p' a procurar: "))
        v = int(input("Digite o valor 'v' a procurar: "))
        posicao_p = None
        posicao_v = None 

        for idx, elemento in enumerate(L):
            if elemento == p and posicao_p is None:
                posicao_p = idx 
            elif elemento == v and posicao_v is None:
                posicao_v = idx 

            if posicao_p is not None and posicao_v is not None:
                break 


        if posicao_p is not None:
            print("Valor 'p' encontrado na posição:", posicao_p)
        else:
            print("Valor 'p' não encontrado na lista.")

        if posicao_p is not None:
            print("Valor 'p' encontrado na posição:", posicao_v)
        else:
            print("Valor 'v' não encontrado na lista.")

        break
    except ValueError:
        print("Entrada inválida. Tente novamente.")

######

L=[8,9,15]
for e in L:
    print(e)

########

L=[8,9,15]
x=0
while x<len(L):
    e=L[x]
    print(e)
    x+=1

#######

while True:
    try:
        L=[7,9,10,12]
        p=int(input("Digite um número a pesquisar: "))
        for e in L:
            if e == p:
                print("Elemento encontrado!")
                break
        else:
            print("Elemento não encontrado.")
            continue
        break
    except ValueError:
        print("Entrada inválida. Tente novamente.")


#############

for v in range(5, 8):
    print(v)

############

for t in range (3, 33, 3):
    print(t, end= " ")
print()

######

L=list(range(100,1100,50))
print(L)

########

L=[5,9,13]
x=0
for e in L:
    print("[%d] %d" % (x,e))

######

L=[5,9,13]
for x, e in enumerate(L):
    print("[%d] %d" % (x,e))

#######

L = [1,7,2,4]
máximo = L[0]
for e in L:
    if e > máximo:
        máximo = e 
print(máximo)

########

L = [1,7,2,4]
mínimo=L[0]
for e in L:
    if e <= mínimo:
        mínimo = e
print(mínimo) 

#######



'''A lista de temperaturas de Mons, na Bélgica, foi armazenada na lista
T = [ -10, -8, 0, 1, 2, 5, -2, -4]. Faça um programa que imprima a menor e a maior
temperatura, assim como a temperatura média.
'''


T = [-10, -8, 0, 1, 2, 5, -2, -4]

# Encontrar a menor temperatura
mínima = min(T)

# Encontrar a maior temperatura
máxima = max(T)

# Calcular a temperatura média
média = sum(T) / len(T)

# Imprimir os resultados
print("Menor temperatura:", mínima)
print("Maior temperatura:", máxima)
print("Temperatura média:", média)

#########

V = [9, 8, 7, 12, 0, 13, 21]
P = []
I = []

for e in V:  # Use 'V' instead of 'v'
    if e % 2 == 0:
        P.append(e)
    else:
        I.append(e)

print("Pares: ", P)
print("Ímpares: ", I)


'''
Controle da utilização de salas de um cinema
'''

lugares_vagos=[10,2,1,3,0]
while True:
    try:
        sala = int(input("Sala (0 sai): "))
        
        if sala == 0:
            print("Fim")
            break
            
        if sala > len(lugares_vagos) or sala < 1:
            print("Sala inválida")
            continue
        
        elif lugares_vagos[sala-1] == 0:
            print("Desculpe, sala lotada!")
            continue
        
        else:
            lugares_disponiveis = lugares_vagos[sala-1]
            lugares = int(input("Quantos lugares você deseja (%d vagos): " % lugares_disponiveis))
            
            if lugares > lugares_disponiveis:
                print("Esse número de lugares não está disponível.")
                continue
                
            elif lugares < 0:
                print("Número inválido")
                continue
                
            else:
                lugares_vagos[sala-1] -= lugares
                print("%d lugares vendidos" % lugares)
                
                print("Utilização das salas") 
                for x, l in enumerate(lugares_vagos):
                    print("Sala %d - %d lugar(es) vazio(s)" % (x+1, l))
                break

    except ValueError:
        print("Entrada inválida. Tente novamente.")

#############

S=["maçãs", "peras", "kiwis"]
print(len(S))
print(S[0])
print(S[1])
print(S[2])

###########


compras = []
while True:
    produto=input("Produto (fim para sair): ")
    if produto == "fim":
        break 
    compras.append(produto)
for p in compras:
    print(p)


###########

# lsitas com strings, acessando letras 

S = ["maçãs", "peras", "kiwis"]
print(S[0][0])  # First character of the first string
print(S[0][1])  # Second character of the first string
print(S[1][1])  # Second character of the second string
print(S[2][2])  # Third character of the third string


#############

'''
Impressão de uma lista de strings, letra a letra
'''

L=["maçãs", "peras", "kiwis"]
for s in L:
    for letra in s:
        print(letra )

###########

produto1 = ["maçã", 10, 0.30]
produto2 = ["pera", 5, 0.75]
produto3 = ["kiwi", 4, 0.98]
compras = [produto1, produto2, produto3]
for e in compras:
    print("Produto: %s" % e [0])
    print("Quantidade: %d" % e[1])
    print("Preço: %5.2f" % e[2])

########

compras = []
while True:
    try:
        produto = input("Produto (fim para sair): ")
        if produto == "fim":
            break
        quantidade = int(input("Quantidade: "))
        preço = float(input("Preço: "))
        compras.append([produto, quantidade, preço])
        soma = 0.0
        for e in compras:
            print("%20s x%5d %5.2f %6.2f" % (e[0],
                        e[1],e[2],
                        e[1] * e[2]))
            soma += e[1] * e[2]
            print("Total: %7.2f" % soma)
            break
    except ValueError:
        print("Entrada inválida. Tente novamente.")

####

L=[7,4,3,12,8]
fim=5 #1
while fim >1: #2
    trocou=False #3
    x=0 #4
    while x<(fim-1): #5
        if L[x] > L[x+1]: #6
            trocou=True #7
            temp=L[x] #8
            L[x]=L[x+1]
            L[x+1]=temp
        x+=1
    if not trocou:#9
        break 
    fim-=1 #10
for e in L:
    print(e)

'''Em ❶, utilizamos a variável fim para marcar a quantidade de elementos da lista. Precisamos marcar 
o fim ou a posição do último elemento porque no “Bubble Sort” não precisamos 
verificar o último elemento após uma passagem completa. Em ❷, verificamos se 
fim > 1, pois como comparamos o elemento atual(L[x]) com o seguinte(L[x+1]), 
precisamos de, no mínimo, dois elementos. Utilizamos a variável trocou em ❸
para indicar que não realizamos nenhuma troca. O valor de trocou será utilizado 
mais tarde para verificar se já temos a lista ordenada ou não. A variável x ❹ será 
utilizada como índice, começando da posição 0. Nossa condição do segundo 
while ❺ é especial, pois temos que garantir um próximo elemento para comparar 
com o atual. Isso faz com que a condição de saída desse while seja x<(fim-1), ou 
melhor, que x seja anterior ao último elemento. Em ❻ temos a comparação em 
si, onde x é nossa posição atual, e o próximo elemento é o de índice x+1. Como 
estamos ordenando em ordem crescente, desejamos que o próximo elemento 
sempre seja maior que o atual, dessa forma garantindo a ordenação da lista. 
Como comparamos apenas dois elementos de cada vez, temos que visitar a lista 
várias vezes, até que todos os elementos estejam em suas posições. Se a condição 
de ❻ for verdadeira, esses elementos estão fora de ordem. Nesse caso, devemos 
inverter ou trocar a posição dos dois elementos. Em ❼ marcamos que efetuamos 
uma troca e, em ❽, utilizamos uma variável auxiliar ou temporária para trocar 
os dois valores de posição.'''


'''Modifique o programa da listagem 6.44 para ordenar a lista em 
ordem decrescente. L=[1,2,3,4,5] deve ser ordenada como L=[5,4,3,2,1]'''

L = [7, 4, 3, 12, 8]
n = 5

while n > 1:
    trocou = False 
    x = 0 

    while x < (n - 1):
        if L[x] < L[x+1]:
            trocou = True
            temp = L[x] 
            L[x] = L[x + 1]
            L[x + 1] = temp 
        x += 1 
    
    if not trocou:
        break 

    n -= 1 

for e in L:
    print(e)


#####

tabela = { "Alface": "R$0.45",
          "Batata": "R$1.20",
          "Tomate": "R$2.30",
          "Feijão": "R$1.50"}
print(tabela["Tomate"])
print("Manga" in tabela)
print("Batata" in tabela)

####

tabela = { "Alface": "R$0.45",
          "Batata": "R$1.20",
          "Tomate": "R$2.30",
          "Feijão": "R$1.50"}
while True:
    produto=input("Digite o nome do produto, fim para terminar:")
    if produto == 'fim':
        break 
    if produto in tabela:
        print("Preço %5.2f" % tabela[produto])
    else:
        print("Produto não encontrado!")

del tabela["Tomate"]
print(tabela)

#############

estoque = { "tomate": [1000, 2.30],
           "alface": [500, 0.45],
           "batata": [2001, 1.20],
           "feijão": [100, 1.50]}
venda = [ ["tomate", 5], ["batata", 10], ["alface",5] ]
total = 0 
print("Vendas:\n")
for operação in venda:
    produto, quantidade = operação
    preço = estoque[produto][1]
    custo = preço * quantidade 
    print("%121s: %3d x%6.2f = %6.2f" % (produto, quantidade, preço, custo))
    estoque[produto][0] -= quantidade 
    total+=custo 
print("Custo total: %21.2f\n" % total)
print("Estoque:\n")
for chave, dados in estoque.items():
    print("Descrição: ", chave)
    print("Quantidade: ", dados[0])
    print("Preço: %6.2f\n" % dados[1])

#####

estoque = {
    "alface": [500, 0.45],
    "batata": [2001, 1.20],
    "feijão": [100, 1.50]
}

venda = []
total = 0 

while True:
    try:
        produto = input("Digite o nome do produto (ou 'sair' para encerrar): ").lower()

        if produto.lower() == 'sair':
            break 

        if produto in estoque:
            try:
                quantidade = int(input(f"Digite a quantidade de {produto} vendida: "))
            except ValueError:
                print("Por favor, digite uma quantidade válida.")
                continue 
            
            preço = estoque[produto][1]
            custo = preço * quantidade 

            print(f"\n{produto}: {quantidade} x {preço:.2f} = {custo:.2f}\n")
            estoque[produto][0] -= quantidade 
            total += custo 
            venda.append([produto, quantidade])
        else:
            print("Produto não encontrado. Por favor, digite um produto válido.\n")
            continue
    except ValueError:
        print("Entrada inválida. Tente novamente.")

print("Vendas:\n")
for operação in venda:
    produto, quantidade = operação 
    preço = estoque[produto][1]
    custo = preço * quantidade 
    print(f"{produto}: {quantidade} x {preço:.2f} = {custo:.2f}")

print(f"\nCusto total: {total:.2f}\n")

print("Estoque:\n")
for chave, dados in estoque.items():
    print("Descrição:", chave)
    print("Quantidade:", dados[0])
    print(f"Preço: {dados[1]:.2f}\n")


######

frase = input("Digite uma frase: ")

# Inicializa um dicionário vazio para armazenar a contagem dos caracteres

# Inicializa um dicionário vazio para armazenar a contagem dos caracteres
contagem_caracteres = {}

# Itera sobre cada caractere na frase
for caractere in frase:
    # Verifica se o caractere já está no dicionário 
    if caractere in contagem_caracteres:
        # Se sim, incrementa a contagem 
        contagem_caracteres[caractere] += 1 
    else:
        # Se não, adiciona o caractere ao dicionário com contagem 1
        contagem_caracteres[caractere] = 1 

# Exibe o dicionário resultante
print("Contagem de caracteres na frase: ")
print(contagem_caracteres)


#####

tupla = ('a', 'b', 'c')
print(tupla)

#####

print(tupla[0])

#####

print(tupla*2)
print(len(tupla))

for e in tupla:
    print(e)

#####

a, b = 10, 20
a, b = b, a 
print(a)

######

t4=()
print(len(t4))

#######

L=[1,2,3]
T=tuple(L)
print(T)


#####

t1=(1,2,3)
t2=(4,5,6)
print(t1+t2)

#####

tupla=("a", ["b", "c", "d"])
print(tupla)
print(len(tupla))
print(tupla[1]) # ["b", "c", "d"]
tupla[1].append('e')
print(tupla)

######

L=list("Alô mundo")
L[0]="a"
print(L)
s="".join(L)
print(s)

#######

nome="João da Silva"
print(nome.startswith("João")) # True
print(nome.startswith("joão")) # False
print(nome.endswith("Silva")) # True

####

s="O Rato roeu a roupa do Rei de Roma"
print(s.lower())
print(s.upper())
print(s.lower().startswith("o rato")) # True
print(s.upper().startswith("O RATO")) # True

#####

s="Maria Amélia Souza"
print("Amélia" in s)
print("Maria" in s)
print("Souza" in s)
print("a A" in s)
print("amélia" in s)

######

s="Todos os caminhos levam a Roma"
print("levam" not in s) # False
print("Caminhos" not in s) # True
print("AS" not in s) # True 

#####

s="João comprou um carro"
print("joão" in s.lower()) # True
print("CARRO" in s.upper()) # True
print("comprou" not in s.lower()) # False
print("barco" not in s.lower()) # True

######

t="um tigre, dois tigres, três tigres"
print(t.count("tigre"))
print(t.count("tigres"))
print(t.count("t"))
print(t.count("z"))

#####

s="Alô mundo"
print(s.find("mun")) # 4
print(s.find("ok")) # -1 

'''
Se o objetivo for pesquisar, mas da direita para a esquerda, utilize o método rfind
'''

s="Um dia de sol"
print(s.rfind("d"))#7
print(s.find("d")) #3

#####

s="um tigre, dois tigres, três tigres"
print(s.find("tigres"))
print(s.rfind("tigres"))
print(s.find("tigres", 7)) #início=7
print(s.find("tigres", 30)) #início=30
print(s.find("tigres",0,10)) #início=0 fim=10

######
s="um tigre, dois tigres, três tigres"
p=0
while(p>-1):
    p=s.find("tigre", p)
    if p>=0:
        print("Posição: %d" % p)
        p+=1

############

str1 = input("Digite a primeira string: ")
str2 = input("Digite a segunda string: ")

posicao_inicio = str1.find(str2)

if posicao_inicio != -1:
    print(f"{str1} encontrado na posição {posicao_inicio + 1} de {str1}")
else:
    print(f"{str2} não encontrado em {str1}")

############

str1 = input("Digite a primeira string: ")
str2 = input("Digite a segunda string: ")

# Inicializa uma string vazia para armazenar os caracteres comuns
string_comum = ""

# Itera sobre cada caractere na primeira string 
for caractere in str1:
    # Verifica se o caractere está presente na segunda string e não foi adicionado ainda
    if caractere in str2 and caractere not in string_comum:
        # Adiciona o caractere à string comum 
        string_comum += caractere 

# Imprime o resultado 
print("Resultado: ", string_comum)

#############

# Solicita ao usuário para inserir as duas strings
str1 = input("Digite a primeira string: ")
str2 = input("Digite a segunda string: ")

# Cria um conjunto com os caracteres únicos de ambas as strings
caracteres_unicos = set(str1) | set(str1)

string_comum = ''.join(caracteres_unicos)

print("Resultado:", string_comum)

######

string = input("Digite uma string: ")

contagem_caracteres = {}

for caractere in string:
    if caractere in contagem_caracteres:
        contagem_caracteres[caractere] += 1 
    else:
        contagem_caracteres[caractere] = 1 

print("Resultado:")
for caractere, contagem in contagem_caracteres.items():
    print(f"{caractere}: {contagem}x")

#########

'''Escreva um programa que leia duas strings e gere uma terceira, na 
qual os caracteres da segunda foram retirados da primeira.
1ª string: AATTGGAA
2ª string: TG
3ª string: AAAA'''

str1 = input("Digite a primeira string: ")
str2 = input("Digite a segunda string: ")

caracteres_resultantes = [] 

for caractere in str1:
    if caractere not in str2:
        caracteres_resultantes.append(caractere)

string_resultante = ''.join(caracteres_resultantes)

print("Resultado: ", string_resultante)


'''Escreva um programa que leia três strings. Imprima o resultado da 
substituição na primeira, dos caracteres da segunda pelos da terceira.
1ª string: AATTCGAA
2ª string: TG
3ª string: AC
Resultado: AAAACCAA
'''

str1 = input("Digite a primeira string: ")
str2 = input("Digite a segunda string: ")
str3 = input("Digite a terceira string: ")

resultado_substituicao = ""

for caractere in str1:
    # Verifica se o caractere está presente na segunda string
    if caractere in str2:
        indice_substituicao = str2.index(caractere)
        if indice_substituicao < len(str3):
            resultado_substituicao += str3[indice_substituicao]
        else:
            # Adiciona o caractere original se o índice for maior ou igual ao comprimento de str3
            resultado_substituicao += caractere
    else:
        resultado_substituicao += caractere 

print("Resultado:", resultado_substituicao)


######

s="tigre"
print("X"+s.center(10)+"X")
print("X"+s.center(10,".")+"X")
print(s.ljust(20))
print(s.rjust(20))
print(s.ljust(20,"."))
print(s.rjust(20,"-"))

# Essas funções são úteis quando precisamos criar relatórios ou simplesmente alinhar a saída dos programas

s="um tigre, dois tigres, três tigres"
print(s.split(","))
print(s.split(" "))
print(s.split())

######

m = "Uma linha\noutra linha\ne mais uma\n"
print(m.splitlines()) 
#['Uma linha', 'outra linha', 'e mais uma']

s = "um tigre, dois tigres, três tigres"
print(s.replace("tigre", "gato"))
print(s.replace("tigre", "gato", 1))
print(s.replace("tigre", "gato", 2))
print(s.replace("tigre", ""))
print(s.replace("","-"))

s="...///Olá///..."
print(s.lstrip("."))
print(s.rstrip("."))
print(s.strip("."))
print(s.strip("./"))

##########

s='125'
p='alô mundo'
s.isalnum() # true
p.isalnum() # false
s.isalpha() # false
s.isalpha() #false

umterço = "\u2153"
novetibetano="\u0f29"
umterço.isdigit()

########

print("771".isdigit())
print("10.4".isdigit())
print("+10".isdigit())
print("-5".isdigit())

s="ABC"
p='abc'
e='aBc'
print(s.isupper)
print(s.islower())
print(p.isupper())
print(p.islower())
print(e.isupper())
print(e.islower())

print("\t\n\r   ".isspace())
print("\tAlô".isspace())

print("\n\t".isprintable())
print("\nAlô".isprintable())
print("Alô mundo".isprintable())

###########

print("{0} {1}".format("Alô", "Mundo"))
print("{0} x {1} R${2}".format(5,"maçã", "1.20"))
# '5 x maçã R$1.20'

print("{0} {1} {0}".format("-","x"))

print("{1} {0}".format("primeiro", "segundo"))
# ' segundo primeiro '

print("{0:10} {1}".format("123", "456"))
#'123       456'
print("X{0:10}X".format("123"))
# 'X123     X'
print("X{0:10}X".format("123456789012345"))
# 'X123456789012345'

print("X{0:<10}X".format("123"))
#X123   X'
print("X{0:>10}X".format("123"))
#'X         123X'

print("X{0:^10}X".format("123"))
#'X     123     X'

print("X{0:.<10}X".format("123"))
#'X123..........X'
print("X{0:!>10}X".format("123"))
#'X!!!!!!!!123X'
print("X{0:*^10}X".format("123"))
#'X***123***X'

print("{0[0]} {0[1]}".format(["123", "456"]))
#'123 456'

'''print("{nome} {0[telefone]}".format({"telefone": 572, "nome": "Maria"}))
e":"Maria"}))
# Maria 572'''

print("{0:*^7}".format(32))
print("{0:*^10}".format(123))
print("{0:*>10}".format(123))
print("{0:10,}".format(7532))
print("{0:10.5f}".format(1500.31))
print("{0:10,.5f}".format(1500.31))
print("{0:+10} {1:-10}".format(5,-6))
print("{0:-10} {1: 10}".format(5,-6))
print("{0: 10} {1:+10}".format(5,-6))
print("{:b}".format(5678))
print("{:c}".format(65))
print("{:o}".format(5678))
print("{:x}".format(5678))
print("{:x}".format(5678))
print("{:d}".format(5678))
print("{:n}".format(5678))

import locale 
print(locale.setlocale(locale.LC_ALL,"pt_BR.utf-8"))

print("{:f}".format(1579.543))
print("{:n}".format(1579.543))

'''
à esquerda mantissa
à direita expoente
multiplicar mantissa por expoente

1.004500 x 10³ = 1.004500 x 1000 = 1004.5
'''

print("{:8e}".format(3.141592653589793))
print("{:8E}".format(3.141592653589793))
print("{:8g}".format(3.141592653589793))
print("{:8G}".format(3.141592653589793))
print("{:8g}".format(3.14))
print("{:5.2%}".format(0.05)) # output: '5.00%'

##########

# jogo da forca

'''palavra = input("Digite a palavra secreta: ").lowr().strip()
for x in range(100):
    print()
digitadas = []
acertos = [] 
erros = 0 
while True:
    senha=""
    for letra in palavra:
        senha += letra if letra in acertos else "."
        print(senha)
        if senha == palavra:
            print("Você acertou!")
            break 
        tentativa = input("\nDigite uma letra: ").lower().strip()
        if tentativa in digitadas:
            print("Você já tentou esta letra!")
            continue 
        else:
            digitadas += tentativa 
            if tentativa in palavra:
                acertos += tentativa 
            else:
                erros += 1 
                print("Você errou!")
            print("X==:==\nX    :   ")
            print("X O " if erros >= 1 else "X")
            linha2=""
            if erros == 2:
                linha2 = "  |  "
            elif erros == 3:
                linha2 = " \|/"
            print("X%s" % linha2)
            linha3=""
            if erros == 5:
                linha3+=" /  "
            elif erros >= 6:
                linha3+=" /\ "
            print("X%¨s" % linha3)
            print("X\n===========")
            if erros == 6:
                print("Enforcado!")
                break'''


###################

palavra = input("Digite a palavra secreta: ").lower().strip()

for x in range(100):
    print()

digitadas = [] 
acertos = [] 
erros = 0 

while True:
    senha = ""
    for letra in palavra:
        senha += letra if letra in acertos else "."
    print(senha)

    if senha == palavra:
        print("Você acertou!")
        break 

    tentativa = input("\nDigite uma letra: ").lower().strip()

    if tentativa in digitadas:
        print("Você já tentou esta letra!")
        continue 
    else:
        digitadas.append(tentativa)
        if tentativa in palavra:
            acertos.append(tentativa)
        else:
            erros += 1 
            print("Você errou!")

        # Draw the hangman figure
        print("X==:==\nX    :   ")
        print("X O " if erros >= 1 else "X")
        linha2 = " | " if erros >= 2 else ""
        linha3 = "\|/" if erros >= 3 else ""
        linha4 = " /\ " if erros >= 5 else ""
        print(f"X{linha2}")
        print(f"X{linha3}")
        print(f"X{linha4}")
        print("X\n============")

        if erros == 6:
            print("Enforcado! A palavra secreta era:", palavra)
            break


#################

import random

def desenhar_boneco(erros):
    print("X==:==\nX    :   ")
    print("X O " if erros >= 1 else "X")
    
    linha2 = "  |  " if erros >= 2 else ""
    linha3 = "\|/" if erros >= 3 else ""
    print(f"X{linha2}")
    print(f"X{linha3}")

    linha4 = "  /\ " if erros >= 6 else ""
    print(f"X{linha4}")
    print("X\n============")

#######################
import random
import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def select_random_word():
    return random.choice(["python", "programacao", "desenvolvimento", "computador", "inteligencia"])

def draw_hangman(errors):
    hangman_art = [
        '''
        X==:==
        X    :   
        X       
        X       
        X       
        X       
        X\n============
        ''',
        '''
        X==:==
        X    :   
        X O 
        X       
        X       
        X       
        X\n============
        ''',
        '''
        X==:==
        X    :   
        X O 
        X |     
        X       
        X       
        X\n============
        ''',
        '''
        X==:==
        X    :   
        X O 
        X |\\    
        X       
        X       
        X\n============
        ''',
        '''
        X==:==
        X    :   
        X O 
        X |/     
        X       
        X       
        X\n============
        ''',
        '''
        X==:==
        X    :   
        X O 
        X |/\\    
        X       
        X       
        X\n============
        ''',
        '''
        X==:==
        X    :   
        X O 
        X |/\\    
        X /     
        X       
        X\n============
        '''
    ]

    print(hangman_art[errors])

def jogo_da_forca():
    lista_de_palavras = ["python", "programacao", "desenvolvimento", "computador", "inteligencia"]

    while True:
        try:
            clear_screen()

            palavra = select_random_word().lower()

            digitadas = []
            acertos = []
            erros = 0

            while True:
                senha = "".join(letra if letra in acertos else "." for letra in palavra)
                print(senha)

                if senha == palavra:
                    print("Você acertou!")
                    break

                tentativa = input("\nDigite uma letra: ").lower().strip()

                if not tentativa.isalpha() or len(tentativa) != 1:
                    print("Por favor, digite uma única letra.")
                    continue

                if tentativa in digitadas:
                    print("Você já tentou esta letra!")
                    continue
                else:
                    digitadas.append(tentativa)
                    if tentativa in palavra:
                        acertos.append(tentativa)
                    else:
                        erros += 1
                        print("Você errou!")
                        draw_hangman(erros)

                    if erros == 6:
                        print("Enforcado! A palavra secreta era:", palavra)
                        break

            play_again = input("Deseja jogar novamente? (s/n): ").lower().strip()
            if play_again != 's':
                print("Obrigado por jogar! Até a próxima.")
                break

        except ValueError:
            print("Entrada inválida.")

if __name__ == "__main__":
    jogo_da_forca()




##################
def jogo_da_velha():
    while True:
        try:
            def imprimir_tabuleiro(tabuleiro):
                for linha in tabuleiro:
                    print(" | ".join(linha))
                    if linha != tabuleiro[-1]:
                        print("---+---+---")

            def verificar_vitoria(tabuleiro, jogador):
                # Verificar linhas e colunas
                for i in range(3):
                    if all(tabuleiro[i][j] == jogador for j in range(3)) or all(tabuleiro[j][i] == jogador for j in range(3)):
                        return True

                return False

            def jogar():
                tabuleiro = [[" " for _ in range(3)] for _ in range(3)]
                jogadores = ["X", "O"]
                jogador_atual = 0

                for _ in range(9):
                    imprimir_tabuleiro(tabuleiro)
                    jogada = int(input(f"Jogador {jogadores[jogador_atual]}, escolha uma posição (1-9): "))

                    linha = (jogada - 1) // 3
                    coluna = (jogada - 1) % 3

                    if tabuleiro[linha][coluna] == " ":
                        tabuleiro[linha][coluna] = jogadores[jogador_atual]
                        if verificar_vitoria(tabuleiro, jogadores[jogador_atual]):
                            imprimir_tabuleiro(tabuleiro)
                            print(f"Jogador {jogadores[jogador_atual]} venceu!")
                            return "vitoria"

                        jogador_atual = 1 - jogador_atual
                    else:
                        print("Posição ocupada. Tente novamente.")
                
                imprimir_tabuleiro(tabuleiro)
                print("Empate!")
                return "empate"

            if __name__ == "__main__":
                resultado = jogar()
                print("Resultado:", resultado)
                break  # Exit the main loop when the game is finished

        except ValueError:
            print("Entrada inválida. Tente novamente.")

jogo_da_velha()



            


################################################

# funções

def soma(a,b):
    print(a+b)
soma(2,9)
soma(7,8)
soma(10,15)

##########

def soma(a,b):
    return(a+b)
print(soma(2,9))

##########

def ehpar(x):
    return(x%2==0)
print(ehpar(2))
print(ehpar(3))
print(ehpar(10))

##############

def ehpar(x):
    return(x%2==0)
def par_ou_ímpar(x):
    if ehpar(x):
        return "par"
    else:
        return "ímpar"
print(par_ou_ímpar(4))
print(par_ou_ímpar(5))

###################

def maximo(a,b):
    return a if a >= b else b 

result1 = maximo(5, 6)
result2 = maximo(2,1)
result3 = maximo(7, 7)

print(result1)
print(result2)
print(result3)

###############

def multiplo(num1, num2):
    return num1 % num2 == 0 

result1 = multiplo(8,4)
result2 = multiplo(7,3)
result3 = multiplo(5,5)

print(result1)
print(result2)
print(result3)

##################

def area_quadrado(lado):
    return lado ** 2 

result1 = area_quadrado(4)
result2 = area_quadrado(9)

print(result1)
print(result2)

#################

def area_triangulo(base, altura):
    return (base * altura) / 2 

result1 = area_triangulo(6,9)
result2 = area_triangulo(5, 8)

print(result1)
print(result2)

####################

def pesquise(lista, valor):
    for x,e in enumerate (lista):
        if e == valor:
            return x 
    return None 
L=[10, 20, 25, 30]
print(pesquise(L, 25))
print(pesquise(L, 27))

####################

def soma(L):
    total=0
    for e in L:
        total+=e
    return total
def media(L):
    return(soma(L)/len(L))

#################

def média(L):
    total=0
    for e in L:
        total+=e
    return total/len(L)


