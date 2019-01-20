price = float(input('Digite o valor do produto: R$ '))
desc = int(input('Desconto (%): '))
descP = desc / 100
new_price = price - (price * descP)
print('{}% de desconto R$ {:.2f}'.format(desc, new_price))

#discount = (val*5)/100
