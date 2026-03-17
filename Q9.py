#Nome: Matheus Augusto Gomes da Silva
#Matrícula: 01894714
#--------------------------------------
#Uma fruteira está vendendo frutas com a seguinte tabela de preços:

#___________|   Até 5 Kg    | Acima de 5 Kg |
#Morango    | R$2,50 por Kg | R$2,20 por Kg |
#Maçã       | R$1,80 por Kg | R$1,50 por Kg |

#Se o cliente comprar mais de 8 Kg em frutas ou o valor total da compra ultrapassar R$ 25,00, receberá ainda
#um desconto de 10% sobre este total. Escreva um algoritmo para ler a quantidade (em Kg) de morangos e a
#quantidade (em Kg) de maças adquiridas e escreva o valor a ser pago pelo cliente.

import time

#Morangos
while True: 
    morangosString = input("🍓 Digite a quantidade em kilos de morango: ").replace(',', '.').strip()#transforma virgulas em pontos e tira espaços
 
#Checar se o usuário passou um numero
    if not morangosString.replace('.', '', 1).isdigit():#tira o primeiro ponto encontrado na string e checa se há somente digitos, se usuario digitar 1.2.3, retorna erro
        print("Erro: Digite apenas números.")
        continue
    
#Calcular o valor de acordo com os kilos e formata para ter no máximo duas casas decimais após o ponto evitando valores como 1.003
    morangosValor = round(float(morangosString) * 2.5 if float(morangosString) < 6 else float(morangosString) * 2.2, 2)
    break

#Maças
while True: 
    macasString = input("🍎 Agora digite a quantidade em kilos de maças: ").replace(',', '.').strip()

    if not macasString.replace('.', '', 1).isdigit():
        print("Erro: Digite apenas números.")
        continue 
    
    macasValor = round(float(macasString) * 1.8 if float(macasString) < 6 else float(macasString) * 1.5, 2)
    break


#checar preço final
precoFinal = macasValor + morangosValor 
if precoFinal > 25 or float(morangosString) + float(macasString) > 8:
    precoFinal = precoFinal * 0.9 
print('⏱️ Calculando tudo...')

time.sleep(2)
#cria uma formated string para cada print, formatando os valores trnaformando . em , e colocando sempre duas casas decimais após a virgula
print("🍓", morangosString.replace('.', ','), f"kg de morangos dá: R$ {morangosValor:.2f} Reais".replace('.', ','))
time.sleep(1)
print("🍎", macasString.replace('.', ','),f"kg de maças dá: R$ {macasValor:.2f} Reais".replace('.', ','))
time.sleep(1)
print(f"💵 Dando um total de: R$ {precoFinal:.2f} Reais".replace('.', ','))

