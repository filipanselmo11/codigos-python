# Insertion Sort usando while ao invés de for
lista = [5, 3, 8, 4, 2]

print(f"Antes de ordenar: {lista}")

i = 1
while i < len(lista):
    chave = lista[i]
    j = i - 1
    # Move os elementos maiores que a chave para frente
    while j >= 0 and lista[j] > chave:
        lista[j + 1] = lista[j]
        j -= 1
    lista[j + 1] = chave
    i += 1

print(f"Lista ordenada (Insertion sort): {lista}")
