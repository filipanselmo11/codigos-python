
lista = []
numerosPositivos = []
numerosNegativos = []

for i in range(10):
    numero = int(input("Digite um numero: "))
    lista.append(numero)

print(f"Lista Original: {lista}")

for i in range(len(lista)):
    if lista[i] > 0:
        numerosPositivos.append(lista[i])
    elif lista[i] < 0:
        numerosNegativos.append(lista[i])


print(f"Lista de numeros maiores que 0: {numerosPositivos}")
print(f"Lista de numeros menores que 0: {numerosNegativos}")
