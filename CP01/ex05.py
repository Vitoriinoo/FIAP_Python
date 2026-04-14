# ====================================== EX05 ======================================
# Crie um programa em Python que registre 5 números digitados pelo usuário e 
# depois mostre algumas informações sobre eles, use laço For.
# 1 - A lista completa de números
# 2 - O maior número
# 3 - O menor número
# 4 - A soma de todos os números

lista_numeros = []

for i in range(5): 
        numeros_solicitados = float(input(f"Digite o {i+1}º número: "))
        lista_numeros.append(numeros_solicitados)


print(f"Lista completa: {lista_numeros}")
print(f"Maior número: {max(lista_numeros)}")
print(f"Menor número: {min(lista_numeros)}")
print(f"Soma de todos os números: {sum(lista_numeros)}")




