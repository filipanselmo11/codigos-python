minhaPilha = [3, 2, 1, 900, 200]
# minhaPilha = []

print(f"Estado inicial da pilha: {minhaPilha}")

numero = int(input("Informe o número que vai ser empilhado: "))

minhaPilha.append(numero)
print()

print(f"O {numero} foi empilhado na pilha")
print()

print(f"Estado atual da pilha: {minhaPilha}")
print()

# print(print(f"Topo: {minhaPilha[-1]} - Base: {minhaPilha[0]}"))
# print()

numeroDesempilhado = minhaPilha.pop(-1)

print(f"O {numeroDesempilhado} foi desempilhado da pilha")
print()

print(f"Estado final da pilha: {minhaPilha}")


