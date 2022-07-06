"""
Altere o programa anterior, intercalando 3 vetores de 10 elementos cada.
"""
vetor_1 = []
vetor_2 = []
vetor_3 = []
vetor_4 = []

for i in range(2):
    while True:
        try:
            numero = int(input('Entre com um número para o primeiro vetor: '))
            if numero >= 0:
                vetor_1.append(numero)
                vetor_4.append(numero)
                break
            else:
                print('Você digitou um número negativo, tente novamente.')
        except ValueError:
            print('Você digitou um valor inválido, tente novamente.')

    while True:
        try:
            numero = int(input('Entre com um número para o segundo vetor: '))
            if numero >= 0:
                vetor_2.append(numero)
                vetor_4.append(numero)
                break
            else:
                print('Você digitou um número negativo, tente novamente.')
        except ValueError:
            print('Você digitou um valor inválido, tente novamente.')

    while True:
        try:
            numero = int(input('Entre com um número para o terceiro vetor: '))
            if numero >= 0:
                vetor_3.append(numero)
                vetor_4.append(numero)
                break
            else:
                print('Você digitou um número negativo, tente novamente.')
        except ValueError:
            print('Você digitou um valor inválido, tente novamente.')

print(f'O primeiro vetor digitado foi: {vetor_1}')
print(f'O segundo vetor digitado foi: {vetor_2}')
print(f'O segundo vetor digitado foi: {vetor_3}')
print(f'O novo vetor (SOMANDO CADA UMA DAS POSIÇÕES) é: {vetor_4}')
