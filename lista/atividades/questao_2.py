
valores = []

for i in range(6):
    x = int(input("Digite o valor de x: "))
    valores.append(x)


print()
print("Valores digitados: ", valores)

valoresDobro = [] #doubleValues = []

for j in range(len(valores)):
    dobro = valores[j] * 2
    valoresDobro.append(dobro)

print()
print("Valores dobrados: ", valoresDobro)