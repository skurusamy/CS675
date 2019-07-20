import sys
datafile=sys.argv[1]
f=open(datafile)
i=0
data=[]
l=f.readline()
while (l != ''):
	k=l.split()
	l2 =[]
	for j in range (0,len(k),1):
		l2.append(float(k[j]))
	data.append(l2)	
	l=f.readline()

rows=len(data)
cols=len(data[0])
f.close()

#Reading labels from file
lablfile = sys.argv[2]
f2=open(lablfile)
trainlabels={}
n=[]
n.append(0)
n.append(0)
l2=f2.readline()
print("Training labels\n")
while (l2 != ''):
	g=l2.split()
	trainlabels[int(g[1])] = int(g[0])
	print(trainlabels[int(g[1])])
	l2=f2.readline()
f2.close()

m0=[]
m1=[]

for j in range (0,cols,1): 
	m0.append(0)
	m1.append(0)

n0=0.0000001
n1=0.0000001

for i in range(0,rows,1):
	if (trainlabels.get(i) != None and trainlabels.get(i) == 0):
		n0+=1
	for j in range (0,cols,1):
		m0[j] += data[i][j]
	if (trainlabels.get(i) != None and trainlabels.get(i) == 1):
		n1+=1
	for j in range (0,cols,1):
		m1[j] += data[i][j]

for j in range (0,cols,1):
	m0[j] /= n0
	m1[j] /= n1
print ("Mean of class 0 is ",m0)
print("\n")
print ("Mean of class 1 is ",m1)

vari0=[]
vari1=[]
for j in range (0,cols,1):
	vari0.append(0.00000001)
	vari1.append(0.00000001)

for i in range(0,rows,1):
	if (trainlabels.get(i) != None and trainlabels.get(i) == 0):
		for j in range (0,cols,1):
			vari0[j] += ((m0[j] - data[i][j])**2)
	if (trainlabels.get(i) != None and trainlabels.get(i) == 1):
		for j in range (0,cols,1):
			vari1[j] += ((m1[j] - data[i][j])**2)

for j in range (0,cols,1):
	vari0[j] /= n0
	vari1[j] /= n1
print("Variance of class 0 is ",vari0)
print("\n")
print("Variance of class 1 is", vari1)

l={}

for i in range (0,rows,1):
	w0=0
	w1=0 
	if (trainlabels.get(i) == None):
		for j in range (0,cols,1):
			w0 += ((m0[j] - data[i][j])/vari0[j])**2
			w1 += ((m1[j] - data[i][j])/vari1[j])**2
		if (w0 < w1):
			print("0",i)
			l[i]=0
		else:
			print("1",i)
			l[i]=1

