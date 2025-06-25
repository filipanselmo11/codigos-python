a = [1, 2, 3, 4, 5, 1]
b = [2, 2, 3, 6, 11, 20, 90, 90, 100]
c = []

tamA = len(a)
tamB = len(b)
tamC = len(c)

# Minha versão
# for i in range(tamA):
#     for j in range(tamB):
#         if a[i] == b[j]:
#             print(f"Elemento do A: {a[i]} - Elemento do B: {b[j]}")
#         else:
#             c = []
#             c.append(a[i])
#             c.append(b[i])

# Versão do GPT
# for i in range(tamA):
#     estar_em_b = False
#     for j in range(tamB):
#         if a[i] == b[j]:
#             estar_em_b = True
#     if estar_em_b == False:
#         if a[i] not in c:
#             c.append(a[i])

# for i in range(tamB):
#     estar_em_a = False
#     for j in range(tamA):
#         if b[i] == a[j]:
#             estar_em_a = True
#     if estar_em_a == False:
#         if b[i] not in c:
#             c.append(b[i])


# print(c)

# Outra versão

# Verifica os elementos de A
# for i in range(tamA):
#     esta_em_b = False
#     for j in range(tamB):
#         if a[i] == b[j]:
#             esta_em_b = True
#     if esta_em_b == False:
        # Verifica se já foi adicionado a c
        # ja_existe = False
        # for k in range(tamC):
        #     if a[i] == c[k]:
        #         ja_existe = True
        # if ja_existe == False:
        #     c.append(a[i])

# Verifica os elementos de B
# for i in range(tamB):
#     esta_em_a = False
#     for j in range(tamA):
#         if b[i] == a[j]:
#             esta_em_a = True
#     if esta_em_a == False:
        # Verifica se já foi adicionado a c
#         ja_existe = False
#         for k in range(tamC):
#             if b[i] == c[k]:
#                 ja_existe = True
#         if ja_existe == False:
#             c.append(b[i])

# print("Elementos exclusivos de A e B:", c)

print("Etapa 1: Verificando elementos de A que não estão em B\n")

for i in range(tamA):
    esta_em_b = False

    for j in range(tamB):
        print(f"Comparando a[{i}] = {a[i]} com b[{j}] = {b[j]}")
        if a[i] == b[j]:
            esta_em_b = True
            print(f"→ {a[i]} existe na lista B\n")

    if esta_em_b == False:
        print(f"{a[i]} NÃO existe na lista B → candidato para a lista C")

        ja_existe = False
        for k in range(tamC):
            if a[i] == c[k]:
                ja_existe = True
                print(f"⚠️ {a[i]} já está na lista C (posição {k}) → não adiciona")

        if ja_existe == False:
            c.append(a[i])
            print(f"✅ Adicionado {a[i]} à lista C\n")
    print("-" * 40)

print("\nEtapa 2: Verificando elementos de B que não estão em A\n")

for i in range(tamB):
    esta_em_a = False

    for j in range(tamA):
        print(f"Comparando b[{i}] = {b[i]} com a[{j}] = {a[j]}")
        if b[i] == a[j]:
            esta_em_a = True
            print(f"→ {b[i]} existe na lista A\n")

    if esta_em_a == False:
        print(f"{b[i]} NÃO existe na lista A → candidato para a lista C")

        ja_existe = False
        for k in range(tamC):
            if b[i] == c[k]:
                ja_existe = True
                print(f"⚠️ {b[i]} já está na lista C (posição {k}) → não adiciona")

        if ja_existe == False:
            c.append(b[i])
            print(f"✅ Adicionado {b[i]} à lista C\n")
    print("-" * 40)

print("\n✅ Lista final C (elementos exclusivos):", c)
