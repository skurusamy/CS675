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
	data[i].append(1)
	i+=1

rows=len(data)
cols=len(data[0])
f1.close()

#Read labels from file
filename = sys.argv[2]
f2=open(filename,"r")
labels={}
m=[]
m.append(0)
m.append(0)
l2=f2.readline()
while (l2 != ''):
	b=l2.split()
	labels[int(b[1])] = int(b[0])
#	if(labels[int(b[1])]==0):
#		labels[int(b[1])]= -1
	l2=f2.readline()
	m[int(b[0])]+=1
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
	n = float(0.02*random.uniform(0,1)-0.01)
#	n=  random.uniform(-0.01,0.01)
	w.append(n)
#gradient descent iteration
eta=0.01
stop_condition=0.0000001
error=0
prevobj = 0
#compute gradient and error
while True:
	gradient=[0]*cols
	prevobj=error
	#for j in range(0,cols,1):
	#	gradient.append(0)
	for i in range (0,rows,1):
		dp=0
		if (labels.get(i) != None):
			dp=dot_product(w,data[i])
			dp=1/(1+math.exp(-dp))
			for j in range (0,cols,1):
				gradient[j]+=(labels.get(i)-dp)*(data[i][j])
#update w
	for j in range (0,cols,1):
		w[j]=w[j] + eta*gradient[j]
#error
	error=0
	for i in range(0,rows,1):
		if(labels.get(i)!=None):
			if(labels[i]==0):
				error += -1 *math.log(1- 1/(1+math.exp(-1 *dot_product(w,data[i]))))
			else:
				dp =dot_product(w,data[i])
				exp1 = math.exp(-1*dp)
				error += -1 * math.log(1/(1+ math.exp(-1 *dot_product(w,data[i]))))
	if abs(prevobj - error ) <= stop_condition :
		break


#print("w",w)
w1=[]#only printing
#distance from origin calculation
normw=0
for j in range(0,cols-1,1):
	normw += w[j]**2
	w1.append(w[j])
print("weights: ",w1)
#print("w0:",w[j+1])
#normw = normw**5
normw = math.sqrt(normw)
print("||w||",normw)
d_origin =( w[len(w)-1]/normw)
print("distance from origin: ",d_origin)

for i in range(0,rows,1):
	if (labels.get(i) == None):
		dp = dot_product(w,data[i])
		if dp>0:
            		print("1,",i)
		else:
            		print("0,",i)

