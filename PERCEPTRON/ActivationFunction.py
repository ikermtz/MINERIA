import math



y = [1.1,2.0,3.3,4.2,5.5,6.0]

print()
print("--- SOFTMAX ACTIVATION FUNCTION ---")

softmaxValues = []

tot = 0
for i in y:
    tot = tot + math.exp(i)

for i in y:
    softmax = math.exp(i)/tot
    softmaxValues.append(softmax)

print(softmaxValues)
print(sum(softmaxValues))


print()
print("--- SIGMOID ACTIVATION FUNCTION ---")

sigmoidValues = []

for i in y:
    sigmoid = (1)/ 1 + (1/math.exp(i))
    sigmoidValues.append(sigmoid)

print(sigmoidValues)
print(sum(sigmoidValues))