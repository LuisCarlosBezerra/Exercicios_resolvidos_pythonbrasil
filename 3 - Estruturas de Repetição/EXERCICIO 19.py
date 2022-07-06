"""
Faça um programa que, dado um conjunto de N números, determine o menor valor, o maior valor e a soma dos valores.
Altere o programa anterior para que ele aceite apenas números entre 0 e 1000.
"""
contador = 0

fim_programa = False
while fim_programa is False:
    try:
        numero = int(input('Digite um número natural de 0 à 1000 '))
        if (numero >= 0) and (numero <= 1000) and (
                contador == 0):  # o CONTADOR garante que os numeros MAIOR e MENOR só receberão o valor NUMERO da
            # primeira vez que o usuario digitar um numero válido.
            maior = numero
            menor = numero
            # print('PASSOU AQUI ')
            contador += 1
    except ValueError:
        print('Você digitou um valor inválido. Tente novamente.')

    if (numero >= 0) and (numero <= 1000):
        if numero >= maior:
            maior = numero
        if numero <= menor:
            menor = numero
    elif numero == 1111:
        fim_programa = True
    else:
        print('Você digitou um valor fora do intervalo solicitado. Tente novamente.')

print(f'MAIOR = {maior}\nMENOR = {menor} \nSOMA: {maior + menor}')
