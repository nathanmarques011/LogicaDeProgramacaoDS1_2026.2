"""
EXERCÍCIO 04: Positivos e Média
Disciplina: Lógica de Programação com Python

ENUNCIADO:
Leia 6 valores numéricos.
Conte quantos foram estritamente positivos (> 0) e calcule a média aritmética deles.
Imprima a quantidade de positivos e a média formatada com 1 casa decimal.
"""

# TODO: Desenvolva o algoritmo abaixo:
quantia = 0
soma = 0
print("digite 6 valores numericos")
for i in range (1, 7) :
    valor = float(input(f"Digite o {i}° número"))
    if valor >0 :
        quantia = quantia + 1
        soma += valor
    if quantia > 0 :
        media = valor / quantia
print(media)