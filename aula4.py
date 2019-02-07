'''
AULA DE LISTA, FILA, PILHA, DICIONARIO(MAPS), TUPLA
'''
#LISTA
lista = []

lista.append('Primeiro')
lista.append('Segundo')
lista.append('Terceiro')

#insere um elemento e empurra os outros para frente
lista.insert(1, 'Este Elemento')
print(lista)

#remove elemento pelo seu nome
lista.remove('Primeiro')
print(lista)

#deleta elemento pelo index
del (lista[0])
print(lista)

#pega o index do elemento
index = lista.index('Segundo')
print(index)

#inverter lista
lista2 = []
lista2.append('João')
lista2.append('Felipe')
lista2.append('Maria')
print(lista2)
lista2.reverse
print(lista2)

#ordenar lista
lista2.sort
print(lista2)


#FILA
#retirar elemento
fila = ['Primeiro', 'Segundo', 'Terceiro']
elemento = fila.pop(0)
print('Saiu o elemento ', elemento)

#DICIONARIO
dic = {}
dic = {'Felipe':10, 'Paulo':11, 'Igor':12}
print(dic)

for chave in dic:
    print('A chave é: '+str(chave))
    print('A referencia é: '+str(dic[chave]))


#TUPLA
tupla = ()

#-------------------------------------------------------------------

#FUNÇÃO

def somar():
    print(3+4)
    return (3 + 6)

print(somar())

#pode-se colocar como default subtrair(a = 10, b = 10)
def subtrair(a, b):
    return(a - b)

print(subtrair(4, 5))

