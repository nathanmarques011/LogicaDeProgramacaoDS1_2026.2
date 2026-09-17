"""
EXERCÍCIO 05: Média Ponderada da Avaliação Técnica
Disciplina: Lógica de Programação com Python

ENUNCIADO:
Solicite as notas de três avaliações do curso técnico.
A primeira prova tem peso 2, a segunda peso 3 e a terceira peso 5.
Calcule e exiba a média final ponderada utilizando apenas operadores aritméticos.
"""

# TODO: Desenvolva o algoritmo abaixo:
nota1 = float(input("Digite o valor da primeira nota"))
nota2 = float(input("Digite o valor da segunda nota"))
nota3 = float(input("Digite o valor da terceira nota"))
valor1 = nota1 * 0.2
valor2 = nota2 * 0.3
valor3 = nota3 * 0.5
media_final = valor1 + valor2 + valor3
print(f"Sua média final é de {media_final:.2f}")