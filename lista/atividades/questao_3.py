
inteiros = []

cont = 0

while cont < 3:
    numero = int(input("Digite um número inteiro: "))
    inteiros.append(numero)
    cont += 1

print()
print("Números inteiros digitados: ", inteiros)

inteirosInvertidos = []
# for k in range(len(inteiros)-1, -1, -1):
#     inteirosInvertidos.append(inteiros[k])
inteirosInvertidos = inteiros[::-1]

print()
print("Números inteiros na ordem inversa: ", inteirosInvertidos)