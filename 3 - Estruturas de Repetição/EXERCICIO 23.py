"""
Faça um programa que mostre todos os primos entre 1 e N sendo N um número inteiro fornecido pelo usuário.
O programa deverá mostrar também o número de divisões que ele executou para encontrar os números primos.
Serão avaliados o funcionamento, o estilo e o número de testes (divisões) executados.
"""
intervalo = int(input('Digite um intervalo para verificar os numeros primos presentes nele: '))
numero_a_testar = 1
limite = numero_a_testar
contador_divisor = 0
divisor = 1
lista_primos = []

while numero_a_testar <= intervalo:
    divisor = 1
    contador_divisor = 0

    while (contador_divisor <= 2) and (divisor <= numero_a_testar):
        divisor_str = divmod(numero_a_testar, divisor)
        if divisor_str[1] == 0:
            contador_divisor += 1
        divisor += 1

    if contador_divisor == 2:
        lista_primos.append(numero_a_testar)
    numero_a_testar += 1

print(f' Os números primos dentro desse intervalo são: {lista_primos}')
