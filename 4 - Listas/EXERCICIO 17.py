"""
Em uma competição de salto em distância cada atleta tem direito a cinco saltos. O resultado do atleta será determinado
pela média dos cinco valores restantes. Você deve fazer um programa que receba o nome e as cinco distâncias alcançadas
pelo atleta em seus saltos e depois informe o nome, os saltos e a média dos saltos. O programa deve ser encerrado
quando não for informado o nome do atleta. A saída do programa deve ser conforme o exemplo abaixo:

Atleta: Rodrigo Curvêllo
Primeiro Salto: 6.5 m
Segundo Salto: 6.1 m
Terceiro Salto: 6.2 m
Quarto Salto: 5.4 m
Quinto Salto: 5.3 m

Resultado final:
Atleta: Rodrigo Curvêllo
altos: 6.5 - 6.1 - 6.2 - 5.4 - 5.3
Média dos saltos: 5.9 m
"""

lista_saltos = []

nome_atleta = str(input('Digite o nome do atleta\nDeixe em branco para encerrar o programa: '))

while nome_atleta != '':

    for i in range(5):
        while True:
            try:
                salto = float(input('Entre com o valor do salto, em metros. '))
                if salto > 0:
                    lista_saltos.append(salto)
                    break
                else:
                    print('Você digitou um valor negativo, tente novamente.')
            except ValueError:
                print('Você digitou um valor inválido, tente novamente.')

    print(f'\nAtleta: {nome_atleta}')
    for j, k in enumerate(lista_saltos):
        print(f'Salto {j + 1} = {k} metros')

    print('RESULTADO FINAL: ')
    print(f'\nAtleta: {nome_atleta}')
    print('SALTOS: ', end=' ')
    for l, m in enumerate(lista_saltos):
        if (l + 1) != 5:
            print(f'{m} -', end=' ')
        else:
            print(m)
    print(f'Média dos saltos: {sum(lista_saltos) / 5}')

    lista_saltos = []
    nome_atleta = str(input('\nDigite o nome do atleta\nDeixe em branco para encerrar o programa: '))

print('\nPROGRAMA FINALIZADO')
