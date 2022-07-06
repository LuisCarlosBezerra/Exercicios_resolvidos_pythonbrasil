"""
Faça um Programa que leia dois vetores com 10 elementos cada. Gere um terceiro vetor de 20 elementos, cujos valores
deverão ser compostos pelos elementos intercalados dos dois outros vetores.
"""
vetor_1 = []
vetor_2 = []
vetor_3 = []

for i in range(10):
    while True:
        try:
            numero = int(input('Digite o numero para o primeiro vetor: '))
            if numero >= 0:
                vetor_1.append(numero)
                vetor_3.append(numero)
                break
            else:
                print('Você digitou um valor negativo, tente novamente.')
        except ValueError:
            print('Você digitou um valor inválido, tente novamente.')

    while True:
        try:
            numero = int(input('Digite o numero para o segundo vetor: '))
            if numero >= 0:
                vetor_2.append(numero)
                vetor_3.append(numero)
                break
            else:
                print('Você digitou um valor negativo, tente novamente.')
        except ValueError:
            print('Você digitou um valor inválido, tente novamente.')

print(f'O primeiro vetor digitado foi: {vetor_1}')
print(f'O segundo vetor digitado foi: {vetor_2}')
print(f'O novo vetor (INTERCALANDO OS VETORES ANTERIORES) é: 1{vetor_3}')
