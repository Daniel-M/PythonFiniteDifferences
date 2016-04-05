#!/usr/bin/python3

import numpy as np
import math
import sys

def condicionInicial(x,A,B):
    return A*math.exp(-(0.5-x)**2/B)

def iterarZ(dt,dz,ZMax,ZMin,i,Ci):
    alpha_ = dt/(dz**2)
    if(i==ZMax):
        return Ci[i] + 2*alpha_*(-Ci[i]+Ci[i-1])
    elif(i==ZMin):
        return Ci[i] + 2*alpha_*(Ci[i+1]-Ci[i])
    elif( (ZMax > i ) and ( i > ZMin) ):
        return Ci[i] + alpha_*(Ci[i+1]-2*Ci[i]+Ci[i-1])
    else:
        print ("El indice no existe")

def crearData1D(dz,nombreBase,instante,nodosInicial):
    fileName=nombreBase + "." + str(instante)
    f = open(fileName,'w')
    f.write("#z\tC(z)\n")
    #print (Ci)
    #print ("\n")
    for i in range(0,Nz+1):
        f.write(str(float(i*dz)) + "\t" + str(nodosInicial[i]) + "\n")
    f.close()

print ("Python Sandbox for FD test in Z")
Nz  = int(sys.argv[1])
tf = float(sys.argv[2])
dz = 1.0/Nz
dt = (0.5*dz**2)/2
t  = 0
zval=[]
Ci=[]
Ci1=[]

instante=0

for i in range(0,Nz+1):
    #print (str(i))
    zval.append(i*dz)
    Ci.append(condicionInicial(i*dz,1,0.1*0.1))

print ("Z values:")
print (zval)
print (Ci)

Ci1 = Ci

crearData1D(dz,"iteration",instante,Ci)

while(t<tf):
    for i in range(0,11):
        Ci1[i]=iterarZ(dt,dz,Nz,0,i,Ci)
    crearData1D(dz,"iteration",instante,Ci1)
    instante+=1
    t+=dt
    Ci=Ci1

print (Ci)    
crearData1D(dz,"iteration",instante,Ci)
