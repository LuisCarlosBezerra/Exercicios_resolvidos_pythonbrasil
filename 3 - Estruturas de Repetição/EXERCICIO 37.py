"""
Uma academia deseja fazer um senso entre seus clientes para descobrir o mais alto, o mais baixo, a mais gordo e o mais
magro, para isto você deve fazer um programa que pergunte a cada um dos clientes da academia seu código, sua altura e
seu peso. O final da digitação de dados deve ser dada quando o usuário digitar 0 (zero) no campo código.
Ao encerrar o programa também deve ser informados os códigos e valores do clente mais alto, do mais baixo,
do mais gordo e do mais magro, além da média das alturas e dos pesos dos clientes
"""
contador_clientes = 0
acum_altura = 0
acum_peso = 0
codigo = 99999

while codigo != 0:
    codigo = int(input('\nDigite o código do cliente \n(0) para finalizar o programa '))
    if codigo != 0:
        contador_clientes += 1
        peso = float(input('Qual é o seu peso: '))
        altura = float(input('Qual é a sua altura: '))

        acum_altura += altura
        acum_peso += peso

        if contador_clientes == 1:
            gordo = peso
            magro = peso
            alto = altura
            baixo = altura
            id_gordo = codigo
            id_magro = codigo
            id_alto = codigo
            id_baixo = codigo

        else:

            if peso > gordo:
                gordo = peso
                id_gordo = codigo
            if peso < magro:
                magro = peso
                id_magro = codigo
            if altura > alto:
                alto = altura
                id_alto = codigo
            if baixo > altura:
                baixo = altura
                id_baixo = codigo

print('\nPROGRAMA ENCERRADO')
print(
    f'\nA média de peso dos clientes foi de {acum_peso / contador_clientes} Kg\nA média de altura dos clientes foi de '
    f'{acum_altura / contador_clientes} metros\n')
print(
    f'\nO cliente mais gordo é o de código {id_gordo}, com {gordo} Kg\nO cliente mais magro é o de código {id_magro}, '
    f'com {magro} Kg')
print(
    f'\nO cliente mais baixo é o de código {id_baixo}, com {baixo} metros\nO cliente mais alto é o de código {id_alto}, '
    f'com {alto} metros')