"""
Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao nome do usuário,
mostrando uma mensagem de erro e voltando a pedir as informações.
"""
usuario = str(input('Digite o nome de USUÁRIO: '))
senha = str(input('Digite a senha a ser utilizada: '))

usuario = usuario.upper()
senha = senha.upper()

while usuario == senha:
    print('Senha inválida!\nA senha não pode ser igual ao nome do usuário!\n')
    senha = str(input('Digite uma senha válida: '))
    senha = senha.upper()

print('Senha válida, parâmetros salvos!')
