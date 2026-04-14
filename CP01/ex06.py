# Crie um programa em Python que peça números ao usuário e some todos eles.
# Use o laço while e receba numeros ate que uma condição seja atendida
soma_total = 0
num = 1

while True:
    num = float(input(f"Digite um número para ser adicionado (insira -1 para parar o programa): "))
    if num < 0:
        break
    soma_total += num
    
print(f"Condição atendida. A soma final foi: {soma_total}. Parabéns ")
