##TIPOS PRIMITIVOS-EXERCICIO 04

a = input('digite algo: ')
print('O tipo primitivo desse valor é ', type(a))
print('Só tem espaços? ', a.isspace())
print('É um numero? ', a.isnumeric())
print('É alfabético? ', a.isalpha())
print('É alfanumérico? ', a.isalnum())
print('Está em Maiúsculas? ', a.isupper())
print('Está capitalizada? ', a.istitle())


a = input('Digite algo: ')
print(f'O tipo primitivo desse valor é {type(a)} \n'
      f'Só tem espaços? {a.isspace()} \n'
      f'É alfabético? {a.isalpha()} \n'
      f'É alfanumérico? {a.isalnum()} \n'
      f'Está em maiúsculas? {a.isupper()} \n'
      f'Está em minúsculas? {a.islower()} \n'
      f'Está capitalizado? {a.istitle()}')

##TESTE OK! =) 25/02/2022

##a.isspace())  ###tem espaços
##a.isnumeric())                   ##numerico
##a.isalpha())                      ##alfabetico
##a.isalnum()                   ##alfanumerico
##a.isupper())                ##maiuscula
##a.istitle())                 ##está capitalizada
##type(a))        ##type saber o tipo ex str etc