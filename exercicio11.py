# Exibe as opções de operação
print("Selecione a operação:")
print("1 - Soma")
print("2 - Subtração")
print("3 - Multiplicação")
print("4 - Divisão")

# Recebe a escolha do usuário
operacao = input("Digite o número da operação desejada (1/2/3/4): ")

# Recebe os números para a operação
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

# Realiza a operação escolhida
if operacao == '1':
    resultado = num1 + num2
    print(f"O resultado da soma é: {resultado}")
elif operacao == '2':
    resultado = num1 - num2
    print(f"O resultado da subtração é: {resultado}")
elif operacao == '3':
    resultado = num1 * num2
    print(f"O resultado da multiplicação é: {resultado}")
elif operacao == '4':
    # Verifica se o divisor é diferente de zero para evitar divisão por zero
    if num2 != 0:
        resultado = num1 / num2
        print(f"O resultado da divisão é: {resultado}")
    else:
        print("Erro: Divisão por zero não é permitida.")
else:
    print("Operação inválida.")

#Esse programa permite que o usuário escolha entre as operações de soma, subtração, multiplicação e divisão, realiza o cálculo e exibe o resultado.