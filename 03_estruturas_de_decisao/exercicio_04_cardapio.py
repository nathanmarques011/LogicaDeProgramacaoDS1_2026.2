"""
EXERCÍCIO 04: Cardápio da Lanchonete
Disciplina: Lógica de Programação com Python

TABELA:
1 - Cachorro Quente: R$ 4.00
2 - X-Salada: R$ 4.50
3 - X-Bacon: R$ 5.00
4 - Torrada Simples: R$ 2.00
5 - Refrigerante: R$ 1.50

ENUNCIADO:
Leia o código do item e a quantidade consumida.
Calcule e mostre o total a pagar.
"""

# TODO: Desenvolva o algoritmo abaixo:
print("1 - Cachorro Quente: R$ 4.00")
print("2 - X-Salada: R$ 4.50")
print("3 - X-Bacon: R$ 5.00")
print("4 - Torrada Simples: R$ 2.00")
print("5 - Refrigerante: R$ 1.50")
um = 4.00
dois = 4.50
tres = 5.00
quatro = 2.00
cinco = 1.50
item = int(input("Digite o código do item desejado"))
quantia =  int(input("Digite a quantidade que deseja"))

if item == 1 :
    pagamento = um * quantia
elif item == 2 :
    pagamento = dois * quantia
elif item == 3 :
    pagamento = tres * quantia
elif item == 4 :
    pagamento = quatro * quantia
elif item == 5 :
    pagamento = cinco * quantia

print(f"O pagamento total será de R$ {pagamento: .2f}")