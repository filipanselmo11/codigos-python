L = ["a"]
L.append("b")
# L.append("h")
print(L)

L.extend(["c"]) # Quando a lista tem apenas um elemento, funciona como append
# L.extend("c")
print(L)

L.append(["d", "e"]) #append sempre adiciona um elemento, mesmo que este seja uma lista
print(L)

L.extend(["f", "g", "h"]) # Adiciona cada elemento a L
print(L)