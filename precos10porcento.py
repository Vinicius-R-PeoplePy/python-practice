# Escreva um programa que aumente o preço de todos os produtos
# do banco preços.db em 10% 

import sqlite3 
from contextlib import closing 

with sqlite3.connect("precos.db") as conexao:
    with closing(conexao.cursor()) as cursor: 
        cursor.execute('''update preços
                          set preço = preço * 1.1''')
        # Mostra os novos preços 
        cursor.execute('''select * from preços''')
        for resultado in cursor.fetchall():
            print("Nome: {0:30s} Preço: {1:6.2f}".format(*resultado))

    