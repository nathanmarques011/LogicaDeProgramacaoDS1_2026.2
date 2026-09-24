"""
EXERCÍCIO 03: Fórmula de Bhaskara
Disciplina: Lógica de Programação com Python

ENUNCIADO:
Leia 3 valores de ponto flutuante (A, B e C) de uma equação do 2º grau.
- Se A for 0 ou delta for negativo, imprima "Impossivel calcular".
- Caso contrário, calcule e mostre as duas raízes (R1 e R2) formatadas com 5 casas decimais.
"""

# TODO: Desenvolva o algoritmo abaixo:
a = float(input("Digite o ponto A"))
b = float(input("Digite o ponto B"))
c = float(input("Digite o ponto C"))
if a <= 0 :
    print("Impossivel calcular.")
else :
    delta = b ** 2 - 4 * a * c
    x1 = (-b + delta ** 0.5) / (2 * a)
    x2 = (-b - delta ** 0.5) / (2 * a)
    print(f"A raiz 1 é {x1: .5f} e a raiz 2 é {x2: .5f}")