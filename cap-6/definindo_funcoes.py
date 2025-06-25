
# def saudacao(nome: str) -> None:
#     print("Olá,", nome, "seja bem vindo(a)!!!")

def saudacao(nome: str):
    print("Olá,", nome, "seja bem vindo(a)!!!")

# nome:str = (input("Digite seu nome: "))
nome = str(input("Digite seu nome: "))
print(type(nome))
saudacao(nome)