#====================================================================================================================
# Desafio 005 - Faça um programa que leia um numero inteiro e mostre na tela o seu sucessor e seu antecessor

n=int(input('Digite um número inteiro: '))
print('='*100)
print('O número escolhido foi {} \nseu sucessor é {} \nseu antecessor é {}'.format(n,(n+1),(n-1)))
print('='*100)

#====================================================================================================================
# Desafio 006 - Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada

n=int(input('Digite um número: '))
dobro=n*2
triplo=n*3
raiz=n**(1/2)
print('='*100)

print('O dobro do número é {} \nO Triplo do número é {} \nA raiz quadrada do número é {}'.format(dobro,triplo,raiz))
print('='*100)

#====================================================================================================================
# Desafio 007 - Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a sua média

n1=int(input('Digite sua primeira nota: '))
n2=int(input('Digite sua segunda nota: '))

media=(n1+n2)/2
print('='*100)
print('A sua média é {}'.format(media))
print('='*100)

#====================================================================================================================
# Desafio 008 - Escreva um programa que leia um valor em metros e o exiba convetido em centimentos e milimetros

n=float(input('Digite um número em metros: '))
cm=n*10
mm=n*100

print('='*100)
print('Em Centimetros fica {} \n Em Milimetros fica {}'.format(cm,mm))
print('='*100)

# Desafio 009 - Faça um programa que leia um número inteiro qualquer e mostre na tela a sua tabuada

n=int(input('Digite o número da tabuada: '))
x1=n*1
x2=n*2
x3=n*3
x4=n*4
x5=n*5
x6=n*6
x7=n*7
x8=n*8
x9=n*9
x10=n*10

print('='*100)
print('{0}x1 = {1}\n{0}x2 = {2}\n{0}x3 = {3}\n{0}x4 = {4}\n{0}x5 = {5}\n{0}x6 = {6}\n{0}x7 = {7}\n{0}x8 = {8}\n{0}x9 = {9}\n{0}x10 = {10}'.format(n,x1,x2,x3,x4,x5,x6,x7,x8,x9,x10))
print('='*100)

# Desafio 010 - Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dolares ela pode comprar 
# (Considere US$1,00 = R$3,27)

n=float(input('Digite quando você tem em dinheiro: '))

dolar=3.27

conv=n/dolar

print('O valor que você possui corresponde {:.2f} Dolares'.format(conv))
print('='*100)

# Desafio 011 - Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de 
# tinta necessaria para pinta-la, sabendo que a cada litro de tinta, pinta uma área de 2m².

n1=float(input('Informe qual a altura da parede: '))
n2=float(input('Informe quanto de largura tem a parede: '))

m=n1*n2

tinta=m/2

print('='*100)
print('A quantidade de litros de tinta necessario é de {} litro(s)'.format(tinta))
print('='*100)

# Desafio 012 - Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto

valor=float(input('Informe o  preço do produto: '))

nvalor=valor-(valor*0.05)

print('='*100)
print('O novo preço do produto será {:.2f}'.format(nvalor))
print('='*100)

# Desafio 013 - Faça um algoritmo que leia o salário de um funcionario e mostre seu novo salario, com 15% de aumento

salario=float(input('Digite o salario: '))
nsalario=salario+(salario*0.15)

print('='*100)
print('O novo salario do funcionario será R${:.2f}'.format(nsalario))
print('='*100)
