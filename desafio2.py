'''
AUTOR: Felipe Moura Wanderley
2º desafio: RECEBER O TAMANHO DE UMA LISTA E OS NÚMEROS DELA E DIZER O VALOR DA SOMA DOS VALORES DE METADE DA LISTA
'''


tamlist = int(input('Digite o tamanho da lista: '))

lista = []

for x in range(tamlist):
#	lista[x] = int(input('Digite o número da posição: '))
	valor = int(input('Digite o valor da lista: '))
	lista.append(valor)

'''
lista = [5, 2, 6, 1, 1, 1, 1]

tamlist = len(lista)
'''

k = int(tamlist/2)

valor = 0

for y in range(k, tamlist):
	valor = lista[y] + valor

print(valor)