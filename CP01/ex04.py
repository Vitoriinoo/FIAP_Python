# Crie um programa em Python que registre 5 produtos comprados em um mercado. 
# Use Listas, laço for e inputs.

compras = []

for i in range(5):
    produtos = input(f"Digite o nome do {i+1}º produto: ")
    compras.append(produtos)

for i in compras:
    print(f"{i}")
