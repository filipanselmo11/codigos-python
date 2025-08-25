notas = []
notasMaioresCinco = []
notasMenoresCinco = []

for i in range(5):
    nota = float(input("Digite a nota: "))
    notas.append(nota)


print()
print("Notas dos alunos: ", notas)

for i in range(len(notas)):
    if notas[i] >= 5:
        notasMaioresCinco.append(notas[i])
    elif notas[i] < 5:
        notasMenoresCinco.append(notas[i])

print()
print("Notas maiores ou iguais a 5: ", notasMaioresCinco)
print()
print("Notas menores que 5: ", notasMenoresCinco)
