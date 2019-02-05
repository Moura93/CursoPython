'''num = 0

while (num < 20):
    print('num', num)
    num += 1
    num = num + 1


    Desafio: ficar no laço do while até o usuario digitar parar
'''
resposta = "não"
cond = True
while(cond):
    resposta = input('Deseja para o programa? ')
    if(resposta == "sim"):
        cond = False
        print("O PROGRAMA PAROU")
    elif(resposta == "s"):
        cond = False
        print("O PROGRAMA PAROU")
    else:
        print("O programa continua...")