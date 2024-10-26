# Solicita um número ao usuário
numero = int(input("Digite um número inteiro: "))

# Assume que o número é primo até que se prove o contrário
eh_primo = True

# Verifica se o número é menor que 2 (pois números menores que 2 não são primos)
if numero < 2:
    eh_primo = False
else:
    # Verifica a divisibilidade do número por valores entre 2 e a metade do número
    for i in range(2, int(numero ** 0.5) + 1):
        if numero % i == 0:
            eh_primo = False
            break

# Exibe se o número é primo ou não
if eh_primo:
    print(f"{numero} é um número primo.")
else:
    print(f"{numero} não é um número. ")