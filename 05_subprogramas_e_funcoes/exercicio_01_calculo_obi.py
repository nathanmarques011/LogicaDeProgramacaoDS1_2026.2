"""
EXERCÍCIO 01: Pontuação OBI (Astro Lume Devs)
Disciplina: Lógica de Programação com Python

ENUNCIADO:
Crie uma função nomeada `calcular_pontuacao_total(fase1, fase2, fase3)` com a diretiva `def`
que receba as 3 notas como parâmetros e retorne a pontuação total da equipe.
"""

# TODO: Desenvolva a função e os testes abaixo:
def calcular_pontuacao_total (fase1, fase2, fase3) :
    valor_total = fase1 + fase2 + fase3
    return valor_total
valor1 = int(input("Digite o valor obtido na fase 1: "))
valor2 = int(input("Digite o valor obtido na fase 2: "))
valor3 = int(input("Digite o valor obtido na fase 3: "))
pontuacao = calcular_pontuacao_total (valor1, valor2, valor3)
print(f"A pontuação total da equipe é: {pontuacao}")