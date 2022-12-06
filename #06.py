n1 = int(input('Digite um valor: '))
n2 = int(input('Digite outro valor: '))
s=n1+n2

print('A soma entre {} e {} vale: {} '.format(n1,n2,s))

n = input('Digite Algo: ')
letra=n.isalpha()
numero=n.isnumeric()
minusculo=n.islower()
maiusculo=n.isupper()

print('{0} é uma letra? {1}{2}{1}{1}{0} é uma número? {1}{3}{1}{1}{0} é minusculo? {1}{4}{1}{1}{0} é maiusculo? {1}{5}'.format(n,'\n',letra,numero,minusculo,maiusculo))