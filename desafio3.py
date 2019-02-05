'''
AUTOR: Felipe Moura Wanderley
3º desafio: RECEBER PESO, ALTURA E SEXO DE 3 PESSOAS CALCULAR O IMC E APRESENTAR NA TELA OS RESULTADOS

IMC 			CLASSIFICAÇÃO
<18,5			Magreza
18,5~24,9		Saudável
25,0~29,9		Sobrepeso
30,0~34,9		Obesidade grau 1
35,0~39,9		Obesidade grau 2
>40				Obesidade grau 3
'''

usuario =[]

for x in range(2):
	nome = str(input('Digite o nome da pessoa ' + str(x) + ': '))
	peso = input('Digite o peso da pessoa: ')
	altura = input('Digite a altura da pessoa: ')
	sexo = str(input('Digite o sexo da pessoa: '))
	imc = float(peso/(altura*altura))
	pessoa = [nome, peso, altura, sexo, imc]
	usuario.append(pessoa)

print()


	

