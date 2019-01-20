salario = float(input('Digite o salário atual: R$ '))
aumento = int(input('Digite o aumento(%): '))
new_pay = salario + (salario * (aumento / 100))
print(new_pay)
