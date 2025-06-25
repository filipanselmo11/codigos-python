import re

idade = int(input("Informe sua idade: "))

print(idade >= 18)

if(idade >= 18):
    print("Você é de maior.")
elif(idade < 18):
    print("Você é de menor.")