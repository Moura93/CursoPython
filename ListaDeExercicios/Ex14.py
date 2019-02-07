'''
Faça um Programa que peça as 4 notas bimestrais e mostre a média.
Autor: Felipe Moura
Data: 06/02/2019
'''

# nome = str(input("Digite o nome do Aluno: "))
# nota1 = float(input("1ª nota de " + nome + ": "))
# nota2 = float(input("2ª nota de " + nome + ": "))
# nota3 = float(input("3ª nota de " + nome + ": "))
# nota4 = float(input("4ª nota de " + nome + ": "))

# print('A média de '+nome+' foi: '+str((nota1+nota2+nota3+nota4)/4))


# POR LISTA DINAMICA

aluno = []
nome = str(input('Digite o nome do Aluno: '))
aluno.append(nome)

for x in range(1,5):
    nota = input(str(x)+'ª nota de '+str(aluno[0])+': ')
    aluno.append(nota)
    pass

print('A média de '+nome+' foi: '+str((int(aluno[1])+int(aluno[2])+int(aluno[3])+int(aluno[4]))/4))