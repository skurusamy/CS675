import sys
import random
import math

datafile = sys.argv[1]

f = open(datafile, 'r')
data = []
# i = 0
l = f.readline()

#################
### Read Data ###
#################

while (l != ''):
    a = l.split()
    l2 = []
    for j in range(0, len(a), 1):
        l2.append(float(a[j]))
    l2.append(float(1))
    data.append(l2)
    l = f.readline()

rows = len(data)
cols = len(data[0])

# print("rows=", rows," cols=", cols)

f.close()
# print(data)
###############################
##### read training labels ####
###############################

labelfile = sys.argv[2]
f = open(labelfile)
trainlabels = {}
n = [0, 0]
l = f.readline()
while (l != ''):
    a = l.split()
    trainlabels[a[1]] = int(a[0])
    #    trainlabels_size[a[0]] = trainlabels_size[a[0]]+1
    if (trainlabels[a[1]] == 0):
        trainlabels[a[1]] = -1;
    l = f.readline()

    n[int(a[0])] += 1

f.close()
print(trainlabels)
# print(trainlabels)
##################################
########## initialize w ##########
##################################
# print("this is new code")
w = []
for j in range(0, cols, 1):
    # print(random.random())
    w.append(0.02 * random.random() - 0.01)


# print(w)

#####################################
#### calculation of doc product #####
#####################################

def dot_product(a, b):
    dp = 0
    for i in range(0, cols, 1):
        dp += a[i] * b[i]
    # dp = sum(p*q for p,q in zip(a, b))
    return dp


#######################################
##### gradient descent iteration ######
#######################################

eta = 0.0001
error = rows + 10
diff = 1
count = 0
# for i in range(0, 1500, 1):
while ((diff) > 0.00000001):
    dellf = []
    for m in range(0, cols, 1):
        dellf.append(0)
    for j in range(0, rows, 1):
        if (trainlabels.get(str(j)) != None):
            dp = dot_product(w, data[j])
            for k in range(0, cols, 1):
                dellf[k] += (trainlabels.get(str(j)) - dp) * data[j][k]

    ##########################
    ####### update w #########
    ##########################

    for j in range(0, cols, 1):
        w[j] = w[j] + eta * dellf[j]

    prev = error
    error = 0

    ############################
    #### compute error #########
    ###########################

    for j in range(0, rows, 1):
        if (trainlabels.get(str(j)) != None):
            # print(dot_product(w,data[j]))
	      error += max(0, 1 - trainlabels.get(j) * dotproduct(w, data[j]))
            #error += (trainlabels.get(str(j)) - dot_product(w, data[j])) ** 2
    if (prev > error):
        diff = prev - error
    else:
        diff = error - prev
    count = count + 1
    if (count % 100 == 0):
        print(error)

print ("error = " + str(error))

# print("w= ")
normw = 0
for i in range(0, (cols - 1), 1):
    normw += w[i] ** 2
    print ("w ", w)

# print("")

# normw = (normw)**0.5
normw = math.sqrt(normw)
# print("sqrt")
# print("||w||="+str(normw))
# print("")

d_orgin = abs(w[len(w) - 1] / normw)

print ("Distance to origin = " + str(d_orgin))

#################################
###### calc of prediction #######
#################################

for i in range(0, rows, 1):
    if (trainlabels.get(str(i)) == None):
        dp = dot_product(w, data[i])
        if (dp > 0):
            print("1 " + str(i))
        else:
            print("0 " + str(i))
