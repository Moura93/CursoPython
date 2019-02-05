#Aula 1 Python 
'''
Felipe Moura Wanderley
Data:30/01/2019
'''
'''
var = 'Felipe'
print (type(var))

var = 50
print (type(var))

var= True
print (type(var))


nome = input('Digite seu nome: ')
print(nome)

print (type(nome))

num1 = int (input('Digite o primeiro número: '))
num2 = input('Digite o segundo número: ')

print (num1 + int(num2))


if(1==1): 
	print("Primeiro nivel")
elif(1==1):
	print("Elif")
else:
	print("Nenhum")

'''

'''
FAZER CALCULADORA SIMPLES - CASA
'''


for elemento_lista in[1,2,3,4]:
	print (elemento_lista)

for elemento_lista in range(10):
	print (elemento_lista)

for elemento_lista in range(1,10):
	print (elemento_lista)

for elemento_lista in ['Felipe', 'Olavo', 'Igor', 'Paulo', 'Grego']:
	print(elemento_lista)

for elemento_lista in [[1,2,3,4], [1,2,3,4], [1,2,3,4]]:
	for elemento_lista in elemento_lista:
		print(elemento_lista)

for i, elemento in enumerate([1,2,3,4,5,6]):
	print (i, elemento)

for i, letra in enumerate('Palavra'):
	print(i, letra)