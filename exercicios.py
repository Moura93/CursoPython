'''
#Desafio 1
#Solucao 1
var1 = int(input('Digite o var 1\n'))
var2 = int(input('Digite o var 2\n'))

impares = []
if(var1 < var2):
	for elemento in range(var1, var2+1):
		if (elemento%2 != 0):
			impares.append(elemento)
else:
	print ('valores invalidos')


print (impares)
'''

'''
#Desafio 1
#Solucao 2

var1 = int(input('Digite o var 1\n'))
var2 = int(input('Digite o var 2\n'))

for elemento in range(var1, var2+1):
	if (elemento%2 != 0):
		print(elemento)

'''

'''
#extra

lista = []

tam = int(input('Qual o tamanho da lista:\n'))

for elemento in range(tam):
	valor = input('Digite o valor' + str(elemento))
	lista.append(valor)

print (lista)
'''

'''
desafio 2
lista = [4,6,89,34,1,70]

metade = int(len(lista)/2)

somatorio = 0
for index in range(metade, len(lista)):
	somatorio = somatorio  + lista[index]
	print (lista[index])
print (somatorio)
'''