#!/usr/bin/python3

import numpy as np
import math
import sys

def condicionInicial(x,A,B):
    return A*math.exp(-(0.5-x)**2/B)

def iterarR(dt,dx,Max,Min,i,Ci):
    r = dt/(dx**2)
    if(i==Max):
        return Ci[Max]+2*r*(Ci[Max-1]-Ci[Max])
    elif(i==Min):
        return Ci[Min] + 4*r*(Ci[Min+1]-Ci[Min])
    elif( (Max > i ) and ( i > Min) ):
        return Ci[i]+r*((2*i+1)*Ci[i+1]-(4*i)*Ci[i]+(2*i-1)*Ci[i-1])/(2*i)
    else:
        print ("El indice no existe")

print ("Python Sandbox for FD test in R")
N  = int(sys.argv[1])
tf = float(sys.argv[2])
dr = 1.0/N
dt = (0.5*dr**2)/2
t  = 0
rval=[]
Ci=[]
Ci1=[]

for i in range(0,N+1):
    #print (str(i))
    rval.append(i*dr)
    Ci.append(condicionInicial(i*dr,1,0.1*0.1))

print ("R values:")
print (rval)
print (Ci)

Ci1 = Ci

while(t<tf):
    for i in range(0,11):
        Ci1[i]=iterarR(dt,dr,N,0,i,Ci)
    t+=dt
    print ("t= %f" % t)
    #print (Ci1)
    Ci=Ci1
    print (Ci)
    print ("\n")

print(Ci)
