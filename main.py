# -*- coding: utf-8 -*-
#Solución
import math
a= int(input("Hola! Con este programa puedes resolver una ecuación cuadrática. Por favor ingresa el primer valor: "))
b= int(input("Por favor ingresa el valor b: "))
c=int(input("Finalmente ingresa el tercer valor (C):"))

d = b**2-4*a*c

if d < 0:
    print "Lo siento , esta ecuación no tiene alguna solución."
elif d == 0:
    x = (-b+math.sqrt(b**2-4*a*c))/2*a
    print "Este ejercicio tiene dos soluciones. Dame un segundo mientras que lo resuelvo...", x
else:
    x1 = (-b+math.sqrt(b**2-4*a*c))/2*a
    x2 = (-b-math.sqrt(b**2-4*a*c))/2*a
    print ("Los resultados de esta ecuación cuadrática es {} y {} . Gracias por utilizar este programa.".format(x1,x2))
#Trabajo creado por Pedro Felipe Gómez ; ID : 000396221
