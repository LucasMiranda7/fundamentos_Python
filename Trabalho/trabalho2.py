# QUESTÃO 2 - até a Aula 04
# Autor: Lucas Miranda da Silva

#Apresentação
print('-'*5, 'Bem vindo a Loja de Marmitas do Lucas Miranda da Silva', '-'*5)
#Cardápio / Menu
print('-'*26 ,'Cardápio','-'*30)
print('-'*66)
print('-'*3, '| ' 'Tamanho', '| ', 'Bife Acebolado (BA)', '| ', 'Filé de Frango (FF)', ' |', '-'*3)
print('-'*3, '|    ' 'P', '   |    ', 'R$ 16.00', '        |     ', 'R$ 15.00', '        |', '-'*3)
print('-'*3, '|    ' 'M', '   |    ', 'R$ 18.00', '        |     ', 'R$ 17.00', '        |', '-'*3)
print('-'*3, '|    ' 'G', '   |    ', 'R$ 22.00', '        |     ', 'R$ 21.00', '        |', '-'*3)
print('-'*66)

BA = 'Bife Acebolado'
FF = 'Filé de Frango'

acumulador = 0

while True:
  # Loop de Validar o sabor
  while True: 
    sabor = input("Entre com o sabor desejado (BA/FF): ")
    if sabor == "BA" or sabor == "FF": 
      break
    else:
      print('Sabor inválido. Tente novamente')
      print("\n")

    # Loop de Validar o tamanho
  while True: 
    tamanho = input("Entre com o tamanho desejado (P/M/G): ")
    if tamanho == "P" or tamanho == "M" or tamanho == "G":
      break
    else:
      print('Tamanho inválido. Tente novamente')
      print("\n") 
      break # Volta para o início do loop de validação do sabor

        #Entrada das Combinações do Sabor "BA"
  if sabor == "BA" and tamanho == "P":
    print(f'Você pediu um {BA} no Tamanho P: R$ 16.00')
    acumulador += 16.00 #acumulador
    print("\n")
    pedir_novamente = input("Deseja mais alguma coisa? (S/N): ")
    if pedir_novamente == "S":
      continue #Retoma o Loop (caso a pessoa responda "S")
    else:
        if pedir_novamente == "N":
          print("\n")
        break # Para o Loop e Trás o valor Final (Caso a resposta seja "N")
    
  elif sabor == "BA" and tamanho == "M":
    print(f'Você pediu um {BA} no Tamanho M: R$ 18.00')
    acumulador += 18.00 #acumulador
    print("\n")
    pedir_novamente = input("Deseja mais alguma coisa? (S/N): ")
    if pedir_novamente == "S":
      continue #Retoma o Loop (caso a pessoa responda "S")
    else:
        if pedir_novamente == "N":
          print("\n")
        break # Para o Loop e Trás o valor Final (Caso a resposta seja "N")
    
  elif sabor == "BA" and tamanho == "G":
    print(f'Você pediu um {BA} no Tamanho G: R$ 22.00')
    acumulador += 22.00 #acumulador
    print("\n")
    pedir_novamente = input("Deseja mais alguma coisa? (S/N): ")
    if pedir_novamente == "S":
      continue #Retoma o Loop (caso a pessoa responda "S")
    else:
        if pedir_novamente == "N":
          print("\n")
        break # Para o Loop e Trás o valor Final (Caso a resposta seja "N")
    
    #Entrada das Combinações do sabor "FF"
  if sabor == "FF" and tamanho == "P":
    print(f'Você pediu um {FF} no Tamanho P: R$ 15.00')
    acumulador += 15.00 #acumulador
    print("\n")
    pedir_novamente = input("Deseja mais alguma coisa? (S/N): ")
    if pedir_novamente == "S":
      continue #Retoma o Loop (caso a pessoa responda "S")
    else:
        if pedir_novamente == "N":
          print("\n")
        break # Para o Loop e Trás o valor Final (Caso a resposta seja "N")

  elif sabor == "FF" and tamanho == "M":
    print(f'Você pediu um {FF} no Tamanho M: R$ 17.00')
    acumulador += 17.00 #acumulador
    print("\n")
    pedir_novamente = input("Deseja mais alguma coisa? (S/N): ")
    if pedir_novamente == "S":
      continue #Retoma o Loop (caso a pessoa responda "S")
    else:
        if pedir_novamente == "N":
          print("\n")
        break # Para o Loop e Trás o valor Final (Caso a resposta seja "N")

  elif sabor == "FF" and tamanho == "G":
    print(f'Você pediu um {FF} no Tamanho G: R$ 21.00')
    acumulador += 21.00 #acumulador
    print("\n")
    pedir_novamente = input("Deseja mais alguma coisa? (S/N): ")
    if pedir_novamente == "S":
       continue #Retoma o Loop (caso a pessoa responda "S")
  else:
      continue # Retoma para o início do loop principal
  if pedir_novamente == "N": 
       print("\n")
       break #Para o Loop
  else:
        print("\n") #Pula Linha
        break # Para o Loop e Trás o valor Final 
    

print(f"O valor total a ser pago é: R$ {acumulador:.2f}") #Calculo do Preço Total