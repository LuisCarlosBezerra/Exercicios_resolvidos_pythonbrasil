"""
Faça um programa que leia 5 números e informe a soma e a média dos números.
"""
# RESOLUÇÃO 1

soma = 0
media = 0
contador = 1

for _ in range(5):
    numero = int(input('Digite um número: '))
    soma += numero
    media = soma / contador
    contador += 1

print(f'A soma dos 5 números é {soma}')
print(f'A média dos 5 números é {media}')
