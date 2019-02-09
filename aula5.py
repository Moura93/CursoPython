import bibliAula5 as b

frase = input('Digite a frase: ')
fraseCriptografada = b.crip(frase)
print(fraseCriptografada)

print('-------------------------')

fraseDescriptografada = b.decrip(fraseCriptografada)
print(fraseDescriptografada)