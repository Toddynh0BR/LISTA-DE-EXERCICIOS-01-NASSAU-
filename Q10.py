#Nome: Áquila Pedro Joaquim Oliveira da Silva
#Matrícula: 01890876
#--------------------------------------
  
#Faça um algoritmo para ler um número que é um código de usuário. Caso este código seja diferente de um 
#código  armazenado  internamente  no  algoritmo  (igual  a  1234)  deve  ser  apresentada  a  mensagem  ‘Usuário 
#inválido!’. Caso o Código seja correto, deve ser lido outro valor que é a senha. Se esta senha estiver incorreta 
#(a  certa  é  9999)  deve  ser  mostrada  a  mensagem  ‘senha  incorreta’.  Caso  a  senha  esteja  correta,  deve  ser 
#mostrada a mensagem ‘Acesso permitido’. 

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