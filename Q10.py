#Nome: Áquila Pedro Joaquim Oliveira da Silva
#Matrícula: 01890876
#--------------------------------------
  
#loop feito com a ajuda de matheus 
while True:
  codigo  = int(input("digite o codigo: "))
  if codigo != 12345:
     print("usuario inválido")
  else:
   break

while True:
    senha = int(input("digite a senha: "))
    if senha != 9999:
      print("senha incorreta")
    else:
     break

print("Acesso concedido")