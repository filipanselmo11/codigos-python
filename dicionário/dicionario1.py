outroDicionario = dict(name="Fílip", age=28, country="Brasil")
print(outroDicionario)

idade_clientes = {"Fílip": 28, "Maria": 34, "João": 23}

print(idade_clientes)

jogos = {
    "Fílip": [
        "The Last of Us",
        "God of War",
        "Uncharted",
        "Guitar Hero 3",
        "Tekken",
        "Street Fighter",
    ],
    "Maria": ["The Sims", "SimCity", "Civilization"],
    "João": ["FIFA", "PES", "Football Manager"],
}

print(jogos["Fílip"])

dadosPessoas = {
    "Fílip": {
        "endereco": "Rua Brigadeiro Eduardo Gomes",
        "numero": "100",
        "CEP": "2526262627",
        "bairro": "Boa Esperanca",
    },
    "Julia": {
        "endereco": "Travessa Servidão",
        "numero": "188",
        "cep": "23017405",
        "bairro": "Campo grande",
    },
}

print(dadosPessoas["Fílip"])

dicionario_python = {"chave": 1, "chave2": 2}

print(dicionario_python)

emails_gerentes = {
    "Iguatemi": "iguatemi@gmail.com",
    "Plaza": "plaza@gmail.com",
    "Barra": "barra@gmail.com,"
}

print(emails_gerentes)

distroLinux = {
    1: "Ubuntu",
    2: "Linux Mint",
    3: "Debian",
    4: "Manjaro",
    5: "Deepin",
    6: "SteamOs",
    7: "Arch Linux",
}

#Acessando e modificando valores
print(distroLinux)

steamOs = distroLinux[6]

print(steamOs)

distroLinux[5] = "Xero Linux"

print(distroLinux)

distro = distroLinux.get(8, 'Chave não encontrada')
print(distro)

#Adicionando e removendo itens do dicionário Python

snkFighters = {
    1: "Athena",
    2: "Mai",
    3: "Terry",
    4: "Andy",
    5: "Rugal",
    6: "Kyo"
}

snkFighters[7] = "Hotaru"

print(snkFighters)

snkFighters.pop(7)
print(snkFighters)

#Percorrendo items em um dicionário

for chave in snkFighters:
    print(chave)


print(snkFighters.keys())

for key in snkFighters:
    print(snkFighters[key])


print(snkFighters.values())

#Verificando existência de chaves e valores no dicionário

frutas = {
    "maca": "Maçã",
    "banana": "Banana",
    "laranja": "Laranja",
    "abacaxi": "Abacaxi",
    "pera": "Pêra",
}

# if "maca" in frutas:
#     print(True)
# else:
#     print(False)

if "Abacaxi" in frutas.values():
    print("A fruta existe no dicionario")
else:
    print("A fruta nao existe no dicionario")


if frutas["abacaxi"] in frutas.values():
    print("A fruta existe no dicionario")
else:
    print("A fruta nao existe no dicionario")

