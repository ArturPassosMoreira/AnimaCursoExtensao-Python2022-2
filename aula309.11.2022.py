print("Inicio da aula 3")


contador = 1
#exibir de 1 a 10 
while(contador <= 10 ):
   print(contador)
   contador = contador +1 #contador += 1



  
# Laço for
fruta= "morango"
print(fruta)
fruta1 ="morango"
fruta2 ="laranja"
fruta3 ="pêra"
#lista
frutas = ["morango", "laranja", "pêra"]

#Quero exibir a terceira fruta(pêra)

print(frutas[2])

#Exibir quantas frutas tem na lista
print(len(frutas)) # length = tamanho
#quero incluir fruta na lista
frutas.append("manga")

print(len(frutas))
print(frutas)

print("Exemplo das frutas com while")

frutas.append("uva")
i = 0
while(i<len(frutas)):
  print(frutas[i])
  i = i + 1

print("Exemplo das frutas com o FOR")
for fruta in frutas:
  print(fruta)