# pintura de um parede sabendo que dois metros quadrados e um litro de tinta
largura = float(input('digite a largura aqui'))
altura = float (input ('digite a altura aqui'))
area = largura * altura
tintanecessaria = area ** 2
print('vc precisa de {} litros de tinta para pintar'.format(tintanecessaria))
