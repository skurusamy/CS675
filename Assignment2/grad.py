import sys
import random
import math

filename=sys.argv[1]
f1=open(filename,"r")
i=0
data=[]
l=f1.readline()
while (l != ""):
	a=l.split()
	l2 =[]
	for j in range (0,len(a),1):
		l2.append(float(a[j]))
	data.append(l2)
	l=f1.readline()

rows=len(data)
cols=len(data[0])
f1.close()

#Read labels from file
filename = sys.argv[2]
f2=open(filename,"r")
labels={}
l2=f2.readline()
while (l2 != ''):
	b=l2.split()
	labels[int(b[1])] = int(b[0])
	l2=f2.readline()

f2.close()

#dot product function
def dot_product(arg1,arg2):
        dp1=0
        for j in range(0,cols,1):
                dp1 += arg1[j]*arg2[j]
        return dp1;

#Initialize w
w=[]
for j in range(0,cols,1):
	n = 0.02*random.random()- 0.01
	w.append(n)
#gradient descent iteration
eta=0.001
stop_condition=0.001
error=0
#compute gradient and error
while True:
	prevobj = error
	gradient=[]
	error=0
	for j in range(0,cols,1):
		gradient.append(0)
	for i in range (0,rows,1):
		dp=0
		if (labels.get(i) != None and labels.get(i) ==0):
			dp=dot_product(w,data[i]);
			for j in range (0,cols,1):
				gradient[j] += (labels[i]-dp)*data[i][j]
#update w
	for j in range (0,cols,1):
		w[j]=w[j]+eta*gradient[j]
#error 
	for i in range(0,rows,1):
		if(labels.get(i)!=None):
			error += (labels[i] - dot_product(w,data[i]))**2
	if abs(prevobj - error ) <= stop_condition :
		break
print(error)	
print("Error= ",error)

#distance from origin calculation
normw=0
for j in range(0,cols-1,1):
	normw += w[j]**2
#	print(w[j])
print("w",w)

normw = math.sqrt(normw)
print("||w||",normw)
d_origin = w[len(w)-1]/normw
print("distance from origin: ",d_origin)

for i in range(0,rows,1):
	if (labels.get(i) == None):
		dp = dot_product(w,data[i])
		if dp>0:
            		print("1,",i)
		else:
            		print("0,",i)

