minhaLista = [0, 1, 2, 3, 4, 5, 6, 7, 1000, 0.0909090, "Oi", "Python", True, False]
outra_lista = ["Python", -30, 1, 2, 3, 4, 5, False, True, "Feijao", -10.676, "Tambaqui"]

for i in range(len(minhaLista)):
    for j in range(len(outra_lista)):
        if minhaLista[i] == outra_lista[j]:
            print(f"O elemento {minhaLista[i]} é igual ao elemento {outra_lista[j]}")
            print(f"Tipo do elemento: {type(minhaLista[i])}")
        elif minhaLista[i] != outra_lista[j]:
            print(
                f"O elemento {minhaLista[j]} é diferente do elemento {outra_lista[j]}"
            )
