#!/usr/bin/python3

import numpy as np
import math
import sys

def condicionInicial(z,r,A,B):
    return  

def condicionInicial(x,A,B):
    return A*math.exp(-(0.5-x)**2/B)

def iterarR(dt,dz,dr,ZMax,ZMin,RMax,RMin,i,j,Ci):
    alpha_ = dt/(dr**2)
    if(j==RMax):
        #print ("[iterarR][RMax] j = %d",j)
        return 2*alpha_*(Ci[i][RMax-1]-Ci[i][RMax])
    elif(j==RMin):
        #print ("[iterarR][RMin] j = %d",j)
        return 4*alpha_*(Ci[i][RMin+1]-Ci[i][RMin])
    elif( (RMax > j ) and ( j > RMin) ):
        return alpha_*((2*j+1)*Ci[i][j+1]-(4*j)*Ci[i][j]+(2*j-1)*Ci[i][j-1])/(2*j)
    else:
        print ("El indice no existe")

def iterarZ(dt,dz,dr,ZMax,ZMin,RMax,RMin,i,j,Ci):
    alpha_ = dt/(dz**2)
    if(i==ZMax):
        #print ("[iterarZ][ZMax] i = %d",i)
        return alpha_*(-Ci[i][j]+Ci[i-1][j])
    elif(i==ZMin):
        #print ("[iterarZ][ZMin] i = %d",i)
        return alpha_*(Ci[i+1][j]-Ci[i][j])
    elif( (ZMax > i ) and ( i > ZMin) ):
        return alpha_*(Ci[i+1][j]-2*Ci[i][j]+Ci[i-1][j])
    else:
        print ("El indice no existe")

def iterarNodo(dt,dz,dr,ZMax,ZMin,RMax,RMin,i,j,nodos):
    resultado = nodos
    return nodos[i][j] + (iterarZ(dt,dz,dr,ZMax,ZMin,RMax,RMin,i,j,nodos) + iterarR(dt,dz,dr,ZMax,ZMin,RMax,RMin,i,j,nodos))
    #return nodos[i][j] + iterarR(dt,dz,dr,ZMax,ZMin,RMax,RMin,i,j,nodos)
    #return nodos[i][j] + iterarZ(dt,dz,dr,ZMax,ZMin,RMax,RMin,i,j,nodos)

def iterarPaso(dt,dz,dr,ZMax,ZMin,RMax,RMin,nodos):
    resultado = nodos
    for i in range(0,Nz+1):
        for j in range(0,Nr+1):
            resultado[i][j] = iterarNodo(dt,dz,dr,ZMax,ZMin,RMax,RMin,i,j,nodos)
    return resultado

def crearData(dz,dr,nombreBase,instante,nodosInicial):
    fileName=nombreBase + "." + str(instante)
    #print(" Creating " + fileName)
    f = open(fileName,'w')
    f.write("#z r C(r,z)\n")
    for i in range(0,Nz+1):
        for j in range(0,Nr+1):
            #print(str(float(i*dz)) + " " + str(float(j*dz)) + " " + str(nodosInicial[i][j]))
            f.write(str(float(i*dz)) + " " + str(float(j*dr)) + " " + str(nodosInicial[i][j]) + "\n")
    f.close()


print ("#Python Sandbox for FD test")
print ("#z r C(r,z)")
Nz = int(sys.argv[1])
Nr = int(sys.argv[2])
tf = float(sys.argv[3])
dz=1.0/Nz
dr=0.5/Nr
dt=(0.5*(1/((1/(dr**2))+(1/(dz**2)))))/10
#dt=(0.5*dr**2)/2
t=0.0
zval=[]
rval=[]
nodes=[[0 for i in range(Nr+1)] for j in range(Nz+1)] 
Ci=[]
Ci1=[]
instante=0



for i in range(0,Nz+1):
    for j in range(0,Nr+1):
        #nodes[i][j] = condicionInicial(j*dr,1,0.1*0.1)
        #nodes[i][j] = condicionInicial(i*dz,j*dr,1,0.1*0.1)
        nodes[i][j] = condicionInicial(i*dz,1,0.1*0.1)
        #print(str(float(i*dz)) + " " + str(float(j*dz)) + " " + str(condicionInicial(i*dr,1,0.1*0.1)))
        print(str(float(i*dz)) + " " + str(float(j*dz)) + " " + str(nodes[i][j]))

nodosInicial = nodes

crearData(dz,dr,"iteration",instante,nodosInicial)
print("#dt = " + str(dt))

while(t<tf):
    nodes = iterarPaso(dt,dz,dr,Nz,0,Nr,0,nodosInicial)
    nodosInicial = nodes
    instante+=1
    crearData(dz,dr,"iteration",instante,nodosInicial)
    print("#Current t = " + str(t) + " out of " + str(tf) )
    t+=dt

#for i in range(0,Nr+1):
    #for j in range(0,Nz+1):
        #print(str(float(i*dz)) + " " + str(float(j*dz)) + " " + str(nodosInicial[i][j]))
