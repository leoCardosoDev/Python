# 1 => ()
# 2 => **
# 3 => * / // %
# 4 => + -



n1 = int(input('Um valor: '))
n2 = int(input('Outro Valor: '))

s = n1 + n2
m = n1 * n2
d = n1 / n2
sb = n1 - n2
rd = n1 % n2
di = n1 // n2
ex = n1 ** n2


print('A Soma(+) vale: {}'.format(s))
print('A Multiplicação(*) vale: {}'.format(m))
print('A Divisão(/) vale: {:.3f}'.format(d))
print('A Subtração(-) vale: {}'.format(sb))
print('O Resto da divisão(%) vale: {}'.format(rd))
print('A Divisão Inteira(//) vale: {}'.format(di))
print('A Potência(**) de {} elevado a {} vale: {}'.format(n1,n2,ex))
