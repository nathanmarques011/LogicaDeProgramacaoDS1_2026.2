"""
EXERCÍCIO 03: Dicionário da Equipe EcoRadar
Disciplina: Lógica de Programação com Python

ENUNCIADO:
Estruture um dicionário com 3 membros (matrícula -> cargo).
Leia uma matrícula via terminal e exiba a função correspondente cadastrada.
"""

# TODO: Desenvolva o algoritmo abaixo:
membros = {
    101: "Professor",
    102: "Aluno",
    103: "Diretor"
}

matricula = int(input("Digite sua matrícula: "))

if matricula in membros:
    print("Cargo:", membros[matricula])
else:
    print("Matrícula não encontrada!")

