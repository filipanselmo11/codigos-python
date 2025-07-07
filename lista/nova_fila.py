

novaFila = []

continuar = True

while continuar:
    print("Digite A para adicionar elementos na fila")
    print("Digite R para remover elementos na fila")
    print("Digite J para ver os elementos da fila")
    print("Digite S para sair do sistema")
    print()

    op = input("Digite a opcao desejada: ")

    if op == "A":
        x = int(input("Digite um valor para x: "))
        if len(novaFila) == 8:
            print("A fila já bateu o tamanho desejado. Não é mais permitido inserir elementos. Segue os elementos abaixo")
            print()
            print(f"Elementos: {novaFila}")
            print()
        else:
            novaFila.append(x)
            print(f"{x} foi adicionado à fila")
            print()

    elif op == "R":
        if len(novaFila) > 0:
            elementoRemovido = novaFila.pop(0)
            print(f"{elementoRemovido} foi removido")
            print()
        else:
            print("A fila está vazia. Não há elementos para remover")
            print()

    elif op == "J":
        print(f"Elementos que estão na fila: {novaFila}")
        print()

    elif op == "S":
        print("Saindo do programa...")
        continuar = False