#Nome: GUILHERME FORTALEZA DE SOUSA
#Matricula: 01877047
#--------------------------------------
#Faça um algoritmo para ler: número da conta do cliente, saldo, débito e crédito. Após, calcular e escrever o
#saldo atual (saldo atual = saldo - débito + crédito). Também testar se saldo atual for maior ou igual a zero
#escrever a mensagem 'Saldo Positivo', senão escrever a mensagem 'Saldo Negativo'.

# FUNÇÃO PARA VERIFICAR SE O SALDO É POSITIVO OU NEGATIVO

def verificar_saldo(saldo_final):

# IF PARA VERIFICAR SE O SALDO FINAL É NEGATIVO OU POSITIVO. SE O SALDO FINAL FOR MENOR QUE ZERO, A MENSAGEM "Saldo negativo." É EXIBIDA. CASO CONTRÁRIO, A MENSAGEM "Saldo positivo." É EXIBIDA.
    if saldo_final < 0:
        print("Saldo negativo.")
    else:
        print("Saldo positivo.")

# O USUARIO DIGITA SEUS DADOS DE SALDO, CREDITO E DEBITO
saldo = float(input("Digite o saldo atual: "))
credito = float(input("Digite o valor do crédito: "))
debito = float(input("Digite o valor do débito: "))

# O SALDO FINAL E CALCULADO SUBTRAINDO O VALOR DO SALDO INICIAL PELO VALOR DO CREDITO E DEBITO
saldo_final = saldo - (credito + debito)

# A FUNÇÃO "verificar_saldo" É CHAMADA PARA VERIFICAR SE O SALDO FINAL É POSITIVO OU NEGATIVO, E O RESULTADO É EXIBIDO AO USUÁRIO. O SALDO FINAL TAMBÉM É EXIBIDO AO USUÁRIO.

verificar_saldo(saldo_final)

print("Saldo final: ", saldo_final)



#ALUNO: GUILHERME FORTALEZA DE SOUSA - MATRICULA: 01877047