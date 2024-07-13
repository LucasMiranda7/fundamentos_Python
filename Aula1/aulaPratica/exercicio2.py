km = int (input('Quantos Km foram percorridos? '))
dias = int(input('Quantos dias foram percorridos? '))


preco = 60 * dias + 0.15 * km
print(f'km = {km}. Dias: {dias}')
print(f'Valor a ser pago: {preco}')


print(' ' *5, 'COBRANÇAS VIA', ' ' *5)

kiloMetros = int (input('Quantos km foram Percorridos ? '))
quantDias = int(input('Quantos dias foi Percorrido ? '))

calTotal = 60 * quantDias + 0.54 * kiloMetros

print(f'KiloMêtros: {kiloMetros}. Dias: {quantDias}')
print(f'Total a ser Pago: {calTotal}')


                    #POSTO DE GASOLINA

print(' ' *5, 'POSTO DE GASOLINA', ' ' *5)

distanciaKm = int(input('INSIRA A DISTÂNCIA QUE IRÁ PERCORRER EM KM: '))
consumoVeic = int(input('INSIRA O CONSUMO DO VEÍCULO POR LITRO: '))
precoCombustivel = float(input('INSIRA O VALOR DA GASOLINA: '))
                                        
calcGeral =  (distanciaKm / consumoVeic) * precoCombustivel



print(f'A distancia em Km é {distanciaKm}.\n O consumo por Litro é {consumoVeic}.\n O Preço padrão da Gasolina é  {precoCombustivel}')
print(f'O valor Total a pagar na Gasolina é  {calcGeral:.2f} ') #\n -quebra de linhas   #:.2f - Quantas casas decimais eu quero