salario_fixo = float(input("Digite o salário fixo: "))
vendas = float(input("Digite o valor das vendas: "))

if vendas <= 1500:
    comissao = vendas * 0.03

else:
    comissao = (1500 * 0.03) + ((vendas - 1500) * 0.05)

    salario_total = salario_fixo + comissao

print("Seu salário total é de: ",salario_total)