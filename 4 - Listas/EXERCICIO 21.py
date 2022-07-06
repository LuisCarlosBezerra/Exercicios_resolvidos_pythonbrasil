"""
Faça um programa que carregue uma lista com os modelos de cinco carros (exemplo de modelos: FUSCA, GOL, VECTRA etc).
Carregue uma outra lista com o consumo desses carros, isto é, quantos quilômetros cada um desses carros faz com um
litro de combustível.

Calcule e mostre:
O modelo do carro mais econômico;
Quantos litros de combustível cada um dos carros cadastrados consome para percorrer uma distância de 1000 quilômetros
e quanto isto custará, considerando um que a gasolina custe R$ 2,25 o litro. Abaixo segue uma tela de exemplo.
O disposição das informações deve ser o mais próxima possível ao exemplo. Os dados são fictícios e podem mudar a cada
execução do programa.

Comparativo de Consumo de Combustível
Veículo 1
Nome: fusca
Km por litro: 7

Veículo 2
Nome: gol
Km por litro: 10

Veículo 3
Nome: uno
Km por litro: 12.5

Veículo 4
Nome: Vectra
Km por litro: 9

Veículo 5
Nome: Peugeout
Km por litro: 14.5

Relatório Final
1 - fusca   -       7.0     -       142.9 litros    -   R$ 321.43
2 - gol     -       10.0    -       100.0 litros    -   R$ 225.00
3 - uno     -       12.5    -       80.0 litros     -   R$ 180.00
4 - vectra  -       9.0     -       111.1 litros    -   R$ 250.00
5 - peugeout -      14.5    -       69.0 litros     -   R$ 155.17

O menor consumo é do peugeout.
"""
lista_veiculos = []
lista_consumo = []

print('DIGITE O NOME DOS 5 VEÍCULOS E SEUS RESPECTIVOS CONSUMOS (Km/L)\n')

for i in range(1, 6, 1):
    print(f'Veículo {i}')
    while True:
        try:
            carro = str(input('Nome: '))
            if carro == '':
                print('Você não digitou o nome do carro. Tente novamente:')
            else:
                lista_veiculos.append(carro)
                break
        except ValueError:
            print('Você digitou um valor inválido!')

    while True:
        try:
            consumo = float(input('Km por litro: '))
            if consumo > 0:
                lista_consumo.append(consumo)
                if i == 1:
                    menor_consumo = consumo
                    id = i
                else:
                    if consumo > menor_consumo:
                        menor_consumo = consumo
                        id = i
                break
            else:
                print('Consumo inválido, tente novamente:')
        except ValueError:
            print('Você digitou um valor inválido, tente novamente!')

print('\nRelatório final\n')

print(f'ID - VEÍCULO\t\t-\tCONSUMO(KM/L)\t\tCONSUMO(1000KM)\t\tVALOR 1000KM\n')

for i in range(1, 6, 1):
    print(
        f'{i} - {lista_veiculos[i - 1]}\t\t-\t{lista_consumo[i - 1]}\t\t\t{"%.2f" % (1000 / lista_consumo[i - 1])} L'
        f'\t\t\t{"%.2f" % ((1000 / lista_consumo[i - 1]) * 7.25)} RS\n')

print(f'O menor consumo é o do {lista_veiculos[id - 1]}')
