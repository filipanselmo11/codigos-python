
lista = []
tamLista = len(lista)
continuar = True

while continuar:
    x = int(input("Digite um valor para x: "))
    if tamLista <= 10:
        lista.append(x)
        tamLista = len(lista)
    else:
        print("Não é permitido adicionar mais itens")
        continuar = False


print(f"Lista: {lista}")
print(f"Tamanho da lista: {tamLista}")

for i in range(tamLista):
    if lista[i] < 0:
        y = int(input("Informe um valor positivo: "))
        lista[i] = y

print(f"Lista atualizada: {lista}")