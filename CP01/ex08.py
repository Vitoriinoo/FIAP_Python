# Crie um programa em Python que registre 3 notas de alunos, garantindo que 
# cada nota seja válida, use as estruturas de laço for e while.
notas = []

for i in range(3):
    while True:
        nota = float(input(f"Digite a {i+1}ª nota: "))
        if 0 <= nota <= 10:
            notas.append(nota)
            break
        else:
            print("Nota inválida! Digite um valor entre 0 e 10.")
print(f"Notas registradas: {notas}")

