# TODO: Desenvolva o acumulador com parada no 0
soma = 0

# Escreva a estrutura de repetição while
numero = int(input("Digite um número inteiro"))
while numero != 0 :
    soma = soma + numero 
    numero = int(input("Digite outro numero inteiro"))
    continue
    if numero == 0 :
        print("Somando todos os números...")
        break
print(f"A soma de todos os números é {soma}")