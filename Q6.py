#Nome: Gustavo Nascimento da Silva
#Matrícula: 01866201
#--------------------------------------

# Entrada de dados


nome = input("Digite seu nome: ")
altura = float(input("Digite sua altura (ex: 1.75): "))
sexo = input("Digite seu sexo (M/F): ").upper()



# Processamento
if sexo == "M":
    peso_ideal = (72.7 * altura) - 58
elif sexo == "F":
    peso_ideal = (62.1 * altura) - 44.7
else:
    print("Sexo inválido!")
    peso_ideal = None



# Saída
if peso_ideal is not None:
    print(f"{nome}, seu peso ideal é: {peso_ideal:.2f} kg")