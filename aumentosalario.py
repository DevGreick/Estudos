# faça um algoritmo que leia o salario de um funcionario e mostre seu novo salario, com 15% de aumento
salario = float(input('digite o valor do salario do funcionario'))
porcentagem = salario * 15 / 100
valoraumentado = salario + porcentagem
print('o valor aumentado do funcionario é {}'.format(valoraumentado))
