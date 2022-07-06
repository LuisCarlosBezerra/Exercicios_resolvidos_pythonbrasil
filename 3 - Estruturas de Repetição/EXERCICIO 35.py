"""
Encontrar números primos é uma tarefa difícil. Faça um programa que gera uma lista dos números primos existentes
entre 1 e um número inteiro informado pelo usuário.
"""
print('PROGRAMA PARA EXIBIÇÃO DE NUMEROS PRIMOS EM UM INTERVALO DE 1 À "N" ')

intervalo = int(input('Digite um número para encontrar os primos que existem entre 1 e o número: '))
lista_primos = []
limite = 2

while limite <= intervalo:
    contador_divisor = 0
    for i in range(1, limite + 1, 1):
        divisor_str = divmod(limite, i)
        if divisor_str[1] == 0:
            contador_divisor += 1
        if (contador_divisor == 2) and (i == limite):
            lista_primos.append(limite)
    limite += 1

print(f'A lista de números primos para o intervalo de 1 à {intervalo} é: {lista_primos}')
