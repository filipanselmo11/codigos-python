
lista = []
tamLista = len(lista)

while tamLista < 9:
    x = int(input("Digite um valor para x: "))
    lista.append(x)
    tamLista = len(lista)

print()

print(f"Lista: {lista}")
print(f"Tamanho da lista: {tamLista}")

print()

listaNumeroPositivo = []
listaNumeroNegativo = []


for indice in range(tamLista):
    # print(f"Elementos da fila: {fila[indice]}")

    if lista[indice] > 0:
        print(f"O elemento {lista[indice]} é um número positivo")
        print()
        listaNumeroPositivo.append(lista[indice])
    else:
        print(f"O elemento {lista[indice]} é um número negativo")
        print()
        listaNumeroNegativo.append(lista[indice])


print(f"Lista de números positivos: {listaNumeroPositivo}")
print(f"Lista de números negativos: {listaNumeroNegativo}")

i = 0
elementosRepetidos = []

while i < tamLista:
    j = i + 1
    while j < tamLista:
        if lista[i] == lista[j]:
            # elementosRepetidos.append(lista[i])
            if lista[i] not in elementosRepetidos:
                elementosRepetidos.append(lista[i])
        else:
            print(f"A lista não possui elementos repetidos")
        j += 1
    i += 1

print(f"Lista de elementos repetidos: {elementosRepetidos}")




