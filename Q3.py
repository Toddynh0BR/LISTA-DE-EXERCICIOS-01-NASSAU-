#Nome: Thiago Henrique Pereira
#Matrícula: 01892849
#--------------------------------------

#A  jornada  de  trabalho  semanal  de  um  funcionário  é  de  40  horas.  O  funcionário  que  trabalhar  mais  de  40 
#horas  receberá  hora  extra,  cujo  cálculo  é  o  valor  da  hora  regular  com  um  acréscimo  de  50%.  Escreva  um 
#algoritmo que leia o número de horas trabalhadas em um mês, o salário por hora e escreva o salário total do 
#funcionário,  que  deverá  ser  acrescido  das  horas  extras,  caso  tenham  sido  trabalhadas  (considere  que  o  mês 
#possua 4 semanas exatas).

#Sem Chat GPT kkk demorei 20 minutos pq esqueci de calcular a diferença kkk

#definindo o salário padrão
salario = 1000
#perguntando ao usuario quantas horas trabalhou
horastrabalhadas = int(input("Quantas horas você trabalhou no mês?: "))
#jornada de trabalho padrão 
jornadadetrabalho = 160
#quanto vai ganhar por o extra
extra_por_hora = salario / jornadadetrabalho * 1.5
#calculo da diferença
diferença = horastrabalhadas - jornadadetrabalho


#definindo o resultado e print final
if horastrabalhadas == 160:
    print(f"Você receberá: R$ {salario}, por suas {horastrabalhadas} horas de trabalho no mês.")
elif horastrabalhadas > 160:
    salario = salario + extra_por_hora * diferença
    print(f"Você receberá: R$ {salario}, por suas {horastrabalhadas} horas de trabalho. no mês.")
