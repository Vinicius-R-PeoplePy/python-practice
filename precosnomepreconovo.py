# Escreva um programa que pergunte o nome do produto e um novo
# preço. Usando o banco preços.db, atualize o preço desse 
# produto no banco de dados. 

import sqlite3 
from contextlib import closing 

with sqlite3.connect("precos.db") as conexao: 
    with closing(conexao.cursor()) as cursor:
        nome = input("Digite o nome do produto a alterar o preço: ")

        cursor.execute('''select * from preços 
                       where nome = ?''', (nome,))
        
        resultado = cursor.fetchone()
        if resultado:
            print("Nome: {0:30s} Preço: {1:6.2f}".format(*resultado))
            novo_preco = input("Digite o novo preço: ")
            cursor.execute('''update preços 
                           set preço = ? 
                           where nome = ?''', (novo_preco, nome))
        else: 
            print("Não encontrado.")

            