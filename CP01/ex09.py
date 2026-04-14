# Crie um programa em Python que registre números digitados pelo usuário e 
# conte quantos são positivos. Use o laço while para registrar todas as entradas
# depois use o laço for para percorrer toda a lista e fazer a contagem.
lista_nums = []

while True:
    nums = float(input("Digite um número (digite 0 para parar): "))

    if nums == 0:
        break
    lista_nums.append(nums)

nums_positivos = 0

for num in lista_nums:
    if num > 0:
        nums_positivos += 1

    print(f"A quantidade de números postivos: {nums_positivos}")
