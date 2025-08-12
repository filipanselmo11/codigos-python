
notas = []

notaMaiorIgualCinco = []
notaMenorCinco = []

for i in range(5):
    nota = float(input("Informe uma nota: "))
    notas.append(nota)

print(f"Notas dos alunos: ", notas)

for i in range(len(notas)):
    if notas[i] >= 5:
        notaMaiorIgualCinco.append(notas[i])
    elif notas[i] < 5:
        notaMenorCinco.append(notas[i])

print(f"Notas Maiores ou Iguais a 5: {notaMaiorIgualCinco}")
print(f" Notas Menores que 5: {notaMenorCinco}")