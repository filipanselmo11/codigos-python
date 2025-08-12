#Preenchimento de um vetor I

lista = []

for i in range(6):
    valor = int(input("Digite um valor: "))
    lista.append(valor)

print(f"Lista Original: ", lista)

listaDobro = []

for i in range(len(lista)):
    x = lista[i] * 2
    listaDobro.append(x)

print(f"Lista Com Valores Dobrados: ", listaDobro)