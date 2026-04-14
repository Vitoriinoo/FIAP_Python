# ====================================== EX02 ======================================
# Crie um programa em Python que compare dois números, peça ao usuario os numeros e
# compare se eles são iguais.

numeros = []

for i in range(2):
    i = float(input(f"Digite o {i+1}° número: "))
    numeros.append(i)

if numeros[0] == numeros[1]:
    print(f"OS números são iguais.")

else:
    print(f"Os números são diferentes.")