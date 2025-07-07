#FIFO - FIRST IN, FIRST OUT

fila = []

print(f"Estado inicial da fila: {fila}")

print("\n")

while True:
    print("Digite A para adicionar uma pessoa à fila")
    print("Digite P para remover uma pessoa da fila")
    print("Digite E para ver o estado atual da fila")
    print("Digite S para sair do programa")
    print("\n")

    op = input("Digite a opção desejada: ")

    if op == "A":
        nome = input("Digite o nome da pessoa que vair entrar na fila: ")
        fila.append(nome)
        print(f"{nome} foi adicionado à fila")
        print("\n")

    elif op == "P":
        # nome = fila.pop(0)
        # print(f"{nome} foi removido da fila")
        # print("\n")
        if len(fila) > 0:
            nome = fila.pop(0)
            print(f"{nome} foi removido da fila")
            print("\n")
        else:
            print("A fila está vazia, não há ninguém para remover")
            print("\n")

    elif op == "E":
        print(f"Estado atual da fila: {fila}")
        print("\n")

    elif op == "S":
        print("Saindo do programa...")
        break

    else:
        print("Opção inválida, por favor tente novamente")
        print("\n")
