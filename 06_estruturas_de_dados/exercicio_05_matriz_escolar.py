"""
EXERCÍCIO 05: Matriz Bidimensional Escolar
Disciplina: Lógica de Programação com Python

ENUNCIADO:
Crie uma matriz com 3 alunos [nome, nota1, nota2].
Percorra a matriz, calcule a média de cada um e exiba:
"Aluno: [Nome] | Média: [Média] | Situação: [Aprovado / Prova Final]"
(Critério: Média >= 6.0 aprovado).
"""

# TODO: Desenvolva o algoritmo abaixo:
alunos = [
    ["Nathan", 8.0, 7.0],
    ["Ana", 5.0, 6.0],
    ["Pedro", 9.0, 8.0]
]

for aluno in alunos:
    nome = aluno[0]
    nota1 = aluno[1]
    nota2 = aluno[2]

    media = (nota1 + nota2) / 2

    if media >= 6.0:
        situacao = "Aprovado"
    else:
        situacao = "Prova Final"

    print(f"Aluno: {nome} | Média: {media:.1f} | Situação: {situacao}")