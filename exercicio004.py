x=input('Digite algo: ')
tipo=type(x)
espaço=x.isspace()
numero=x.isnumeric()
alfabetico=x.isalpha()
alfanumerico=x.isalnum()
maiuscula=x.isupper()
minuscula=x.islower()
capitalizado=x.istitle()

print('O tipo mrimitivo desse valor é {}\n Só tem espaços? {}\n É um número? {}\n É alfabético? {}\n É alfanumérico? {}\n Está em Maiúsculas? {}\n Está em Minusculas? {}\n Está capitalizada? {}'
.format(tipo,espaço,numero,alfabetico,alfanumerico,maiuscula,minuscula,capitalizado))