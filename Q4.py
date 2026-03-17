#Nome: Kauãn Felipe da Silva Melo 
#Matrícula: 01892125
#--------------------------------------
#Escreva um algoritmo que leia o salário fixo e o valor das vendas efetuadas pelo vendedor de uma empresa.
#Sabendo-se que ele recebe uma comissão de 3% sobre o total das vendas até R$ 1.500,00 mais 5% sobre o que
#ultrapassar este valor, calcular e escrever o seu salário total.

salario_fixo = float(input("Digite o salário fixo: "))
vendas = float(input("Digite o valor das vendas: "))

if vendas <= 1500:
    comissao = vendas * 0.03

else:
    comissao = (1500 * 0.03) + ((vendas - 1500) * 0.05)

    salario_total = salario_fixo + comissao

print("Seu salário total é de: ",salario_total)