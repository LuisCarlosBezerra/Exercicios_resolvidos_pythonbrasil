"""
Faça um programa que leia um número indeterminado de valores, correspondentes a notas, encerrando a entrada de dados
quando for informado um valor igual a -1 (que não deve ser armazenado). Após esta entrada de dados, faça: Mostre a
quantidade de valores que foram lidos; Exiba todos os valores na ordem em que foram informados, um ao lado do outro;
Exiba todos os valores na ordem inversa à que foram informados, um abaixo do outro;

Calcule e mostre a soma dos valores;
Calcule e mostre a média dos valores;
Calcule e mostre a quantidade de valores acima da média calculada;
Calcule e mostre a quantidade de valores abaixo de sete;
Encerre o programa com uma mensagem;
"""
nota = 0
lista_notas = []

while nota != -1:
    while True:
        try:
            nota = float(input('Digite o valor da nota (Digite -1 para encerrar o programa) '))
            if ((nota >= 0) and (nota <= 10)):
                lista_notas.append(nota)
            elif nota == -1:
                break
            else:
                print('Você digitou um valor fora do intervalo de 1 à 10. Tente novamente.')

        except ValueError:
            print('Você digitou um valor inválido. Tente novamente.')

print(f'\nVocê digitou um total de {len(lista_notas)} nota(s)')

print('\nOs valores digitados, na ordem, foram: ')
for i in lista_notas:
    print(i, end=' ')

lista_notas.reverse()
print('\nOs valores, na ordem REVERSA, são: ')
for j in lista_notas:
    print(j, end=' ')

print(f'\n\nA soma dos valores digitados é igual a: {sum(lista_notas)}')
print(f'\nA média das notas digitadas é igual a: {sum(lista_notas) / len(lista_notas)}')

print('\nOs valores acima da média de notas são: ')
for k in lista_notas:
    if k >= (sum(lista_notas) / len(lista_notas)):
        print(k, end=' ')

print('\n1\nOs valores abaixo de 7 são: ')
for l in lista_notas:
    if l < 7:
        print(l, end=' ')

print('\n\nPROGRAMA ENCERRADO!')
