#Parte 1
notas = [10.0, 2.5, 9.5, 7.0, 4.5, 10.0]

#Parte 2
indices = [0, 1, 2, 3, 4, 5]
notas = [10.0, 2.5, 9.5, 7.0, 4.5, 10.0]

#Parte 3
novaNota = 8.5

#Parte 3.1
notas.append(novaNota)

#Parte 3.2
#print("Lista de notas atualizada 3.1: ", notas)

#Parte 3.3
#notas.pop()

#Parte 3.4
#print("Lista de notas atualizada 3.2: ", notas)

#Parte 3.5
#notas.pop(2)
#print("Lista de notas atualizada 3.3: ", notas)

novaLista = [10.0, "Mario", True, False, "Jonas"]
tamNovaLista = len(novaLista)
#Método 1
for i in range(tamNovaLista):
	print(f"Índice ({i}): {novaLista[i]}")

#Método 2

# indice = 0
# while indice < tamNovaLista:
#     print(f"Indice: {indice} - Conteúdo do Índice({indice}): {novaLista[indice]}")
#     indice += 1 #indice = indice + 1
# print(f"Nova lista: {novaLista}")
