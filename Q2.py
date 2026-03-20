#Nome: Thiago Thiago Henrique Pereira
#Matrícula: 01892849
#--------------------------------------

#Escreva  um  algoritmo  que  leia  o  ano  atual  e  o  ano  de  nascimento  de  uma  pessoa.  Escreva  na  tela  uma 
#mensagem que diga se ela poderá ou não votar este ano (não é necessário considerar o mês em que a pessoa 
#nasceu).

#Definindo o ano atual
ano = 2026

#Pedindo uma entrada para o usuário digitar seu nascimento 
idade = int(input("Digite Sua Data De Nascimento: "))

#definindo oque é a diferença
diferença = ano - idade

#declarando que se idade for menor que 16 não votará
if diferença < 16:
    print("Você não poderá votar esse ano!")
else:
    print("Você votará esse ano!")