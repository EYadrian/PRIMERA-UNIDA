#hacer un programa que leea nombre, edad y el sexo de 10 personas
from curses.ascii import isdigit


def mostrar(n,e,s):
    if e>=18:
        if s=='M' or s =='m':
            print('Hombre')
    elif e<18:
        if s=='M' or s=='m':
            print('nino')

def validarletras(a):
    x=0
    for i in a:
        if isdigit(i):
            print('Es una letra')
        else:
            print('No es caracter')
