#Importar biblioteca
import sqlite3
#PASSOS 2 e 3 virarão função conectar()
def conectar():
 
  # estabelecer conexão com bancos de dados
  conexao = sqlite3.connect("dc_universe.db")
  #criar um ojeto de tipo cursor
  cursor = conexao.cursor()
  
  return conexao, cursor