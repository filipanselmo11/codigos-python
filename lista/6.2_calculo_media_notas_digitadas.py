
notas = [0, 0, 0, 0, 0]
soma = 0
x = 0
tamNotas = len(notas)

while x < tamNotas:
    notas[x] = float(input(f"nota[{x}]:"))
    print("Array de Notas: ", notas)
    soma = soma + notas[x]
    x = x + 1

# print(f"Notas: {notas}")

x = 0

print("\t")
while x < tamNotas:
    print(f"Nota {x}: {notas[x]:.2f}")
    print("\t")
    x = x + 1

print("\t")
print(f"Soma: {soma:.2f}")
print(f"x: {x}")
print(f"Média: {soma / x:.2f}")