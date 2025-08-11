# Lista de números a serem ordenados
L = [7, 4, 3, 12, 8]

# 'fim' indica até onde o algoritmo deve comparar
fim = 5

print(f"Antes de aplicar a ordenacao: ", L)

# Enquanto ainda há elementos para comparar
while fim > 1:
    trocou = False  # Marca se houve troca nesta passagem
    x = 0  # Índice inicial
    # Percorre a lista até a posição 'fim - 1'
    while x < (fim - 1):
        # Compara elementos vizinhos
        if L[x] > L[x + 1]:
            trocou = True  # Marca que houve troca
            # Troca os elementos de lugar
            temp = L[x]
            L[x] = L[x + 1]
            L[x + 1] = temp
        x += 1  # Avança para o próximo par
    # Se não houve troca, a lista já está ordenada
    if not trocou:
        break
    # Reduz o 'fim', pois o maior elemento já está na posição correta
    fim -= 1

# Imprime a lista ordenada
print(f"Depois de aplicar a ordenacao:", L)
# for elemento in L:
#     print(elemento)