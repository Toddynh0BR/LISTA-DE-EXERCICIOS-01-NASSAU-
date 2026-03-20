#Nome: Gustavo Nascimento da Silva
#Matrícula: 01866201
#--------------------------------------

#Faça  um  algoritmo  para  ler:  a  descrição  do  produto  (nome),  a  quantidade  adquirida  e  o  preço  unitário. 
#Calcular e escrever o total (total = quantidade adquirida * preço unitário), o desconto e o total a pagar (total a 
#pagar = total - desconto), sabendo-se que: 
 
#- Se quantidade <= 5 o desconto será de 2% 
#- Se quantidade > 5 e quantidade <=10 o desconto será de 3% 
#- Se quantidade > 10 o desconto será de 5%

# Entrada de dados
produto = input("Digite o nome do produto: ")
quantidade = int(input("Digite a quantidade: "))
preco = float(input("Digite o preço unitário: "))

# Cálculo do total
total = quantidade * preco

# Cálculo do desconto
if quantidade <= 5:
    desconto = total * 0.02
elif quantidade <= 10:
    desconto = total * 0.03
else:
    desconto = total * 0.05

# Total a pagar
total_pagar = total - desconto

# Saída
print("\n--- RESULTADO ---")
print(f"Produto: {produto}")
print(f"Total: R$ {total:.2f}")
print(f"Desconto: R$ {desconto:.2f}")
print(f"Total a pagar: R$ {total_pagar:.2f}")