quantidade = int(input("Digite o numero de maçãs: "))

if quantidade < 12:
    valor = quantidade * 1.30
else:
    valor = quantidade * 1.00

print(" O valor da compra é: R$", valor)