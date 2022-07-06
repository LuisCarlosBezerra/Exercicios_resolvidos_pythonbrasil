"""
Faça um Programa que leia 4 notas, mostre as notas e a média na tela.
"""
print('PROGRAMA PARA MÉDIA DE 4 NOTAS')

lista_notas = []

for _ in range(1, 5, 1):
    while True:
        try:
            nota = float(input('Entre com a nota do aluno: '))

            if (nota >= 0) and (nota <= 10):
                lista_notas.append(nota)
                break
            else:
                print('Você digitou uma nota fora do intervalo padrão (1 à 10), tente novamente.')

        except ValueError:
            print('Você digitou um valor inválido, tente novamente.')

soma_notas = sum(lista_notas)
print(f'As notas digitadas foram: {lista_notas}')
print(f'A média do aluno foi: {soma_notas / 4}')
