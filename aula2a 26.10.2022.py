 # SEGUNDA AULA 26/10/2022
# comando input(): Quero permitir que o usuario digite algo
# o usuario digite algo...
nome = input("Digite seu nome: ")
# pede a idade "Qual sua idade?"
idade =  int(input("Digite sua idade: "))
# comando de saida ..exibir na tela
print(f"Olá {nome}" )
print(f"Você tem {idade} anos de idade")
# e se quisesse mostar o dobro?
dobro = idade * 2
print("O dobro da sua idade e {}".format(dobro))
# estrutura condicional "SE"
# Se for maior de idade mostre
# "Voce e maior de idade e ja pode dirigir"
sexo = input("Digite seu sexo(M/F): ")
if (idade >= 18):
  print("Você e maior de idade, ja pode dirigir")
  
else:
  print("Você ainda e menor de idade ")  
  
#E se eu quisessem perguntar o gênero (M = Masculino e F = Feminino)
#Mostre (...e você também precisa/precisou prestar o serviço militar obrigatório)
if (idade >= 18 and sexo == "M"):
  print("Você precisa se alistar")
else:
  print("Você não precisa se alistar") 





