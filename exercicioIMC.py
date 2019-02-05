usuarios = []

cond = True

#while do menu em loop
while(cond):
	#entrada do menu
	menu = int(input('Menu\n[1] - Calcular IMC\n[2] - Mostrar Resultado\n[3] - Sair\n'))
	if(menu == 1):
		nome = input('Digite o nome: ')
		altura = float(input('Digite a altura: '))
		peso = float(input('Digite o peso: '))
		sexo = input('Digite o sexo: ')
		#criando um usuario como uma lista de dados
		usuario = [nome, altura, peso, sexo]
		#adicionando o usuario na lista global
		usuarios.append(usuario)
	elif(menu == 2):
		#percorrer os usuarios e calcular o imc
		for nome, altura, peso, sexo in (usuarios):
			imc = (peso / (altura*altura))
			if(sexo.lower() == 'F'.lower()):
				if(imc < 19.1):
					print (nome, 'esta abaixo do peso',imc)
				elif(imc >= 19.1 and imc < 25.8):
					print (nome, 'esta no peso normal',imc)
				elif(imc >= 25.8 and imc < 27.3):
					print (nome, 'marginalmente acima do peso',imc)
				elif(imc >= 27.3 and imc < 32.3):
					print (nome, 'acima do peso ideal',imc)
				elif(imc>=32.3):
					print (nome, 'obeso',imc)
				else:
					print ('Valor invalido!')
			elif(sexo.lower() == 'M'.lower()):
				if(imc < 20.7):
					print (nome, 'esta abaixo do peso',imc)
				elif(imc >= 20.7 and imc < 26.4):
					print (nome, 'esta no peso normal',imc)
				elif(imc >= 26.4 and imc < 27.8):
					print (nome, 'marginalmente acima do peso',imc)
				elif(imc >= 27.8 and imc < 31.1):
					print (nome, 'acima do peso ideal',imc)
				elif(imc >= 31.1):
					print (nome, 'obeso',imc)
				else:
					print ('Valor invalido!')
			else:
				print('O sexo digitado eh invalido!')
	elif(menu == 3):
		cond = False
		print('Fim do Programa')



