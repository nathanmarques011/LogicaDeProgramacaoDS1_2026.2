"""
EXERCÍCIO 05: Acesso à Bilheteria do Parque
Disciplina: Lógica de Programação com Python

ENUNCIADO:
Receba a idade do visitante (valor base do ingresso: R$ 100,00):
- Menor que 12 anos: "Infantil" (50% de desconto -> R$ 50,00)
- Maior ou igual a 60 anos: "Melhor Idade" (Gratuidade -> R$ 0,00)
- Demais idades: "Integral" (R$ 100,00)

Imprima o tipo de bilhete e o valor final a pagar.
"""

# TODO: Desenvolva o algoritmo abaixo:
idade = int(input("digite sua idade"))
ingresso = 100
if idade < 12 :
    valor_final = ingresso * 0.5
    print(f"Ingresso Infantil : R$ {valor_final}")
elif idade >= 60 :
    valor_final = 0
    print(f"Melhor idade : R$ {valor_final}")
else :
    print(f"Ingresso integral {ingresso}")