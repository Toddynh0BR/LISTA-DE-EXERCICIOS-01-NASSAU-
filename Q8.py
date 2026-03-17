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

while True:
    print('Digite o combustível desejado(A: Álcool, B: Gasolina):')
    tipo = input('Tipo: ').strip().upper()

    if tipo != 'A' and tipo != 'G':
        print('Digite um tipo válido(A ou G).')
        continue

    print('Combustivel escolhido:', 'Álcool' if tipo == 'A' else 'Gasolna')
    break