from datetime import datetime

horaInicial = input("Digite a hora inicial (hh:mm): ")
horaFinal = input("Digite a hora final (hh:mm): ")

formato = "%H:%M"
inicio = datetime.strptime(horaInicial, formato)
fim = datetime.strptime(horaFinal, formato)

diferenca = fim - inicio
minutos = diferenca.total_seconds() / 60

print(f"Tempo decorrido: {minutos} minutos")

# horas = minutos / 60

# print(f"Duração em horas: {horas} horas")