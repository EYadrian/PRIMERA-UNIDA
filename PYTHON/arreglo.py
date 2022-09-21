def llenar(x):
    a = int(input('Escribe un numero'))
    arr.append(a)
    x += 1
    if x <5:
        llenar(x)

def mostrar():
    for x in range(0,len(arr)):
        print(x," ",arr[x],"\n")

def pila():
    aux = len(arr)-1
    for x in range(0,len(arr)):
        arr.pop(x)
        mostrar()
        aux -=1


def liberar():
    valor = int(input("Posicion a eliminar"))
    if valor>=0 and valor<len(arr):
        arr.pop(valor)
    else:
        print("Posicion incorrecta")
    
x = 0
arr = []
res = "si"
llenar(x)
mostrar()
liberar()
pila()
'''while(res=="si"):
    
    
    mostrar()
    res = input('Deseas otra ejecucion si/no')'''
   