# ====================================== EX01 ======================================
# Crie um programa em Python que verifique se uma pessoa pode entrar em um evento 
# se for maior de 18 anos.
while True:

    i = int(input("Digite a sua idade: "))

    if i >= 18 and i <100:
        print("Acesso liberado ao evento")
        break

    elif i < 18 and i >= 0:
        print("Acesso negado, evento permitido apenas para maiores de idade")
        break
    
    else:
        print("O valor digitado não corresponde a uma idade válida(0/100), tente novamente.")
        