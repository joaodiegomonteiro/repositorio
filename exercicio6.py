#Solicite as três notas do aluno
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))

# Calcula a média das notas
media = (nota1 + nota2 + nota3) / 3

# Exibe o resultado com base na média
if media >= 7:
    print(f"A média é {media:.2f}. Aluno aprovado.")
else:
    print(f"A média é {media:.2f}. Aluno reprovado.")