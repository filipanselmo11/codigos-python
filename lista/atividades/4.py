x = []

for i in range(3):
    valor = int(input("Valor de X: "))
    x.append(valor)

print(f"Valores de X: {x}")

copiaX = []
#Forma 1
# for i in range(len(x) - 1, -1, -1):
#     copiaX.append(x[i])

#Forma 2
copiaX = x[::-1]

print(f"Copia de X: {copiaX}")