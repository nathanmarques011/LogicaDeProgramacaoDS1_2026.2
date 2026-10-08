"""
EXERCÍCIO 02: Resto da Divisão por 5
Disciplina: Lógica de Programação com Python

ENUNCIADO:
Leia dois valores inteiros X e Y.
Utilize o laço for para imprimir todos os inteiros entre X e Y (em ordem crescente)
cujo resto da divisão por 5 seja igual a 2 ou igual a 3.
"""

# TODO: Desenvolva o algoritmo abaixo:
valor1 = int(input("Digite um valor inteiro" ))
valor2 = int(input("Digite outro valor inteiro "))
print(f"Todos os inteiros entre {valor1} e {valor2} que tem seu resto da divisão sendo 2 ou 3 são: ")
for divisor in range(valor1, valor2 + 1) :
    x = divisor % 5
    if x == 2 or x == 3 :
        print(divisor)