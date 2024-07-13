

print(" "*5, "LANCHONETE", " "*5)
print('1 - Coxinha R$ 5,00')
print('2 - Pastel R$ 7,00')
print('3 - Café R$ 4,00')
print('4 - Suco R$ 6,00')
print('5 - SAIR ')

total = 0

while True:
  op = int(input("Qual item gostaria de comprar? "))


  if (op == 1):
        qtd = int(input("Quantas unidades quer comprar? "))
        total = total + qtd * 5.00
        print("\n")
        continue
  
  elif (op == 2):
        qtd = int(input("Quantas unidades quer comprar? "))
        total = total + qtd * 7.00
        print("\n")
        continue
       
  elif (op == 3):
        qtd = int(input("Quantas unidades quer comprar? "))
        total = total + qtd * 4.00
        print("\n")
        continue
        
  elif (op == 4):
       qtd = int(input("Quantas unidades quer comprar? "))
       total = total + qtd * 6.00
       print("\n")
       continue

  elif (op == 5):
       print(f"O Total a ser gasto nesse pedido é de R$: {total}.")
       print("Agradeçemos pela compra! Volte sempre.")
       break
  
  else: 
       print("Produto não existe. Tente novamente")
       
  

 
 
