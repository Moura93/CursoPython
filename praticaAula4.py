'''
Faça um programa que contém um Menu.

Menu:
1 - Calculadora de Financiamentos
2 - Editor de Texto
3 - Banco de Dados com Lista
4 - Sair

Autor: Felipe Moura
Data: 06/02/2019
'''
sair = True
textCheck = False

#OPREAÇÕES DA CALCULADORA
def somar(val1, val2):
    return(val1+val2)

def subtrair(val1, val2):
    return(val1-val2)

def multiplicar(val1, val2):
    return(val1*val2)

def dividir(val1, val2):
    return(val1/val2)

#FUNÇÕES DE BANCO DE DADOS
def CriarElementos(tamanhoDaEstrutura, estrutura):  #OK
    if (opc == 1):      #LISTA
        for x in range(0,tamanhoDaEstrutura):
            item = input('Digite o '+str(x)+'º valor da Lista: ')
            estrutura.append(item)
    elif (opc == 2):    #MAP
        for x in range(0,tamanhoDaEstrutura):
            item = input('Digite o '+str(x)+'º valor do Map: ')
            index = input('Digite o '+str(x)+'º index do Map: ')
            estrutura[index] = item
    elif (opc == 3):    #TUPLA/MATRIZ
        listaDaTupla = []
        for x in range(0,tamanhoDaEstrutura):
            item = input('Digite o '+str(x)+'º valor da Tupla/Matrix: ')
            listaDaTupla.append(item)
        estrutura = tuple((listaDaTupla))
    else:               #OPÇÃO INVALIDA
        print('Estrutura não definida!')
    return estrutura
opc = 0

def InserirElementos(InsElem):                      #OK
    while (InsElem):
        item = input('Digite o item a ser inserido na Estrutura: ')
        if (opc == 1):  #INSERIR ITEM NA LISTA
            ondeInserir = input('Onde deseja inserir um item na sua lista?\n[1] - Fim\n[2] - Inicio\n[3] - Trocar por um item especifico\n[4] - Sair')
            if (ondeInserir == 1):  #INSERIR ELEMENTO NO FIM
                estrutura.append(item)
            elif (ondeInserir == 2): #INSERIR ELEMENTO NO INICIO
                estrutura.reverse()
                estrutura.append(item)
            elif (ondeInserir == 3): #TROCAR POR UM ITEM ESPECIFICO
                local = input('Digite o local onde será inserido o item '+str(item)+' : ')
                certeza = input('Tem certeza que deseja trocar o local ['+str(local)+'] de "'+str(estrutura[local])+'" por "'+str(item)+'" ?\nS ou N')
                if(certeza == 'S'):
                    estrutura[local] = item
                    print('Item Trocado!')
                elif(certeza == 'N'):
                    print('Item Mantido!')
                else:
                    print('Opção Invalida!')
            elif (ondeInserir == 4): #SAIR
                pass
            else:                   #OPÇÃO INVALIDA
                print('Opção Invalida!')   
        elif(opc == 2): #INSERIR ITEM NO MAP
            index = input('Digite o index do Map: ')
            ondeInserir = int(input('Onde deseja inserir um item no seu Map?\n[1] - Qualquer lugar\n[2] - Trocar por um item especifico referente ao index\n[3] - Sair\n'))
            if (ondeInserir == 1):  #INSERIR ELEMENTO NO MAP
                estrutura[index] = item
            elif (ondeInserir == 2): #TROCAR POR UM ITEM ESPECIFICO REFERENTE AO INDEX
                index = input('Digite o index onde será inserido o item '+str(item)+' : ')
                certeza = input('Tem certeza que deseja trocar no index ['+str(local)+'] de "'+str(estrutura[local])+'" por "'+str(item)+'" ?\nS ou N')
                if(certeza == 'S'):
                    estrutura[index] = item
                    print('Item Trocado!')
                elif(certeza == 'N'):
                    print('Item Mantido!')
                else:
                    print('Opção Invalida!')
            elif (ondeInserir == 3): #SAIR
                InsElem = False
            else:                   #OPÇÃO INVALIDA
                print('Opção Invalida!')

def RemoverElementos(RemElem):                      #OK
    if (opc == 1):      #REMOVER ITEM DE LISTA
        ondeRemover = input('\nDe onde deseja remover o item da lista?\n[1] - Inicio\n[2] - Fim\n[3] - Local especifico\n')
        if (ondeRemover == 1):      #REMOVER ITEM DO FIM DA LISTA
            estrutura.pop()
        elif (ondeRemover == 2):    #REMOVER ITEM DO INICIO DA LISTA
            estrutura.reverse()
            estrutura.pop()
            estrutura.reverse()
        elif (ondeRemover == 3):    #REMOVER ITEM DE UM LOCAL ESPECIFICO DA LISTA
            localDaLista = input('Digite o número do local que deseja remover o item da lista: ')
            estrutura.pop(localDaLista)
        else:
            print('Opção Invalida!')
    elif (opc == 2):    #REMOVER ITEM DE MAP
        index = input('Digite o index do elemento que deseja apagar: ')
        estrutura.pop(index)
    elif (opc == 3):    #"REMOVER ITEM DE TUPLA"
        print('Opção não exite para Tupla/Matriz!')
        RemElem = False
    else:               #ESTRUTURA NÃO DEFINIDA
        print('Estrutura não Definida!')
        RemElem = False

#PROGRAMA GERAL
while(sair):
    calculadora = False
    menu = int(input('\nMenu:\n[1] - Calculadora de Financiamentos\n[2] - Editor de Texto\n[3] - Banco de Dados\n[4] - Sair\n')) 
