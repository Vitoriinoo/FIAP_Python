num = 7 
tentativas = 3

user_num = int(input("Tente adivinhar o numero escolhido, esta entre 1 e 10: "))

while user_num != num and tentativas >= 1:
    print(f"Tentativas restante: {tentativas - 1}")
    user_num = int(input("Numero errado, tente novamenete: "))
    tentativas -= 1

if tentativas == 0 and user_num != 7:
    print("Parabéns, vc definitivamnete é um USUARIO!!!")
    print(f"O numero era: {num}")
else:
    print("Parabéns, vc foi promovido a dev")