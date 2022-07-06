"""
Faça um programa que leia 5 números e informe o maior número.
"""
maior = 0

for _ in range(5):
    numero = int(input('Digite um número: '))
    if numero > maior:
        maior = numero
    print(f'Até o momento, o maior número digitado foi {maior}')

print(f'O maior número digitado foi: {maior}')
