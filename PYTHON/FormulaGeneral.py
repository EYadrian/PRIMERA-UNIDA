from math import sqrt
a = int(input('Escrbe el valor de a '))
b = int(input('Escrbe el valor de b'))
c = int(input('Escrbe el valor de c'))

e= b**2
n=e-4*a*c
r= sqrt(n)
re=-b+r
re2=-b-r
d=re/2*a
d2=re2/2*a

r1=d
r2=d2
print('x1 es igual a: ',e)
print('x2 es igual a: ',n)