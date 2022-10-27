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