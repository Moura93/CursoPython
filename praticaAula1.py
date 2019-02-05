'''
Aula 1 Prática
'''

nome = input('Digite o nome do aluno: ')

nota1 = int(input('Digite a primeira nota do aluno: '))
nota2 = int(input('Digite a segunda nota do aluno: '))

resultado = (nota1 + nota2)/2

if(resultado>=7):
	print('Aluno: ' + nome)
	print('APROVADO com média: ', resultado)
else:
	print('Aluno: ' + nome)
	print('REPROVADO com média: ', resultado)