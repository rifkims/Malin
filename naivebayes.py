import csv
import math 
# Naive Bayes data excelnya yang data trinset sama data test ya
#data yang digunakan untuk menghitung dan menentukan kelas >50K dan <=50K
age_a = [['young',0],['adult',0],['old',0]]
age_b = [['young',0],['adult',0],['old',0]]
wc_a = [['Private',0],['Self-emp-not-inc',0],['Local-gov',0]]
wc_b = [['Private',0],['Self-emp-not-inc',0],['Local-gov',0]]
edu_a = [['Some-college',0],['Bachelors',0],['HS-grad',0]]
edu_b = [['Some-college',0],['Bachelors',0],['HS-grad',0]]
ms_a = [['Married-civ-spouse',0],['Never-married',0],['Divorced',0]]
ms_b = [['Married-civ-spouse',0],['Never-married',0],['Divorced',0]]
occup_a = [['Prof-specialty',0],['Exec-managerial',0],['Craft-repair',0]]
occup_b = [['Prof-specialty',0],['Exec-managerial',0],['Craft-repair',0]]
rship_a = [['Husband',0],['Not-in-family',0],['Own-child',0]]
rship_b = [['Husband',0],['Not-in-family',0],['Own-child',0]]
hpw_a = [['normal',0],['low',0],['many',0]]
hpw_b = [['normal',0],['low',0],['many',0]]
train = []
test = []
prob_a = {}
prob_b = {}
priori = {}
prior_a = 0
prior_b = 0

with open ('TrainsetTugas1ML.csv') as datatrml: #untuk membaca file csv data train
	next(datatrml)
	spamreader = csv.reader(datatrml,  delimiter=',')
	for bar in spamreader:
		train.append(bar)
		if (bar[8] == '>50K'):
			prior_a += 1
		else:
			prior_b += 1
		
prior_a = prior_a/len(train)
prior_b = prior_b/len(train)

def separate(dataset): #fungsi yang memsiahkan data yang ada kedalam kelas >50K dan <=50K
	separated = {}
	for i in range(len(dataset)):
		cbcb = dataset[i]
		if (cbcb[-1] not in separated):
			separated[cbcb[-1]] = []
		separated[cbcb[-1]].append(cbcb)
	return separated

def proprior(x,y,q): #untuk memisahkan data yang dibawah 50k dan diatas 50k 
	prior_a = 0
	prior_b = 0
	priori = separate(train)
	for key in priori:
		for a in priori[key]:
			if (key == '>50K'):
				prior_a +=1
				for i in range(0,len(x)):
					if (a[q] == x[i][0]):
						x[i][1] += 1		
			else:
				prior_b +=1
				for j in range(0,len(y)):
					if (a[q] == y[j][0]):
						y[j][1] += 1
	List(x,y,prior_a,prior_b)

def List(aa,bb,a,b): #untuk menghitung probalitas dari setiap data yang ada ditiap kelas
	for x in range(0, len(aa)):
		if aa[x][0] not in prob_a:
			prob_a[aa[x][0]] = aa[x][1]/a
	for x in range(0, len(bb)):
		if bb[x][0] not in prob_b:
			prob_b[bb[x][0]] = bb[x][1]/b

def getPredictions(summaries, testSet): #fungsi untuk memprediksi
	predictions = []
	for i in range(len(testSet)):
		result = predict(summaries, testSet[i])
		predictions.append(result)
	return predictions

proprior(age_a,age_b,1) #untuk memanggil data yg sudah terbagi di kelas >50K, <=50K
proprior(wc_a,wc_b,2)
proprior(edu_a,edu_b,3)
proprior(ms_a,ms_b,4)
proprior(occup_a,occup_b,5)
proprior(rship_a,rship_b,6)
proprior(hpw_a,hpw_b,7)

with open ('TestsetTugas1ML.csv') as datatsml: #untuk membaca file csv data tes
	next(datatsml)
	spamreader = csv.reader(datatsml,  delimiter=',')
	listBarisb = []
	for bar in spamreader:
		del bar[0]
		up50 = 1
		down50 = 1
		for key,isi in prob_a.items(): #untuk menghitung Ph(X)
			for a in range(0,len(bar)):
				if (key == bar[a]):
					up50 = up50 * isi
		up50 = up50 * prior_a
		for key,isi in prob_b.items():
			for a in range(0,len(bar)):
				if (key == bar[a]):
					down50 = down50 * isi
		down50 = down50 * prior_b
		if (up50>down50): #untuk mengkelompokan data >50K dan <=50K
			test.append('>50K')
		else:
			test.append('<=50K')
			
with open ('TebakanTugas1ML.csv','w',newline='') as hasilfile: #untuk memasukan hasil ke csv baru
    writer = csv.writer(hasilfile)
    for x in test:
        writer.writerow([x])
