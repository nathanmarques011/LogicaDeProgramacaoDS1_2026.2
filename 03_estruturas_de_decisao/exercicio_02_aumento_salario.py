"""
EXERCÍCIO 02: Aumento de Salário Escolar
Disciplina: Lógica de Programação com Python

ENUNCIADO:
Leia o salário de um colaborador da escola e aplique o percentual de reajuste:
- 0.00 a 400.00: 15%
- 400.01 a 800.00: 12%
- 800.01 a 1200.00: 10%
- 1200.01 a 2000.00: 7%
- Acima de 2000.00: 4%

Imprima: novo salário, valor do reajuste ganho e percentual aplicado.
"""

# TODO: Desenvolva o algoritmo abaixo:
salario = float(input("Digite seu salario"))
reajuste1 = 0.15
reajuste2 = 0.12
reajuste3 = 0.10
reajuste4 = 0.07
reajuste5 = 0.04

if salario <= 400 :
    salario_reajustado = salario * reajuste1 + salario
elif salario > 400 :
    salario_reajustado = salario * reajuste2 + salario
elif salario > 800 :
    salario_reajustado = salario * reajuste3 + salario
elif salario > 1200 :
    salario_reajustado = salario * reajuste4 + salario
elif salario > 2000 :
    salario_reajustado = salario * reajuste5 + salario

print("O valor do seu salário reajustado é de", salario_reajustado)