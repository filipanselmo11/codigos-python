notas = [6, 7, 5, 8, 9]
soma = 0
x = 0
tamNotas = len(notas)

while x < tamNotas:
    # soma += notas[x]
    soma = soma + notas[x]
    # x += 1
    x = x + 1

print(f"Soma: {soma}")
print(f"x: {x}")
print(f"Média: {soma / x:.2f}")