"""
EXERCÍCIO 02: Consumo da Kawasaki Versys 300
Disciplina: Lógica de Programação com Python

ENUNCIADO:
Para planejar uma viagem técnica de Tianguá até o Beach Park (Aquiraz),
solicite:
1. A distância total percorrida (em Km).
2. O total de combustível gasto (em Litros).

Calcule e imprima o consumo médio da motocicleta (Km/L) formatado com 2 casas decimais.
"""

# TODO: Desenvolva o algoritmo abaixo:
distancia = float(input("Distância total percorrida"))
combustivel_gasto = float(input("Total de litros de gasolina gastos"))
consumo_medio = distancia / combustivel_gasto
print(f"O consumo médio da Kawasaki foi de {consumo_medio:.2f}, Km/l")