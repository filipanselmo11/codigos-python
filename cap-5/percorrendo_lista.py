
nomes = ["Ana", "João", "Carlos"]

#Usando o for
print("Usando o for")
for nome in nomes:
    print("Nome: ", nome)

#Usando o while. Sempre tem que ter um contador
print("Usando o while")
contador = 0
tam_nome = len(nomes)
while(contador < tam_nome):
    print("Nome: ", nomes[contador])
    contador += 1