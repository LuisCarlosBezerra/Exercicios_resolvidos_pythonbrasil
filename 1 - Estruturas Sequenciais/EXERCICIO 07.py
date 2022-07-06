"""
Faça um Programa que calcule a área de um quadrado, em seguida mostre o dobro desta área para o usuário.
"""
print('Digite o valor do lado do quadrado ')

teste = False
while teste is False:
    try:
        lado = float(input())
        teste = True
    except ValueError:
        print("Digite um valor válido")

dobroarea = lado * lado * 2
print(f'O DOBRO DA ÁREA desse quadrado é igual a: {dobroarea:.2f}')
