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
  imposto = preco_produto * 0.07
  return imposto

# aqui e o uso
preco = 299
imposto = calcular_imposto(preco)
print(f"Esse aqui a função e (7%): {imposto}")


# agora calcular imposto a alíquota mudar 

valores = [1.99, 24.50, 78.27, 1515.5]
# se eu quiser calcular o imposto destes valores
for valor in valores:
  
  print(f"O imposto de {valor} é {calcular_imposto(valor)}")


#Declarar uma função calcular_imposto_aliquota que recebe dois parâmetros: o preço do produto e a alíquota de imposto a ser aplicada e retorna o imposto calculado. Se a aliquota não for informada, utilize 7% como padrão.

def calcular_imposto_aliquota(valor, aliquota=7):
  imposto = valor * aliquota/100
  return imposto

for valor in valores:
  
  print(f"O imposto de {valor} é {calcular_imposto_aliquota(valor)}")

# E se o imposto for de 10%
  
for valor in valores:
  
  print(f"O imposto de {valor} é {calcular_imposto_aliquota(valor, 10)}")
  
