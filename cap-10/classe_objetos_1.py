class Robo:
    def __init__(self, nome):
        self.nome = nome

    def dizer_oi(self):
        print("Olá meu nome é:", self.nome)

    def mostrar_menu(self):
        print("Por favor selecione uma das opções disponíveis")
        print("1 - Realizar o cálculo de alguma conta.\t")
        print("2 - Contar uma história.\t")
        print("3 - Calcular o IMC.\t")
        print("4 - Enviar email.\t")
        print("5 - Desligar o robô.\t")
        opcao = int(input("Selecione uma opção: "))

        if opcao == 1:
            print("Você escolheu a opção de realizar o cálculo de alguma conta")
            self.realizar_conta()
            self.mostrar_menu()
        elif opcao == 2:
            print("Você escolheu a opção de contar história. Aqui está...")
            self.contar_historia()
            self.mostrar_menu()
        elif opcao == 3:
            print("Você escolheu a opção de calcular o IMC.")
            self.calcular_imc()
            self.mostrar_menu()
        elif opcao == 4:
            print("Você escolheu a opção de enviar email.")
            self.enviar_email()
            self.mostrar_menu()
        elif opcao == 5:
            print("Até logo!")
            # exit()
        else:
            print("Opção inválida")
            self.mostrar_menu()

    def realizar_conta(self):
        opcao = int(
            input(
                "Informe o tipo de conta que quer resolver: 1-soma, 2-subtracao, 3-multiplicacao: "
            )
        )
        x = int(input("Informe o valor de x: "))
        y = int(input("Informe o valor de y: "))
        if opcao == 1:
            print(
                "Você selecionou a opção de soma. Aguarde que a soma está sendo feita..."
            )
            soma = x + y
            print("O resultado da soma é: ", soma)
        elif opcao == 2:
            print(
                "Você selecionou a opção de subtracao. Aguarde que a subtracao está sendo feita..."
            )
            subtracao = x - y
            print("O resultado da subtracao é: ", subtracao)
        elif opcao == 3:
            print(
                "Você selecionou a opção de multiplicacao. Aguarde que a multiplicacao está sendo feita..."
            )
            multiplicacao = x * y
            print("O resultado da multiplicacao é: ", multiplicacao)

    def contar_historia(self):
        print(
            f"Lorem ipsum dolor sit amet, consectetur adipiscing elit. In faucibus vel arcu et posuere. Curabitur dictum odio nisl, in finibus velit eleifend at. Fusce et tortor congue, sollicitudin felis at, cursus ipsum."
        )

    def calcular_imc(self):
        peso = float(input("Informe o seu peso corporal: "))
        altura = float(input("Informe sua altura: "))
        imc = peso / (altura * altura)
        print(f"O seu imc é: {imc}")

        if imc < 18.5:
            print("Baixo Peso")
        elif imc >= 18.5 and imc < 24.9:
            print("Peso Normal")
        elif imc >= 25 and imc < 29.9:
            print("Sobrepeso")
        elif imc >= 30:
            print("Obesidade")

    def enviar_email(self):
        print(
            "Você selecionou a opção de enviar email. Me informe os dados necessários."
        )
        remetente = str(input("Informe seu email: "))
        destinatario = str(input("Informe o email do destinatario: "))
        mensagem = str(input("Digite sua mensagem: "))

        print("Email enviado com sucesso!!")


robo1 = Robo("Bobby")
robo1.dizer_oi()
robo1.mostrar_menu()
