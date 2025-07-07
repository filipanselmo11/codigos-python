novaFila = []

while True:
    print("Digite I para inserir um elemento na fila")
    print("Digite R para remover um elemento da fila")
    print("Digite T para ver o tamanho da lista")
    print("Digite H para ver os elementos da lista")
    print("Digite S para sair do programa")
    print()

    op = input("Digite a opção desejada: ")
    print()

    if op == "I":
        print("Escolha a regra de inserção:")
        print("1 - Inserir apenas valores pares e que não estejam na fila")
        print("2 - Inserir apenas valores positivos e que não estejam na fila")
        regra = input("Digite 1 ou 2: ")
        print()
        entrada = int(input("Digite o valor a ser inserido: "))
        if regra == "1":
            if entrada % 2 == 0:
                if entrada in novaFila:
                    print(f"O valor {entrada} já existe na fila, não será adicionado novamente.")
                else:
                    novaFila.append(entrada)
                    print(f"{entrada} (par) foi inserido na fila.")
            else:
                print("O valor informado não é par, não será adicionado à fila.")
        elif regra == "2":
            if entrada > 0:
                if entrada in novaFila:
                    print(f"O valor {entrada} já existe na fila, não será adicionado novamente.")
                else:
                    novaFila.append(entrada)
                    print(f"{entrada} (positivo) foi inserido na fila.")
            else:
                print("O valor informado não é positivo, não será adicionado à fila.")
        else:
            print("Opção de regra inválida.")
        print()

    elif op == "R":
        if len(novaFila) > 0:
            itemRemovido = novaFila.pop(0)
            print(f"{itemRemovido} foi removido da fila")
        else:
            print("A fila está vazia, não há elementos para remover")
        print()

    elif op == "T":
        tamanho = len(novaFila)
        print(f"O tamanho atual da fila é: {tamanho}")
        print()

    elif op == "H":
        if len(novaFila) > 0:
            print("Elementos na fila:")
            for item in novaFila:
                print(item)
            print()
        else:
            print("A fila está vazia")
            print()

    elif op == "S":
        print("Saindo do programa...")
        break

    else:
        print("Opção inválida, por favor selecione uma opção válida")
        print()
