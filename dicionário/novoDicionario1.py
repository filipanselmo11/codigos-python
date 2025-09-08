
dicionario_1 = {
    'primeiro': 1,
    'segundo': 2,
    'terceiro': 3
}


print(dicionario_1)


dicionario_2 = dict(primeiro=1, segundo=2, terceiro=3)

print(dicionario_2)

dicionario_3 = dict(a="Arroz", b="Batata", c="Carne")

print(dicionario_3)

pessoa = {
    'nome': 'Fílip',
    'idade': 28,
    'cidade': 'São Gabriel da Cachoeira',
    'email': 'filip.silva@ifam.edu.br'
}

print(pessoa.get('idade'))

print(pessoa['idade'])

print(pessoa.get('celular'))

computador = {
    'marca': 'Dell',
    'modelo': 'Inspiron',
    'processador': 'Intel i7',
    'memoria': '16GB',
    'armazenamento': '512GB SSD',
    'sistema_operacional': 'Windows 10',
    'placa_de_video': 'NVIDIA GTX 1650'
}

print(computador.keys())

for chave in computador.keys():
    print(chave)


print(computador.values())

for valor in computador.values():
    print(valor)
