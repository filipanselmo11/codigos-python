
notas = []
soma = 0

for i in range(9):
    nota = float(input("Digite a nota: "))
    notas.append(nota)

print()
print("Notas digitadas: ", notas)

for j  in range(len(notas)):
    soma += notas[j]


print()
print("Soma das notas: ", soma)

