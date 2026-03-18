#Nome: Matheus Augusto Gomes da Silva
#Matrícula: 01894714
#--------------------------------------
#Um posto está vendendo combustíveis com a seguinte tabela de descontos:

#Álcool
#até 20 litros, desconto de 3% por litro
#acima de 20 litros, desconto de 5% por litro
#Gasolina
#até 20 litros, desconto de 4% por litro
#acima de 20 litros, desconto de 6% por litro

#Escreva um algoritmo que leia o número de litros vendidos e o tipo de combustível (codificado da seguinte
#forma: A-álcool, G-gasolina), calcule e imprima o valor a ser pago pelo cliente sabendo-se que o preço do litro
#da gasolina é R$ 3,30 e o preço do litro do álcool é R$ 2,90.

import time
print('Digite o combustível desejado (A: Álcool, G: Gasolina): ')

while True:
    tipo = input('Tipo: ').strip().upper()

    if tipo != 'A' and tipo != 'G':
        print('Digite um tipo válido (A para Álcool ou G para Gasolina).')
        continue

    valor = 2.9 if tipo == 'A' else 3.3
    print('Combustivel escolhido:', 'Álcool' if tipo == 'A' else 'Gasolina')
    time.sleep(1)
    break

print('Digite quantos litros você deseja colocar: ')
while True:
    litrosString = input('Litros: ').replace(',', '.').strip()

    if not litrosString.replace('.', '', 1).isdigit():
       print('Digite um número válido.')
       continue

    litros = float(litrosString)
    break

desconto = 0

if litros <= 20:
  desconto = 0.03 if valor == 2.9 else 0.04
else:
   desconto = 0.05 if valor == 2.9 else 0.06

preco = (litros * valor)
precoComDesconto = preco - (desconto * preco)

#barra de carregamento para deixar mais interessante
total = 25  #total de barrinhas que vão aparecer na barra de carregamento
for i in range(total + 1):
    #cria um loop de um 0 a 26(range nunca vai ate o numero maximo ex: 25 ele vai ate 24)

    barra = "\\" * i
    #multiplica as barras a cada for aumentando-as

    print(f"\r⛽ Abastecendo {barra:<25} {i*4}%", end="")
    #cria um print formated string a cada for com o numero de barras aumentado
    #a cada for, o end="" impede que o codigo quebre a linha mantendo um print acima do outro
    #
    #senao seria algo como:
    #Abastecendo //
    #Abastecendo /////
    #Abastecendo ////////
    #Abastecendo ///////////

    time.sleep(0.2)


print(f'\n\nValor total: R${str(precoComDesconto).replace('.', ',')} Reais com {str(10 * desconto).replace('.', '').replace('0', '')}% de desconto.')