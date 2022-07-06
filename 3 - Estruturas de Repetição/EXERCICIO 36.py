"""
Desenvolva um programa que faça a tabuada de um número qualquer inteiro que será digitado pelo usuário, mas a tabuada
não deve necessariamente iniciar em 1 e terminar em 10, o valor inicial e final devem ser informados também pelo
usuário, conforme exemplo abaixo:

Montar a tabuada de: 5
Começar por: 4
Terminar em: 7

Vou montar a tabuada de 5 começando em 4 e terminando em 7:
5 X 4 = 20
5 X 5 = 25
5 X 6 = 30
5 X 7 = 35
"""
tabuada = int(input('Digite o número que você que mostrar na tabuada: '))
print('\nAgora vamos escolher o intervalo da tabuada!\n')

while True:
    limite_inferior = int(input('Entre com o primeiro número da tabuada: '))
    limite_superior = int(input('Entre com o último número do intervalo: \n'))

    if (limite_superior >= limite_inferior):
        for i in range(limite_inferior, limite_superior + 1, 1):
            print(f'{tabuada} x {i} = {tabuada * i}')
        if i == limite_superior:
            break
    else:
        print('Você digitou um número menor para o último do intervalo, tente novamente.')
