"""
Created on Thu Oct  20 09:10:32 2021

@author: jointedace
"""
import numpy as np
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
from scipy.integrate import odeint
import random


order=5
INFI=-10000
ENERGY=1.0/8.0#default

def henon(Y,t):
    x,y,px,py=Y
    dydt=[px,py,-x-(2*x*y),-y-(x*x)+(y*y)]
    return dydt

def getini(y,py):
    global INFI, ENERGY
    E=ENERGY
    x=0
    px=2*E-(py**2)-(y**2)+((y**3)*(2.0/3.0))
    if px<0:
        return (INFI,[])
    
    px=np.sqrt(px)
    px=abs(px)
    
    ps=[x,y,px,py]
    
    return (E,ps)

def weightadd(y,k,h):#y+k*h
    t=[]
    for i in range(len(y)):
        t.append(y[i]+h*k[i])
    return t

def rkstep(y,dt):
    k1=henon(y,dt)
    k2=henon(weightadd(y,k1,dt/2),dt)
    k3=henon(weightadd(y,k2,dt/2),dt)
    k4=henon(weightadd(y,k3,dt),dt)
    
    yp=weightadd(k1,k2,2)
    yp=weightadd(yp,k3,2)
    yp=weightadd(yp,k4,1)
    yp=weightadd(y,yp,dt/6.0)
    
    #yp=y+(dt/6)*(k1+2*k2+2*k3+k4)
    
    return 1*yp

def newsolver(y,py):
    global order,INFI
    E,ps=getini(y,py)
    
    if E == INFI:
        #print('bad intial!')
        return({},[])
    
    N=10**3
    t=np.linspace(0,100,N)
    dt=t[1]-t[0]
    
    yt={}
    y0=1*ps
    
    for i in range(N):
        yt[t[i]]=y0
        y0=rkstep(y0,dt)
    
    return (yt,t)


def ploter(yt,t):
    global order
    
    Y=[]
    Py=[]
    
    for i in range(1,len(t)-1):
        y=yt[t[i]]#x,y,px,py
        if (y[0])*(yt[t[i+1]][0])<0:#x(t)=0
            #print('P!')
            Y.append(y[1])
            Py.append(y[3])
        else:
            #print('N')
            continue
            
    return (Y,Py)


def runensemble(n,s,f,E,axs):
    global ENERGY
    testy=np.linspace(-s,f,n)
    testp=np.linspace(-s,f,n)
    
    PSy=[]
    PSpy=[]
    
    ENERGY=E
    
    for i in range(n):
        #print(i)
        for j in range(n):
            y0,py0=testy[i],testp[j]
            
            yt,t=newsolver(y0,py0)
            Y,Py=ploter(yt,t)
            
            for k in range(len(Y)):
                PSy.append(Y[k])
                PSpy.append(Py[k])

    axs.scatter(PSy,PSpy)
    axs.set(xlabel='Y',ylabel='Py')
    axs.set_title('Poincare section x=0 for energy E= ' +str(round(E,3)))

Ecase=[1.0/12.0,1.0/15.0,1.0/8.0,1.0/6.0]


n=10
start=0.6
finish=0.6

fig, axs= plt.subplots(1,len(Ecase),tight_layout=True,figsize=(4*len(Ecase),4))
for i in range(len(Ecase)):
    runensemble(n,start,finish,Ecase[i],axs[i])

