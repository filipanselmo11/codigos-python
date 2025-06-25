numero = int(input("Digite um número (0 para sair): "))
soma = 0

while numero != 0:
    if numero > 0:
        soma += numero
        # soma = soma + numero
    numero = int(input("Digite um número (0 para sair): "))

print("A soma dos números positivos é:", soma)
