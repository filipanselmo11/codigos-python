
peso = float(input("Informe seu peso (kg): "))
altura = float(input("Informe sua altura (m): "))

IMC = peso / (altura * altura)

if IMC < 18.5:
    print("Abaixo do peso")
elif IMC >= 18.5 and IMC <= 24.9:
    print("Peso ideal")
elif IMC >= 25.0:
    print("Acima do peso")