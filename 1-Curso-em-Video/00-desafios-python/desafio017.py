from math import sqrt
b = int(input('Digite o valor do cateto Oposto: '))
c = int(input('Digite o valor do cateto Adjacente: '))
co = pow(b,2)
ca = pow(c,2)
h = co + ca
a =  sqrt(h)
print(h)

print('A soma dos catetos: cateto oposto {}² + cateto adjacente {}² é igual ao valor da Hipotenusa {} que é {:.0f}² '.format(b, c, h, a))
