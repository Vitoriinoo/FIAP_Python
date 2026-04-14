numero_usuario = int(input("Digite um numero par: "))

while numero_usuario % 2 !=0: 
    numero_usuario = int(input("tente novamente, digite um numero par: "))
else:
    print(f"O numero {numero_usuario} escolhido pelo usuário é par.")