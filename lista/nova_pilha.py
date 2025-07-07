
novaPilha = []

continuar = True

while continuar:
    print("Digite A para empilhar elementos na pilha")
    print("Digite R para desempilhar elementos da pilha")
    print("J para ver os elementos da pilha")
    print("Digite S para sair do sistema")
    print()

    op = input("Digite a opcao desejada: ")

    if op == "A":
        elemento = int(input("Informe o valor do elemento: "))