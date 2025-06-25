
matriz = [[1, 2], [3, 4]]

print(matriz[0])
print(matriz[0][0])
print(matriz[0][1])

print("\t")

print(matriz[1])
print(matriz[1][0])
print(matriz[1][1])

print("\t")
# Percorrendo uma matriz
print("Percorrendo uma matriz")
print("\t")
# for linha in matriz:
#     print("Imprimindo linha: ",linha)
#     for elemento in linha:
#         print("Imprimindo elemento: ", elemento)
for linha in matriz:
    for elemento in linha:
        print(elemento)