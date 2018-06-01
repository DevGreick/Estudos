# Faça um algoritmo que leia o preço de um produto e mostre seu novo preço,com 5% de desconto

produto =float(input('digite o valor do produto'))
porcentagem = produto * 5 / 100
porcentagemtotal = produto - porcentagem
print(' o valor do produto descontato e {}'.format(porcentagemtotal))
