#ini tugas 3 malin tentang som
import numpy as np 
import matplotlib.pyplot as plt
import random as random
import csv 
import math

def mathA(a,b): #rumus euclidian
    dist = 0

    for x in range(2):
        dist += pow((a[x]-b[x]), 2)

    return np.sqrt(dist)

def mathB(i,j): #rumus euclidian
    distance = 0

    for x in range(2):
        distance += pow((i[x]-j[x]), 2)

    return distance

Data = []
with open ('datatugas2.csv') as datacsv: #untuk membaca file csv data tes
    next(datacsv)
    spamreader = csv.reader(datacsv,  delimiter=',', quotechar='|' )
    for row in spamreader:
        X = [float(row[0]),float(row[1])]
        Data.append(X)

berat = np.random.rand(15,2)+10
learningrate = 0.4
itterasi = 20
tahulr = 8
tahusigm = itterasi/np.log(15)
sigm = 0.1
t_sigm = itterasi/np.log(15)
a = 0

while (a != itterasi):
    learningratebaru = learningrate*math.exp(-a/tahulr)
    newsigm = sigm*math.exp(-a/tahusigm)
    for i in range(len(Data)):
        dist = []
        for j in range(len(berat)):
            beta = mathB(Data[i], berat[j])
            dist.append(beta)
        aa = np.argmin(dist)
        mini = berat[aa]
        for n in range (len(berat)):
            for m in range (2):
                hasil = -mathA(mini, berat[n])/(2*(newsigm**2))
                tim = math.exp(hasil)
                delta = learningratebaru*tim*(Data[i][m] - berat[n][m])
                berat[n][m] = berat[n][m] + delta
    a+=1

print(berat)

for i in range(0, len(Data)):
    alpa = Data[i]
    plt.scatter(alpa[0], alpa[1],c='b')

for i in berat:
    plt.scatter(i[0], i[1], c='r')

plt.show()
