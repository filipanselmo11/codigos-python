matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print(f"Matriz: {matriz}")

print(f"Acessando um elemento da matriz: {matriz[0][1]}")

print("Elementos da linha 0")
print(matriz[0][0])
print(matriz[0][1]) 
print(matriz[0][2])

print("Percorrendo a matriz")

for linha in matriz:
    for elemento in linha:
        print(elemento)

