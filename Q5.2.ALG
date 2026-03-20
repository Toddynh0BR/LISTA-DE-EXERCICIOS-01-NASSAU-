//Nome: Áquila Pedro Joaquim Oliveira da Silva
//Matrícula: 01890876
//--------------------------------------
//Faça um algoritmo para ler: número da conta do cliente, saldo, débito e crédito. Após, calcular e escrever o
//saldo atual (saldo atual = saldo - débito + crédito). Também testar se saldo atual for maior ou igual a zero
//escrever a mensagem 'Saldo Positivo', senão escrever a mensagem 'Saldo Negativo'.

ALGORITMO "calculadora de saldo"
VAR
numero_da_conta : inteiro
saldo, saldo_final, debito, credito : real

INICIO
escreval("Digite o numero da sua conta")
leia(numero_da_conta)
escreval("Digite seu saldo")
leia(saldo)
escreval("valor gasto no debito")
leia(debito)
escreval("valor gasto no credito")
leia(credito)

saldo_final := saldo - (credito + debito)

escreval("seu numero da conta é: ",numero_da_conta)
escreval("seu saldo final é: ",saldo_final)
se(saldo_final >= 0) entao
escreval("saldo positivo")
senao
escreval("saldo negativo")
fimse
FIMALGORITMO