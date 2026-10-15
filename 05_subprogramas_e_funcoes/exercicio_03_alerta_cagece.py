"""
EXERCÍCIO 03: Gerador de Alertas da Cagece
Disciplina: Lógica de Programação com Python

ENUNCIADO:
Desenvolva um procedimento `emitir_alerta_fatura(nome_cliente, valor, data_vencimento)`
que imprima a mensagem:
"Prezado(a) [nome], sua fatura da Cagece no valor de R$ [valor] vence no dia [data]."
"""

# TODO: Desenvolva o procedimento abaixo:
def emitir_alerta_fatura(nome_cliente, valor, data_vencimento) :
    alerta = print(F"Prezado(a) {nome_cliente} , sua fatura da Cagece no valor de R$ {valor} vence no dia {data_vencimento}.")
    return alerta
nome = str(input("Digite seu nome: "))
valor = float(input("Digite o valor da fatura: "))
data = input("Digite a data de vencimento: ")
alerta = emitir_alerta_fatura(nome, valor, data)
print(alerta)