pilha = []

print(f"Estado inicial da pilha: {pilha}")

print()

while True:
    print("Digite E para empilhar um prato na pilha")
    print("Digite D para desempilhar um prato da pilha")
    print("Digite S para ver status atual da pilha")
    print("Digite X para sair do programa")
    print()

    op = input("Digite a opção desejada: ")
    print()

    if op == "E":
        prato = input("Digite o nome do prato que vai ser empilhado: ")
        pilha.append(prato)
        print()
        print(f"{prato} foi empilhado na pilha")
        print()
    
    elif op == "D":
        if len(pilha) > 0:
            prato = pilha.pop(-1)
            print(f"{prato} foi desempilhado da pilha")
            print()
        else:
            print("A pilha está vazia, não há pratos para desempilhar")
            print()

    elif op == "S":
        if len(pilha) > 0:
            print("Estado atual da pilha (do topo para a base):")
            for prato in reversed(pilha):
                print(prato)
            print()
        else:
            print("A pilha está vazia")
            print()

    elif op == "X":
        print("Saindo do programa...")
        break

    else:
        print("Opção inválida, por favor tente novamente")
        print()