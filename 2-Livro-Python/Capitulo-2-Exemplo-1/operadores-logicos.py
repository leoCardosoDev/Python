imposto = float(input('Imposto % '))

if imposto <= 10.:
    print('Muito Baixo')
elif imposto > 10. and imposto <= 20.9:
    print('Baixo')
elif imposto > 20.9 and imposto <= 27.5:
    print('Médio')
else:
    print('Alto')
