"""
Faça um Programa que leia um vetor de 10 caracteres, e diga quantas consoantes foram lidas. Imprima as consoantes.
"""
consoantes = ['B', 'C', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'M', 'N', 'P', 'Q', 'R', 'S', 'T', 'V', 'X', 'Y', 'Z']
while True:

    try:
        vetor = str(input('Entre com uma palavra de 10 caracteres: '))
        tamanho = len(vetor)

        if tamanho == 10:
            print('Valor digitado com sucesso!')
            vetor = vetor.upper()
            print(vetor)
            break
        else:
            print('Você digitou um valor fora do padrão de 10 caracteres, tente novamente.')

    except ValueError:
        print('Você entrou com um valor inválido, tente novamente.')

print('As consoantes para esse vetor são: ', end=" ")
for i in vetor:
    if i in consoantes:
        print(i, end=" ")
