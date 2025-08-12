#Calcula a media de notas

notas = [0, 0, 0, 0, 0]
soma = 0
x = 0

#versão com while
while x < 5:
    notas[x] = float(input("Digite a nota: "))
    soma += notas[x]
    x += 1

x = 0
while x < 5:
    print("Nota", x + 1, ":", notas[x])
    x += 1

print("Média das notas (while):", soma / 5)