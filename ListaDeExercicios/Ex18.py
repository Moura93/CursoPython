'''
Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. 
Calcule e mostre o total do seu salário no referido mês.
Autor: Felipe Moura
Data: 06/02/2019
'''
SalarioHora = float(input('Quanto você ganha por hora? '))
HorasPorDia = float(input('Quantas horas você trabalha por dia? '))
salario = 4*5*HorasPorDia*SalarioHora
print('Seu salario mensal é: R$'+str(salario))