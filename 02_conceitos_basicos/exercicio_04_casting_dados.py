"""
EXERCÍCIO 04: Casting de Dados e Idade em 2026
Disciplina: Lógica de Programação com Python

ENUNCIADO:
Receba do usuário o ano de nascimento como texto (str).
Converta essa entrada para inteiro (int) utilizando o conceito de casting
e calcule a idade que a pessoa completará até o final de 2026.
Imprima a idade calculada com uma mensagem personalizada.
"""

# TODO: Desenvolva o algoritmo abaixo:
ano_de_nascimento = str(input("Digite seu ano de nascimento"))
ano_de_nascimento_numero = int(ano_de_nascimento)
idade_final_do_ano = 2026 - ano_de_nascimento_numero
print("Sua idade até o final de 2026 será de", idade_final_do_ano)