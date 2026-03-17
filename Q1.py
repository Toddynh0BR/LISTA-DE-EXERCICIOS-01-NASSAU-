#Nome: Kauãn Felipe da Silva Melo 
#Matrícula: 01892125
#--------------------------------------
#As maçãs custam R$ 1,30 cada se forem compradas menos de uma dúzia, e R$ 1,00 se forem compradas
#pelo menos 12. Escreva um algoritmo que leia o número de maçãs compradas, calcule e escreva o custo total
#da compra.

quantidade = int(input("Digite o numero de maçãs: "))

if quantidade < 12:
    valor = quantidade * 1.30
else:
    valor = quantidade * 1.00

print("O valor da compra é: R$", valor)