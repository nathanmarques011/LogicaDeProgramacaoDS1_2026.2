"""
DESAFIO 05: O INVENTÁRIO SUSPEITO DO LABORATÓRIO
Disciplina: Lógica de Programação com Python

RELATÓRIO DA INVESTIGAÇÃO:
Elimine duplicatas usando conjuntos (set) e previna o erro KeyError em dicionários
usando o método .get().

SUA MISSÃO:
1. Obtenha a lista de itens únicos a partir de uma lista com duplicatas.
2. Consulte chaves no dicionário de forma segura sem quebrar o programa.
"""

# TODO: Desenvolva o algoritmo abaixo:
itens = ["Mouse", "Teclado", "Monitor", "Mouse", "Teclado", "CPU"]

itens_unicos = set(itens)

print("Itens únicos:", itens_unicos)

inventario = {
    "Mouse": 10,
    "Teclado": 5,
    "Monitor": 3
}

item = input("Digite o item que deseja consultar: ")

quantidade = inventario.get(item, "Item não encontrado")

print("Resultado:", quantidade)