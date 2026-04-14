# Crie um programa em Python que registre as notas de 3 alunos em 4 provas usando
# uma matriz (lista de listas), calcule a media de cada aluno.
# Use seu conhecimento de laços para cumprir a tarefa.

notas = []

for i in range(3): 
    aluno = []
    
    for j in range(4):  
        nota = float(input(f"{i+1}º aluno, {j+1} ª prova. A nota foi: "))
        aluno.append(nota)
    
    notas.append(aluno)

for i in range(3):
    soma = 0
    
    for j in range(4):
        soma += notas[i][j]
    
    media = soma / 4
    print(f"Média do aluno {i+1}: {media}")