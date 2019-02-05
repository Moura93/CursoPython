#tamanho da lista
tman = 30
#criação da lista
lista = list(range(tman))
print(lista)

for x in range(tman):
    #par ou impar?
    res = lista[x]%2
    if (res == 0):
        print(lista[x])
    else:
        y = lista[x]*lista[x]
        print(y)