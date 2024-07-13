#Tópicos importantes com laços em Python
#Nomeclatura recomendada 

#Operações especiais de atribuição
soma = 0
cont = 1
while (cont <=5):
  x = int(input(f'Digite a {cont}° numero:'))
  soma += x #Equivalente: soma = soma  + x
  cont += 1 # Equivalente: cont = cont + 1
print(f'Somátorio: {soma}')