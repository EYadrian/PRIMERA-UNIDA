from re import A


while (True):
    a = int(input('Escribe un numero '))
    b = int(input('Escribe otro numero '))
    c = int(input('Escribe otro numero '))
    if a**2 + b**2 == c**2:
        print('Es correcto y su valor es: ',c**2)
    else:
        print('No se cumple ')

