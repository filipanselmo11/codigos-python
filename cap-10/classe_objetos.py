class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def se_apresentar(self):
        print(f"Nome: {self.nome} - Idade: {self.idade}")


pessoa1 = Pessoa("Ana", 25)
pessoa2 = Pessoa("Maria", 32)
pessoa3 = Pessoa("Jonas", 21)
pessoa4 = Pessoa("Lucio", 30)

pessoa1.se_apresentar()
pessoa2.se_apresentar()
pessoa3.se_apresentar()
pessoa4.se_apresentar()