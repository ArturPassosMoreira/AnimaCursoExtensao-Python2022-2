import aula4_c_16_11_2022 as bd

con, cur = bd.conectar()
nome = input("Digite o nome do heroi/vilão:")
nome_civil = input("Digite o nome civil do heroi/vilão(Identidade secreta):")
tipo_numerico=input("Tecle 1 Herói(na) ou Tecle 2 Vilã(o):")
#Consulta para o valor maximo usado no banco
sql = "SELECT MAX(pessoa_id)+1 FROM pessoas"
cur.execute(sql)
pessoa_id = cur.fetchone()[0]
if tipo_numerico == "1":
  tipo = "Herói(na)"
else:
  tipo = "Vilã(o)"
  
sql = f"INSERT INTO pessoas (pessoa_id, nome, nome_civil, tipo) VALUES ({pessoa_id}, '{nome}', '{nome_civil}', '{tipo}')"

cur.execute(sql)
con.commit()
con.close()