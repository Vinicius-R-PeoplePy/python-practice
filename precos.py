import sqlite3 
from contextlib import closing 

with sqlite3.connect("precos.db") as conexao: 
    with closing(conexao.cursor()) as cursor:
        cursor.execute('''
                create table preços(
                    nome text,
                    preço numeric)
                ''')
        cursor.execute('''
                insert into preços (nome, preço)
                    values(?, ?)
                    ''', ("Batata", "3.20"))
        cursor.execute('''
                insert into preços (nome, preço)
                    values(?, ?)
                    ''', ("Pão", "1.20"))
        cursor.execute('''
                insert into preços (nome, preço)
                    values(?, ?)
                    ''', ("Mamão", "2.14"))
        
