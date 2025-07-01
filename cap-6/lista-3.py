minhaLista = []
print("Tamanho inicial da Lista: ", len(minhaLista))

while len(minhaLista) < 10:
    print("Tamanho da lista é menor que 10, adicionando um elemento")
    elemento = input("Digite um elemento para adicionar à lista: ")
    minhaLista.append(elemento)
    print("Tamanho atual da lista: ", len(minhaLista))

print("Tamanho da lista é 10, saindo do loop")
print("Estado final da Lista: ", minhaLista)