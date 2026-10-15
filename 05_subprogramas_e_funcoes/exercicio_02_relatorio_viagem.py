"""
EXERCÍCIO 02: Modularizando Relatório de Viagem
Disciplina: Lógica de Programação com Python

ENUNCIADO:
Crie duas funções:
1. `calcular_custo_transporte(distancia_km, consumo_kml, preco_combustivel)`
2. `calcular_custo_alimentacao(qtd_pessoas, dias, diaria_alimentacao)`

No programa principal, leia os dados, execute as funções e mostre o custo total da viagem.
"""

# TODO: Desenvolva as funções e o programa principal abaixo:
def calcular_custo_transporte (distancia_km, consumo_kml, preco_combustivel) :
    custo_viagem = consumo_kml * preco_combustivel / distancia_km
    return custo_viagem

def calcular_custo_alimentacao(qtd_pessoas, dias, diaria_alimentacao) :
    custo_alimentacao = diaria_alimentacao * dias * qtd_pessoas
    return custo_alimentacao

distancia = float(input("Digite a distância em KM: "))
consumo = int(input("Qual consumos em KM/L? "))
preco = float(input("Qual preço do combustivel? "))
pessoas = int(input("Quantas pessoas foram? "))
dias = int(input("Quantos dias de viagem foram? "))
diaria = float(input("Qual valor da diaria? "))

custo_total = calcular_custo_transporte (distancia, consumo, preco) + calcular_custo_alimentacao (pessoas, dias, diaria)

print(f"O custo total da viagem foi de {custo_total: .2f}")
