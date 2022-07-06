"""
Faça um Programa que peça a idade e a altura de 5 pessoas, armazene cada informação no seu respectivo vetor. Imprima a
idade e a altura na ordem inversa a ordem lida.
"""
lista_idade = []
lista_altura = []

for i in range(5):
    while True:
        try:
            idade = int(input('Entre com a idade: '))

            if idade >= 0:
                lista_idade.append(idade)
                break
            else:
                print('Você digitou um valor inválido, tente novamente.')

        except ValueError:
            print('Você digitou um valor inválido, tente novamente.')

    while True:
        try:
            altura = int(input('Digite o valor da altura, em centímetros: '))
            if altura >= 0:
                lista_altura.append(altura)
                break
            else:
                print('Você digitou um valor inválido, tente novamente.')

        except ValueError:
            print('Você digitou um valor inválido, tente novamente.')

lista_idade.reverse()
lista_altura.reverse()
print(f'REVERSÃO DA LISTA DE IDADE: {lista_idade}')
print(f'REVERSÃO DA LISTA DE ALTURA: {lista_altura}')
