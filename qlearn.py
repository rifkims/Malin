import numpy as np
import pandas as pd
import random as random
import matplotlib.pyplot as plt 

#QLearning pake TXT ya

data = np.genfromtxt('data3.txt')
q_matrix = np.zeros((15,15))
g = 0.8
a = 1
lastMove = [0,14]

def valid(E):
    baris = E[0]
    kolom = E[1]
    arah = ['N','E','W','S']
    if (kolom==0):
        arah.remove('W')
    if (baris==0):
        arah.remove('N')
    if (baris==len(q_matrix)-1):
        arah.remove('S')
    if (kolom==len(q_matrix)-1):
        arah.remove('E')
    return arah

def move(E,arah):
    moveR = E[0]
    moveC = E[1]
    if (arah=='N'):
        moveR = moveR-1
    if (arah=='E'):
        moveC = moveC+1
    if (arah=='W'):
        moveC = moveC-1
    if (arah=='S'):
        moveR = moveR+1
    return[moveR, moveC]

def belMan(r,q,lis):
    return q + (a * (r + (g * (max(lis)))-q))

def isi(n):
    for i in range(n):
        start = [14,0]
        current = start
        while (current!=lastMove): 
            action = random.choice(valid(current)) 
            tujuan = move(current,action) 
            reward = data[tujuan[0], tujuan[1]] 
            temp=[]
            for act in valid(tujuan):
                kemungkinan = move(tujuan, act)
                temp.append(q_matrix[kemungkinan[0],kemungkinan[1]]) 

            q_matrix[tujuan[0],tujuan[1]] = belMan(reward,q_matrix[tujuan[0],tujuan[1]],temp) 
            current = tujuan 

def jalan():
    path = []
    reward = 0
    start = [14,0] 
    current = start
    path.append(current)
    
    while (current!=lastMove): 
        q_state = {}
        for act in valid(current):
            maju = move(current, act)
            q_state[act] = q_matrix[maju[0], maju[1]] 
        best = max(q_state,key=q_state.get)
        c = move(current,best) 
        reward += data[c[0],c[1]] 
        
        current = c 
        path.append(current)

    p = path
    print(p)
    print(reward)
    for i in p:
        tmp = i
        plt.scatter(x=tmp[0],y=tmp[1])
    

isi(100)
jalan() 
plt.show()
