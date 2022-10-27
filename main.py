'''# Meu primeiro Projeto Python!!!
#  PRIMEIRA AULA 19/10/2022
# print() = comando de saida
print("Alo Mundo!")

# Quando quiser guardar uma String!
nome = "Artur Moreira"
# Quando quiser guardar um numero inteiro!
idade = 18
# Exibir o nome
print("Seu nome é ", nome)
print(f"A minha idade é: {idade} ")
print("A minha idade é: {}".format(idade))
'''




 # SEGUNDA AULA 26/10/2022
'''# comando input(): Quero permitir que o usuario digite algo
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
'''




#Pede o nome do aluno e sua nota (de 0 a 10) e, se ele tirou nota 10, mostra "Você é bichão, mesmo..."

nome = str(input("Digite seu nome: "))
nota = float(input("Qual sua nota: "))

if(nota == 10):
  print("Parabéns {}, voce tirou  nota maxima!".format(nome))
elif(nota < 10 and nota >= 7):
  print("Você passou acima da media!")
elif(nota == 6):
  print("Você passou na média.")
elif(nota < 6 and nota >= 0):
  print("Você reprovou. :(")
elif(nota > 10 or nota < 0):
  print("Insira um valor entre 0 e 10.")






