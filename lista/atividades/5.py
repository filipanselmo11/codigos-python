notas = []
soma = 0

for i in range(9):
    nota = float(input("Digite uma nota: "))
    notas.append(nota)

print(f"Notas: {notas}")

for i in range(len(notas)):
    soma += notas[i]

print(f"A soma das notas é: {soma}")