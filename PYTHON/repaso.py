#hacer un programa que en un arreglo de 10 posiciones, en las posiciones pares se almacenen numeros pares y en las inpares se almacenen numeros inpares

def validar(b,p):
    b2=False

    if (b==False):
        if a[p]==0:
            arreglo(p)

def arreglo(q):
    print('Hola ')
    n = int(input('Escribe un numnero diferente de 0'))
    if (a[q]==0):
        if ((q%2)==0 and (n%2)==0):
            a[q]=n
        if ((q%2)!=0 and (n%2)!=0):
            a[q]=n
        if a[q]==0:

            ban=False
            validar(ban,q)

a =[0,0,0,0,0,0,0,0,0,0]
for x in range (0,9): #recorre todas las posiciones
    arreglo(x)
    print(x,' ',a[x])