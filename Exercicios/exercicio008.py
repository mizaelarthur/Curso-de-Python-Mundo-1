# Faça um programa que leia a distancia em metros e exiba em:
# Centímetros e Milímetros

n=float(input('Digite a distancia em metros: '))
print('A distancia em centímetros e milímetros é, especitivamente: \n {:.1f} e {:.1f}'.format(n*100,n*1000))

