salario = int(input('Salário? R$ '))
imposto = input('Imposto em porcentagem(%) (Ex: 27,9): ')

if not imposto:
    imposto = 27.9
else:
    imposto = imposto.replace(',', '.')
    imposto = float(imposto)

result = salario - (salario * (imposto * 0.01))
print('O salário real é de R$ {}'.format(result))