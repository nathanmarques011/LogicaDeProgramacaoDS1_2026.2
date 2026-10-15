"""
EXERCÍCIO 04: Função Lambda de Desconto Casas Paulino
Disciplina: Lógica de Programação com Python

ENUNCIADO:
Escreva uma função anônima (lambda) que receba o valor de um produto
e retorne o valor com 15% de desconto à vista aplicado.
"""

# TODO: Desenvolva a expressão lambda e teste-a abaixo:
valor_com_desconto = lambda c: (c - c * 0.15)
valor = float(input("Digite o valor que quer aplicar o desconto:"))
print(f"O valor com desconto de 15% aplicado é de {valor_com_desconto(valor): .2f}")