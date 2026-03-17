#Nome: Guilherme Fortaleza de Souza
#Matricula: 01877047
#--------------------------------------
#Escreva um algoritmo que leia o salário fixo e o valor das vendas efetuadas pelo vendedor de uma empresa.
#Sabendo-se que ele recebe uma comissão de 3% sobre o total das vendas até R$ 1.500,00 mais 5% sobre o que
#ultrapassar este valor, calcular e escrever o seu salário total.

# FUNÇÃO PARA CALCULAR O SALÁRIO TOTAL DE UM VENDEDOR, CONSIDERANDO O SALÁRIO FIXO E A COMISSÃO SOBRE AS VENDAS.

def verificar_salario(salario, comissao):
    salario_total = salario + comissao
    
# SALÁRIO TOTAL É A SOMA DO SALÁRIO FIXO COM A COMISSÃO CALCULADA SOBRE AS VENDAS. O RESULTADO É RETORNADO PELA FUNÇÃO PARA SER EXIBIDO AO USUÁRIO.   
    
    return salario_total

# O USUÁRIO É SOLICITADO A DIGITAR O VALOR DO SALÁRIO FIXO E O VALOR TOTAL DAS VENDAS. 

salario = float(input("Digite o valor do salário: "))
vendas = float(input("Digite o valor total das vendas: "))

# CALCULO DA COMISSÃO SOBRE AS VENDAS, CONSIDERANDO QUE A COMISSÃO É DE 3% PARA VENDAS ATÉ R$1500,00 E 5% PARA O EXCEDENTE. O RESULTADO DO CÁLCULO DA COMISSÃO É ARMAZENADO NA VARIÁVEL "comissao".

if vendas <= 1500:
    comissao = vendas * 0.03
else:    
    comissao = ((vendas - 1500) * 0.05) + (1500 * 0.03)

# FUNÇÃO PARA CALCULAR O SALÁRIO TOTAL DE UM VENDEDOR, CONSIDERANDO O SALÁRIO FIXO E A COMISSÃO SOBRE AS VENDAS.
salario_total = verificar_salario(salario, comissao)

# RESULTADO DO PROCESSO DO CÁLCULO DO SALARIO TOTAL
print("Salário total: ", salario_total)


