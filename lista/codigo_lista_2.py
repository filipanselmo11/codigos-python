
lista = []
continuar = True

while continuar:
    x = int(input("Digite um valor para x: "))
    if len(lista) < 4:
        lista.append(x)
    else:
        print("Não é permitido adicionar mais itens")
        print()
        continuar = False


print(f"Lista: {lista}")
print(f"Tamanho da lista: {len(lista)}")

for i in range(len(lista)):
    if lista[i] < 0:
        y = int(input("Informe um valor positivo: "))
        print()
        while y < 0:
            print("Valor inválido. Informe um valor positivo.")
            y = int(input("Informe um valor positivo: "))
            print()
        lista[i] = y

print(f"Lista atualizada: {lista}")