#Escopo de Variáveis
##Um escopo é Propriedade que determina onde uma variável pode ser utilizada dentro de um programa / Escopo Local e Escopo Global

#Exemplo 1
def omelete():
  ovos = 12 # variavel local

  #programa principal
  omelete()
  print(ovos)# escopo global


print('-'*20)
#Exemplo 2
def omelete():
   print(ovos) # escopo local

  #programa principal
ovos = 12 # Variavel / escopo global
omelete()


print('-'*20)
#Exemplo 3
def omelete():
   ovos = 12
   bacon()
   print(ovos)

def bacon():
   ovos = 6

   #programa principal
omelete()


print('-'*20)
#Exemplo 4

def omelete():
   ovos = 12 # variavel local de omelete
   print('Ovos = ', ovos)

def bacon():
   ovos = 6 # variavel local de bacon
   print('Ovos = ', ovos)
   omelete()
   print('Ovos = ', ovos)

#programa principal
ovos = 2 #variavel global
bacon()
print('Ovos = ', ovos)


print('-'*20)
#A instrução global
#Exemplo 5

def omelete():
   global ovos
   ovos = 6

   #programa principal
ovos = 12
omelete()
print(ovos)


#Exemplo 6

def omelete():
   global ovos 
   ovos = 6 
   bacon()

def bacon():
    ovos = 12
    pimenta()
 
def pimenta():
    print(ovos)
   
  #programa principal
ovo = 4
omelete()
print(ovos)


print('-'*20)
#Exemplo 7

def omelete():
   print(ovos)
   ovos = 6

ovos = 12
omelete()
