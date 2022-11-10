#Criação de funções
#print()
#input()
#len()
preco = 1999.90
#calcular 5% de imposto, guarda na variavel de imposto e exibir na tela

imposto = preco * 0.05
print(imposto)

preco2 = 100
imposto2 = preco2 * 0.05
print(imposto2)

#CRIAR uma função calcular_imposto() que calcula um imposto de 5% e retorna a quem pediu...
# isso e a declaração da função
def calcular_imposto(preco_produto):
  imposto = preco_produto * 0.05
  return imposto

# aqui e o uso
preco = 299
imposto = calcular_imposto(preco)
print(imposto)
