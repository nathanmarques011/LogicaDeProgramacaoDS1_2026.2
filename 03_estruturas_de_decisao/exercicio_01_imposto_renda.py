"""
EXERCÍCIO 01: Imposto de Renda de Lisarb
Disciplina: Lógica de Programação com Python

ENUNCIADO:
Leia o salário de uma pessoa em Rombus (R$).
- Até R$ 2000.00: Isento
- De R$ 2000.01 até R$ 3000.00: 8% sobre o excedente de R$ 2000.00
- De R$ 3000.01 até R$ 4500.00: 18% sobre o excedente de R$ 3000.00 + 8% da faixa anterior
- Acima de R$ 4500.00: 28% sobre o que ultrapassar R$ 4500.00 + impostos anteriores

Imprima "Isento" ou o valor total do imposto formatado com 2 casas decimais.
"""

# TODO: Desenvolva o algoritmo abaixo:
salario = float(input("Digite seu salário em R$"))
taxa1 = 0.08
taxa2 = 0.18
taxa3 = 0.28

if salario <= 2000 :
     print("isento")
elif salario > 2000 :
     taxa = salario * taxa1
elif salario > 3000 :
     excedente = salario - 3000
     taxa = (excedente * taxa2) + salario * taxa1
elif salario > 4500 :
     excedente = salario - 4500
     taxa = (excedente * taxa3) + salario * taxa2 + salario + taxa3
salario_real = salario + taxa
print(f"O seu salário com as devidas taxas aplicadas é de {salario_real: .2f}")