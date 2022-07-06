"""
Faça um Programa para um caixa eletrônico. O programa deverá perguntar ao usuário a valor do saque e depois informar
quantas notas de cada valor serão fornecidas. As notas disponíveis serão as de 1, 5, 10, 50 e 100 reais.
O valor mínimo é de 10 reais e o máximo de 600 reais. O programa não deve se preocupar com a quantidade de notas
existentes na máquina.

Exemplo 1: Para sacar a quantia de 256 reais, o programa fornece duas notas de 100, uma nota de 50, uma nota de 5 e
uma nota de 1;
Exemplo 2: Para sacar a quantia de 399 reais, o programa fornece três notas de 100, uma nota de 50, quatro notas de 10,
uma nota de 5 e quatro notas de 1.
"""
saque = int(input('Digite o valor do SAQUE:\nValor mínimo de RS 10,00 e máximo de RS 600,00 '))
if 10 <= saque <= 600:
    if saque >= 100:
        cedula_100_str = divmod(saque, 100)
        cedula_100 = cedula_100_str[0]
        if cedula_100_str[1] == 0:
            print(f'Você receberá {cedula_100} notas de 100 reais.')
        else:
            if cedula_100_str[1] >= 50:
                cedula_50_str = divmod(cedula_100_str[1], 50)
                cedula_50 = cedula_50_str[0]
                if cedula_50_str[1] == 0:
                    print(f'Você receberá {cedula_100} notas de 100 reais e {cedula_50} nota de 50 reais.')
                else:
                    if cedula_50_str[1] >= 10:
                        cedula_10_str = divmod(cedula_50_str[1], 10)
                        cedula_10 = cedula_10_str[0]
                        if cedula_10_str[1] == 0:
                            print(
                                f'Você receberá {cedula_100} notas de 100 reais, {cedula_50} nota de 50 reais '
                                f'e {cedula_10} notas de 10 reais.')
                        else:
                            cedula_1_str = divmod(cedula_10_str[1], 1)
                            cedula_1 = cedula_1_str[0]
                            print(
                                f'Você receberá {cedula_100} notas de 100 reais, {cedula_50} nota de 50 reais, '
                                f'{cedula_10} notas de 10 reais e {cedula_1} notas de 1 real.')
                    else:
                        cedula_1_str = divmod(cedula_50_str[1], 1)
                        cedula_1 = cedula_1_str[0]
                        print(
                            f'Você receberá {cedula_100} notas de 100 reais, {cedula_50} nota de 50 reais '
                            f'e {cedula_1} notas de 1 real.')

            else:  # EXISTE NOTA DE 100. NÃO EXISTE DE 50. PULA PRA CA
                if cedula_100_str[1] >= 10:
                    cedula_10_str = divmod(cedula_100_str[1], 10)
                    cedula_10 = cedula_10_str[0]
                    if cedula_10_str[1] == 0:
                        print(f'Você receberá {cedula_100} notas de 100 reais e {cedula_10} notas de 10 reais.')
                    else:
                        cedula_1_str = divmod(cedula_10_str[1], 1)
                        cedula_1 = cedula_1_str[0]
                        print(
                            f'Você receberá {cedula_100} notas de 100 reais, {cedula_10} notas de 10 reais '
                            f'e {cedula_1} notas de 1 real.')

                else:  # não existe nota de 10, pular pra 1 real
                    if cedula_100_str[1] >= 1:
                        cedula_1_str = divmod(cedula_100_str[1], 1)
                        cedula_1 = cedula_1_str[0]
                        print(f'Você receberá {cedula_100} notas de 100 reais e {cedula_1} notas de 1 real.')

    # NAO EXISTE NOTA DE 100, PULAR PRA CÁ

    else:
        if saque >= 50:
            cedula_50_str = divmod(saque, 50)
            cedula_50 = cedula_50_str[0]
            if cedula_50_str[1] == 0:
                print(f'Você receberá {cedula_50} nota de 50 reais.')
            else:
                if cedula_50_str[1] >= 10:
                    cedula_10_str = divmod(cedula_50_str[1], 10)
                    cedula_10 = cedula_10_str[0]
                    if cedula_10_str[1] == 0:
                        print(f'Você receberá{cedula_50} nota de 50 reais e {cedula_10} notas de 10 reais.')
                    else:
                        cedula_1_str = divmod(cedula_10_str[1], 1)
                        cedula_1 = cedula_1_str[0]
                        print(
                            f'Você receberá {cedula_50} nota de 50 reais, {cedula_10} notas de 10 reais '
                            f'e {cedula_1} notas de 1 real.')

                else:
                    cedula_1_str = divmod(cedula_50_str[1], 1)
                    cedula_1 = cedula_1_str[0]
                    print(f'Você receberá {cedula_50} nota de 50 reais e {cedula_1} notas de 1 real.')

        # NAO EXISTEM NOTAS DE 100 NEM 50, PULAR PRA CA
        else:
            if saque >= 10:
                cedula_10_str = divmod(saque, 10)
                cedula_10 = cedula_10_str[0]
                if cedula_10_str[1] == 0:
                    print(f'Você receberá {cedula_10} notas de 10 real.')
                else:
                    cedula_1_str = divmod(cedula_10_str[1], 1)
                    cedula_1 = cedula_1_str[0]
                    print(f'Você receberá {cedula_10} nota de 10 reais e {cedula_1} notas de 1 real.')

else:
    print('Você digitou um valor inválido! O valor permitido é de no mínimo 10 e no máximo 600 reais.')
