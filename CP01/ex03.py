# ====================================== EX03 ======================================
# Crie um programa em Python que registre 3 notas de um aluno e determine 
# sua situação na disciplina, peça ao usuario as 3 notas e salve em uma lista, tire 
# a media e se for 7 ou maior ele passou na materia.

lista_notas = []

for i in range(3):
    nota = float(input(f"Digite a {i+1} nota: "))
    lista_notas.append(nota)

soma_notas = sum(lista_notas)
quantidade = len(lista_notas)

if soma_notas / quantidade >= 7:
    print(f"Você passou na matéria")

else:
    print(f"Você não passou na metéria")
 



