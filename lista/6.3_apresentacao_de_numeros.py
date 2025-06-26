numeros = [0, 0, 0, 0, 0]
x = 0

while x < 5:
    numeros[x] = int(input(f"Posicao {x + 1} - Número:"))
    x = x + 1

print(f"Lista de números: {numeros}")

while True:
    numero_escolhido = int(
        input("Informe a posição da lista que voce quer imprimir (0 para sair): ")
    )
    if numero_escolhido == 0:
        break
    print(f"Você escolheu o número: {numeros[numero_escolhido - 1]}")
    # print(f"Você escolheu o número: {numeros[numero_escolhido]}")
    # else:
    #     print(f"Você escolheu o número: {numeros[numero_escolhido - 1]}")
