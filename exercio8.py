numero = int(input("Digite um numero: "))
 
print(f"Tabuada do {numero}:")
for i in range(1, 11):
    resultado = numero * 1
    print(f"{numero} x {i} = {resultado}")