#   CALCULADORA - OK
    if(menu == 1):
        calculadora = True
        while(calculadora):
            val1 = float(input('Digite o primeiro número: '))
            val2 = float(input('Digite o segundo número: '))
            calc = int(input('\nCalculadora:\n[1] - Somar\n[2] - Subtrair\n[3] - Dividir\n[4] - Multiplicar\n[5] - Sair\n'))
            if (calc == 1):     #SOMAR
                print(somar(val1, val2))
            elif (calc == 2):   #SUBTRAIR
                print(subtrair(val1, val2))
            elif (calc == 3):   #DIVIDIR
                print(dividir(val1, val2))
            elif (calc == 4):   #MULTIPLICAR
                print(multiplicar(val1, val2))
            elif (calc == 5):   #SAIR
                calculadora = False
            else:               #INVALIDO
                print('Opção invalida!')

#   EDITOR DE TEXTO - OK
    elif(menu == 2):
        edTx = True
        while (edTx):
            editor = int(input('\nEditor de Texto:\n[1] - Inserir texto\n[2] - Colocar tudo maiusculo\n[3] - Colocar tudo minusculo\n[4] - Trocar palavra\n[5] - Contar quantas palavras especifica tem no texto\n[6] - Mostrar texto\n[7] - Sair\n'))
            if (editor == 1):   #INSERIR TEXTO
                textCheck = True
                texto = input("Digite seu texto: \n")
            elif(editor == 2 and textCheck):  #COLOCAR TUDO MAIUSCULO
                print(texto.lower())
            elif(editor == 3 and textCheck):  #COLOCAR TUDO MINUSCULO
                print(texto.upper())
            elif(editor == 4 and textCheck):  #TROCAR PALAVRA
                palavraDoTexto = input('Digite palavra que se encontra no texto: ')
                palavraParaSubstituir = input('Digite a palavra que você quer trocar por '+str(palavraDoTexto)+' : ')
                texto = texto.replace(palavraDoTexto, palavraParaSubstituir)
            elif(editor == 5 and textCheck):  #CONTAR PALAVRAS DO TEXTO
                palavraDoTexto = input('Digite a palavra a ser contada no texto: ')
                quantidade = texto.count(palavraDoTexto)
                print('A palavra "'+palavraDoTexto+'" aparece '+str(quantidade)+' vezes no texto')
            elif(editor == 6 and textCheck):  #MOSTRAR TEXTO
                print(texto)
            elif(editor == 7):  #SAIR
                edTx = False
            else:               #OPÇÃO INVALIDA
                print('Opção Invalida ou Texto não Inserido!')

#   BANCO DE DADOS
    elif(menu == 3):
        bDD = True
        while(bDD == True):
            bancoDeDados = int(input('\nBanco de Dados:\n[1] - Criar/Modificar\n[2] - Inserir elementos\n[3] - Retirar elementos\n[4] - Procurar elementos\n[5] - Mostrar todos os elementos\n[6] - Sair\n'))
            if (bancoDeDados == 1):     #CRIAR/MODIFICAR
                print('OPÇÃO CRIAR/MODIFICAR')
                opc = int(input('\nQual tipo de estrutura deseja criar?\n[1] - Lista\n[2] - Map\n[3] - Tupla/Matriz\n'))
                if (opc == 1):      #LISTA
                    estrutura = []
                    tamanhoDaEstrutura = int(input('Digite a quantidade de elementos da sua Lista: '))
                    estrutura = CriarElementos(tamanhoDaEstrutura, estrutura)
                    print(estrutura)
                elif (opc == 2):    #MAP
                    estrutura = {}
                    tamanhoDaEstrutura = int(input('Digite a quantidade de elementos do seu Map: '))
                    estrutura = CriarElementos(tamanhoDaEstrutura, estrutura)
                    print(estrutura)
                elif (opc == 3):    #TUPLA/MATRIZ
                    estrutura = 0
                    tamanhoDaEstrutura = int(input('Digite a quantidade de elementos da sua Tupla/Matriz: '))
                    estrutura = CriarElementos(tamanhoDaEstrutura, estrutura)
                    print(estrutura)
                else:               #OPÇÃO INVALIDA
                    print('Opção Invalida!')
            elif (bancoDeDados == 2):   #INSERIR ELEMENTOS
                if (opc == 3):
                    print('Esta estrutura não permite esta opção!')
                elif(opc == 1 or opc == 2):
                    InsElem = True
                    InserirElementos(InsElem)
                else:
                    print('Estrutura não criada')
            elif (bancoDeDados == 3):   #RETIRAR ELEMENTOS
                if (opc == 3):
                    print('Esta estrutura não permite esta opção!')
                elif(opc == 1 or opc == 2):
                    RemElem = True
                    RemoverElementos(RemElem)
                else:
                    print('Estrutura não criada')           
            elif (bancoDeDados == 4):   #PROCURAR ELEMENTOS
                if(opc==1 or opc==2 or opc==3):
                    local = input('Digite o index/local do elemento: ')
                    print(estrutura[local])
                else:
                    print('Estrutura não criada!')
            elif (bancoDeDados == 5):   #MOSTRAR TODOS OS ELEMENTOS
                if(opc==1 or opc==2 or opc==3):
                    print(estrutura) 
                else:
                    print('Estrutura não criada!')          
            elif (bancoDeDados == 6):   #SAIR
                bDD = False
            else:
                print('Opção Invalida!')

#   SAIR - OK
    elif(menu == 4):
        sair = False

#   OPÇÃO INVALIDA - OK
    else:
        print('Número invalido!')
