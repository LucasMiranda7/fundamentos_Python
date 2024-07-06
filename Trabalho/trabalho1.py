# QUESTÃO 1 - até a Aula 03 
# Autor: Lucas Miranda da Silva 

#Mensagem de boas-vindas
print('Bem-vindo a Loja do Lucas Miranda da Silva')

##Entrada dos Input de Valor do Pedido e Quantidade de Parcelas
valorDoPedido = float(input('Entrar com o valor do pedido: '))
quantidadeParcelas = int(input('Entrar com a quantidade de parcelas: '))

#Estrutura da Lógica if
if (quantidadeParcelas < 4 ):
    juros = (0/100) #0% de 100

elif (quantidadeParcelas >= 4 and quantidadeParcelas < 6):
    juros = (4/100) #4% de 100

elif (quantidadeParcelas >= 6 and quantidadeParcelas < 9):
    juros = (8/100) #8% de 100

elif (quantidadeParcelas >= 9 and quantidadeParcelas < 13):
    juros = (16/100) #16% de 100

else: 
   quantidadeParcelas >= 13
   juros = (32/100) #32% de 100

#Calculos
valorDaParcela = valorDoPedido * (1 + juros) / quantidadeParcelas
valorTotalParcelado = valorDaParcela * quantidadeParcelas

#Saida
print(f'O valor das parcelas é de: R$ {valorDaParcela:.2f}')
print(f'O valor Total Parcelado é de: R$ {valorTotalParcelado:.2f}')
