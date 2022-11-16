#Importar biblioteca
import sqlite3
# estabelecer conexão com bancos de dados
conexao = sqlite3.connect("dc_universe.db")
#criar um ojeto de tipo cursor
cursor = conexao.cursor()
# Comando SQL do banco
sql = "SELECT pessoa_id, nome, nome_civil, tipo FROM pessoas"
#Executar o comando SQL no SQLlite(No cursor)
cursor.execute(sql)
#Uma consulta mostrando todos os nomes do banco de dados
pessoas = cursor.fetchall()
for pessoa in pessoas:
  print(pessoa)

for pessoa in pessoas:
  print(f"Nome: {pessoa[1]} ({pessoa[3]})")