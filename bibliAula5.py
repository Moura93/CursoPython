dic = {'a':'1', 'b':'2', 'c':'3', 'd':'4', 'e':'5', 'f':'6', 'g':'7', 'h':'8', 'i':'9', 'j':'/', 'k':'*', 'l':'-', 'm':'+', 'n':'.', 'o':'!', 'p':'@', 'q':'#', 'r':'$', 's':'%', 't':'¨', 'u':'&', 'v':'*', 'x':'(', 'y':')', 'w':'~', 'z':'?'}

def crip(frase):
    fraseCriptografada = ''
    for letra in list(frase):
        if letra in dic:
            fraseCriptografada = fraseCriptografada + dic[letra] 
    return fraseCriptografada

def decrip(fraseCriptografada):
    fraseDecriptografada = ''
    key = list(dic.keys())
    val = list(dic.values())
    print(key)
    print(val)
    for index in list(fraseCriptografada):
        for index in key:
            fraseDecriptografada = fraseDecriptografada + val[index]
    print(fraseDecriptografada)
