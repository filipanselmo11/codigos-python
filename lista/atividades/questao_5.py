
lista = []

for i in range(10):
    inteiro = int(input("Digite um número inteiro: "))
    lista.append(inteiro)



print()
print("Números inteiros digitados: ", lista)

numerosNegativos = []
numerosPositivos = []

for k in range(len(lista)):
    if (lista[k] > 0):
        numerosPositivos.append(lista[k])
    else:
        numerosNegativos.append(lista[k])


print()
print("Numeros Positivos: ", numerosPositivos)
print("Numeros Positivos: ", numerosNegativos)
