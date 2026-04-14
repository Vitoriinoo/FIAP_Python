# Crie um programa em Python que simule um sistema simples de login.
# Usar um primeiro laço while para pedir o nome de usuário até que 
# o usuário digite o valor correto, faça o mesmo para a senha.

nome_usr = input("Digite o seu nome de usuário: ")
senha_usr = input("Digite a sua senha: ")

print("Para realizar seu acesso, digite o que for solicitado: ")


verificacao_nome = input("Digite seu nome de usuário: ")
verificacao_senha = input("Digite a sua senha: ")

while verificacao_nome != nome_usr or verificacao_senha != senha_usr:
        print("Nome de usuário e/ou senha incorreto. Verifique e tente novamente.")
        verificacao_nome = input("Digite seu nome de usuário: ")
        verificacao_senha = input("Digite a sua senha: ")
        break


print("Acesso concedido")

