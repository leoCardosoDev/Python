salario = int(input('Salário R$: '))
imposto = 27.

while imposto > 0.:
    imposto = input('Imposto (%) ou (0) para sair: ')
    if not imposto:
        imposto = 27.
    else:
        imposto = imposto.replace(',', '.')
        imposto = float(imposto)
        result = salario - (salario * (imposto * 0.01))
        print('O valor real é R$ {} '.format(result))
