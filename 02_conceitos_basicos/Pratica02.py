# TODO: Desenvolva seu algoritmo aqui
# 1. Leia o valor da conta (float)
# 2. Leia o número de pessoas (int)
# 3. Calcule o valor por pessoa
# 4. Imprima formatado usando f-string
valor = float(input("Valor da conta"))
pessoas = int(input("Quantidade de pessoas"))
valor_por_pessoa = valor / pessoas
print(f"O valor que cada um deverá pagar é:{valor_por_pessoa:.2f}")

