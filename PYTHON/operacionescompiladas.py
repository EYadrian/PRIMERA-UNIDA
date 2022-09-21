from curses.ascii import isdigit
from msilib import PID_LASTAUTHOR


def validarnumero(op):
    con=0
    for x in op:
        if isdigit (x):
            con += 1
    if con==len(op):
        return True
    else:
        return False
def crearpila():
    print('La pila fue creada')
    
    return pila

def ingresar(pila):
    valor = input('Escribe un valor a la pila')
    if validarnumero(valor):
        pila.append(valor)
    else:
        print('Error de datos')


def menu():
    print('1.- Crear Pila')
    print('2.- Ingresar elementos de la pila')
    print('3.- Eliminar elementos de la pila')
    print('4.- Vaciar Pila')
    print('5.-Mostrar pila')
    print('6.- Salir')
    op = input('Elige una opcion/n')
    if (validarnumero(op)):
        o= int(op)
        if o == 1:
            p = crearpila()
        if o == 2:
            ingresar(p)
        if o == 3:
            eliminar()
        if o == 4:
            vaciarPila()
    else:
        print('Error de valor vuelve a ingresarlo')
        menu()
pila=[]
op = '1'
while(op!='6'):    
    op=menu()
