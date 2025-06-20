salario = float(input('Qual o salário do funcionário? '))

if salario > 1250.0:
    salarioAumento = salario * 1.1
else:
    salarioAumento = salario * 1.15

print('O funcionário que recebe R${:.2f}, com um aumento receberá R${:.2f}'.format(salario, salarioAumento))