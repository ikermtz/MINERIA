import random,numpy

orGate = [[0,0],[0,1],[1,0],[1,1]]
realOutput = [0,1,1,1]
bias = 1
lr = 1

weights = []
for k in range(3):
    weights.append(random.random())

def perceptron(inp1,inp2,output):
    out_perc = inp1*weights[0]+inp2*weights[1]+bias*weights[2]
    out_perc = 1.0 / (1 + numpy.exp(-out_perc))
    error = output - out_perc
    weights[0] += error*inp1*lr
    weights[1] += error*inp2*lr
    weights[2] += error*bias*lr


j=0
max_iter = 10
while j<max_iter:
    i = 0
    
    for x,y in orGate:
        out_perc = x*weights[0]+y*weights[1]+bias*weights[2]
        outp = 1.0/(1+numpy.exp(-out_perc))
        print( x, "OR" , y)
        print(outp)
        print(realOutput[i])
        print("Iteracion", j)
        print("---")
        i=i+1

    j=j+1