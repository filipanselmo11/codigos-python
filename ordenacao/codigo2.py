
lista = [5, 3, 8, 4, 2]

print(f"Lista antes da ordenação: {lista}")

for i in range(len(lista) - 1):
    for j in range(len(lista) - 1):
        if lista[j] > lista[j + 1]:
            temp = lista[j]
            lista[j] = lista[j + 1]
            lista[j + 1] = temp


print("Lista ordenada (Bubble Sort):", lista)