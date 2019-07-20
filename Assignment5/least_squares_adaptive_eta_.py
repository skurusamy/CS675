import sys
import random

##read data file
datafile=sys.argv[1]
f=open(datafile)
data=[]
i=0
l=f.readline()
while(l!=''):
    k=l.split()
    l2=[]
    for j in range(0,len(k),1):
        l2.append(float(k[j]))
    data.append(l2)
    l=f.readline()

rows=len(data)
cols=len(data[0])
f.close()
#--------------------------------------------------------------
##read label data
labelfile=sys.argv[2]
f=open(labelfile)
trainlabels={}
n=[]
n.append(0)
n.append(0)
l=f.readline()
while(l!=''):
	k=l.split()
	trainlabels[int(k[1])]=int(k[0])
	#print(trainlabels[int(k[1])])
	l=f.readline()
	n[int(k[0])]+=1

##initialize w
w = []

for j in range(cols):
	w.append(0)
	w[j] = (0.02 * random.uniform(0,1)) - 0.01

##define function dot_product
def dotproduct(list1, list2):
	dotproduct = 0
	refw = list1
	refx = list2
	for j in range (cols):
		dotproduct += refw[j] * refx[j]
	return dotproduct

eta_list = [1, .1, .01, .001, .0001, .00001, .000001, .0000001, .00000001, .000000001, .0000000001, .00000000001 ]
bestobj = 1000000000000
for k in range(0, len(eta_list), 1):
	eta = eta_list[k]
##gradient descent iteration
##eta = 0.0001
##calculate error outside the loop
error=0.0
# for i in range (rows):
	# if(trainlabels.get(i) != None):
		# error += ( -trainlabels.get(i) + dotproduct(w,data[i]) )**2

#initialize flag and iteration parameters
flag = 0
k=0
while(flag != 1):
	k+=1
	delf = []
	for i in range(cols):
		delf.append(0)

	for i in range(rows):
		if(trainlabels.get(i) != None):
			dot_product = dotproduct(w, data[i])
			for j in range (cols):
#compute gradient
				delf[j] += (-trainlabels.get(i) + dot_product) * data[i][j]

##update
	for j in range(cols):
		w[j] = w[j] + eta*delf[j]

##compute error
	curr_error = 0
	for i in range (rows):
		if(trainlabels.get(i) != None):
			curr_error += ( -trainlabels.get(i) + dotproduct(w,data[i]) )**2
	#print(error,k)
	if error - curr_error < 0.001:
		flag = 1
	error = curr_error	
	print("best eta",eta)
##remove eta	
for j in range(cols):
    w[j] = w[j] - eta*delf[j]
print("w =",w[:-1])

normw = 0
for j in range((cols-1)):
    normw += w[j]**2
    #print(w[j])

normw = (normw)**0.5
print("||w||=", normw)

origin_distance = w[(len(w)-1)] / normw
print("origin_distance =",abs(origin_distance))

for i in range(rows):
    if(trainlabels.get(i) == None):
        dot_product = dotproduct(w, data[i])
        if(dot_product > 0):
            print("1",i)
        else:
            print("0",i)




