minhaFila = [
    "Naruto",
    "Fílip",
    "Manoel",
    "Jonas",
    "Francisca",
    "Josefa",
    "Goku",
    "Luffy",
    "Julia",
    "Nina",
    "Yoshimitsu",
    "Leona",
    "Vegeta",
    "Bulma",
    1,
    2,
    3,
    4,
    5
]

tamFila = len(minhaFila)
indice = 0  # cont = 0

while indice < tamFila:
    print(f"Fila atual({indice}): {minhaFila}")
    # print(f"Tamanho atual da fila: {tamFila}")
    item_removido = minhaFila.pop(0)
    print(f"Item removido: {item_removido}")
    print("\t")
    indice += 1
    # tamFila -= 1

print(f"Fila Atual: {minhaFila}")

# Não usar for, quando o tamanho da lista muda(tamanho dinâmico)
# for i in range(tamLista):
#     print(f"Lista Atual({i}):", minhaFila)
#     print("\n")
#     print("Removendo o primeiro item\n")
# if i == 0:
#     minhaFila.pop(i)
#     print(f"Item removido: {minhaFila[i]}")
# minhaFila.pop(i)
# print(f"Item removido: {minhaFila[i]}")
