with open("1.txt") as f:
    line = f.read().strip().split("\n")

input = []
for i in line:
    if i != "":
        input.append(int(i));
    else:
        input.append(-1)

sum = 0
max = 0
input2 = []
for i in input:
    if i != -1:
        sum += i
    else:
        if sum > max:
            max = sum
        input2.append(sum)
        sum = 0
if sum > max:
    max = sum   
n1 = 0
n2 = 0
n3 = 0
input2.sort()
print(input2[-1] + input2[-2] + input2[-3])