"""
Faça um programa que leia e valide as seguintes informações:

Nome: maior que 3 caracteres;
Idade: entre 0 e 150;
Salário: maior que zero;
Sexo: 'f' ou 'm';
Estado Civil: 's', 'c', 'v', 'd';
"""
nome = str(input('Digite o nome (deve ser maior que 3 caracteres) '))
while len(nome) < 4:
    print('Nome informado não tem a quantidade mínima de caracteres! ')
    nome = str(input('Digite um nome com mais de 3 caracteres: '))

salario = float(input('Digite o seu salário: '))
while salario <= 0:
    print('Valor de salário inválido! ')
    salario = float(input('Digite um valor maior que 0: '))

sexo = str(input('Digite o seu sexo. M para MASCULINO ou F para FEMININO: '))
sexo = sexo.upper()
while (sexo != 'M') and (sexo != 'F'):
    print('Sexo inválido! ')
    sexo = str(input('Digite um valor válido para o sexo, M para MASCULINO ou F para FEMININO: '))
    sexo = sexo.upper()

estado_civil = str(input('Digite o estado civil. S para SOLTEIRO, c para CASADO, V para VIUVO ou D para DIVORCIADO:  '))
estado_civil = estado_civil.upper()
while (estado_civil != 'S') and (estado_civil != 'C') and (estado_civil != 'V') and (estado_civil != 'D'):
    print('Estado civil inválido! ')
    estado_civil = str(input('Digite um valor válido para o ESTADO CIVIL, S para SOLTEIRO, c para CASADO, '
                             'V para VIUVO ou D para DIVORCIADO: '))
    estado_civil = estado_civil.upper()
