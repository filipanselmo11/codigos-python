minhaLista = [0, 1, 2, 3, 4, 5, 6, 7, 1000, .0909090, "Oi", "Python", True, False]
outra_lista = ["Python", -30, 1, 2, 3, 4, 5, False, True, "Feijao", -10.676, "Tambaqui"]

# print("Estado atual da minha Lista: ", minhaLista)
# print("Tamanho da minha Lista: ", len(minhaLista))
# print("\n")
# for i in range(len(minhaLista)):
#     print("Índices da minha Lista: ", i)
# print("\n")
# for elemento in range(len(minhaLista)):
#     print("Elementos da minha Lista: ", minhaLista[elemento])
# print("\n")
# for k in range(len(minhaLista)):
#     for j in range(len(outra_lista)):
#         if minhaLista[k] == outra_lista[j]:
#             print(f"O elemento {minhaLista[k]} é igual ao elemento {outra_lista[j]}")
#             print(f"Tipo do elemento: {type(minhaLista[k])}")
#         elif minhaLista[k] != outra_lista[j]:
#             print(f"O elemento {minhaLista[k]} é diferente do elemento {outra_lista[j]}")
# if minhaLista[k] in outra_lista:
#     print(f"O elemento {minhaLista[k]} está na outra lista")

# Versão usando while
k = 0
while k < len(minhaLista):
    j = 0
    while j < len(outra_lista):
        if minhaLista[k] == outra_lista[j]:
            print(f"O elemento {minhaLista[k]} é igual ao elemento {outra_lista[j]}")
            print(f"Tipo do elemento: {type(minhaLista[k])}")
        j += 1
    k += 1