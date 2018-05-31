#Digitar algo e que apareca o formato e seus atributos completos
algo = input('digite algo para comparar')
print(type('o valor e {}'.format(algo)))
print('e alfanumerico',algo.isalnum())
print('e decimal',algo.isdecimal())
print('e minusculas',algo.islower())
print('e maiusculas',algo.isupper())
