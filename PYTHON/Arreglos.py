
#arreglos en python

from calendar import c
from curses.ascii import isdigit


def validarNumeros(a):
    c = 0
    x = 0
    for i in a:
        if isdigit(a[x]):
            c+=1
            x += 1
    if c == len(a):
        return True
    else:
        return False

def arreglo(po):
    res = 's'
    while res == 's' or res == 's':
        a = input ('valor')
        if validarNumeros(a):
            ar[po]=int(a)
            po +=1
        else:
            print('Error solo se permiten numeros')
        if po<len(ar):
            res = input('Deseas otro valor s/n \n')

def mostrar():
    for x in ar:
        if( x != 0):
            print(x,' ')
        
ar=[0,0,0,0,0,0,0,0,0,0]
po=0
arreglo()
mostrar()