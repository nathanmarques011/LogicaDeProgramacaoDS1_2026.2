
media_aluno = float(input("Média do aluno"))
frequencia_percentual = int(input("Percentual de frequência do aluno"))

media_final = media_aluno >=6
frequencia_final = frequencia_percentual >=75

resultado = media_final and frequencia_final
print("Você foi aprovado? ->", resultado)

