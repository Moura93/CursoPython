'''
AUTOR: Felipe Moura Wanderley
1º desafio: RECEBER 2 NÚMEROS E MOSTRAR OS NUMEROS IMPARES NO INTERVALO DESSES NÚMEROS
'''

#ENTRADA DE DADOS
num1 = int(input('Digite um número: '))
num2 = int(input('Digite outro número: '))

#CÁLCULO
for x in range(num1, num2):
	y = x%2
	if (y!=0):
		print(x)

#SAIDA DE DADOS