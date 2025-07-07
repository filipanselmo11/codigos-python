
minhaFila = ["João", "Maria", "Pedro", "Ana"]
# minhaFila = []

print(f"Estado inicial da fila: {minhaFila}")

nome = input("Informe o nome da pessoa que vai entrar na fila: ")

minhaFila.append(nome)
# minhaFila.insert(0, nome)  # Insere o novo elemento no início da fila

print(f"{nome} foi adicionado(a) à fila")
print()

print(f"Estado atual da fila: {minhaFila}")
print()
# indice = 0
indice = int(input("Informe o índice da pessoa que vai sair da fila (0 para o primeiro): "))
print()

if indice == 0:
    removido = minhaFila.pop(indice)
    print(f"{removido} foi removido(a) da fila")
    print()
else:
    print("Não foi possível realizar a remoção, pois o índice informado não é 0, ou seja quebra a regra da fila (FIFO - First In, First Out).")
    print()
# minhaFila.pop() # Remove o último elemento da fila
# minhaFila.pop(0) # Remove o primeiro elemento da fila


print(f"Estado final da fila: {minhaFila}")