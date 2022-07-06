"""
Altere o programa de cálculo do fatorial, permitindo ao usuário calcular o fatorial várias vezes e limitando
o fatorial a números inteiros positivos e menores que 16.
"""
print('PROGRAMA PARA CÁLCULO DE FATORIAL( ! )\nDIGITE 99 PARA ENCERRAR')
programa_rodar = True
acumulador = 1

while programa_rodar is True:

    fatorial = int(input('Digite um número natural menor ou igual a 16: \n(99 para encerrar) '))
    contador = fatorial
    if (fatorial > 0) and (fatorial <= 16):
        while contador > 1:
            acumulador *= contador
            contador += -1
        print(acumulador)
        acumulador = 1
    elif fatorial == 99:
        programa_rodar = False
    else:
        print('Você digitou um valor fora do intervalo válido! ')

print('FIM DO PROGRAMA')
