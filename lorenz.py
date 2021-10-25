# -*- coding: utf-8 -*-
"""
Created on Thu Oct  7 09:33:56 2021

@author: jointedace
"""

import numpy as np
import matplotlib.pyplot as plt
from numpy import dot as dot
from scipy import linalg as LA

def map(x,r):
    y= np.mod(r*x*(1-x),1)
    return y


N=10

X={}
X0=np.linspace(0,1,N)


R=np.linspace(3,4,N)

for i in range(N):
    r=R[i]
    for j in range(N):
        x0=X0[j]
        n=[]
        xt=[]
        x=np.mod(x0+np.pi,1)
        for t in range(N**2):
            n.append(t)
            xt.append(x)
            x=map(x,r)
        X[(x0,r)]=(1*xt,1*n)

while True:
    i=int(input('xo '))
    j=int(input('r '))
    xt,n=X[(X0[i],R[j])]
    fig=plt.figure()
    plt.plot(n,xt)
    plt.xlabel('n')
    plt.ylabel('Xn')
    ti='X0= '+str(np.mod(X0[i]+np.pi,1))+' ; r= '+str(R[j])
    plt.title(ti)
    plt.show()
    fil=str(i)+'('+str(j)+').png'
    #fig.savefig(fil)
"""
i=0
while i<N:
    j=0
    while j<N:
        xt,n=X[(X0[i],R[j])]
        fig=plt.figure()
        plt.plot(n,xt)
        plt.xlabel('n')
        plt.ylabel('Xn')
        ti='X0= '+str(np.mod(X0[i]+np.pi,1))+' ; r= '+str(R[j])
        fil='pic00'+str(i)+str(j)+'.png'
        plt.title(ti)
        plt.show()
        #fig.savefig(fil)
        j=j+1
    i=i+1
"""
