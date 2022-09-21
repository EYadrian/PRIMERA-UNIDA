def numero():
    n = int(input('Escribe un numero entre 5 y 20: '))
    if (n >=5 or n<=20):
        print('los numero intermedios son:',len(n%2))
    else:
        print('El numero no esta dentro de los parametros establecidos')
    
numero()
