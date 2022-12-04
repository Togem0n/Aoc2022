with open("4.txt") as f:
    lines = f.read().strip().split("\n")
res = 0
for line in lines:
    input = line.split(",")
    tmp = []
    for bundle in input:
        numbers = bundle.split("-")
        tmp.append(int(numbers[0]))
        tmp.append(int(numbers[1]))
    if(tmp[0] == tmp[2] and tmp[1] == tmp[3]) :
        res += 1
        continue
    if(tmp[0] <= tmp[2] and tmp[1] >= tmp[3] ):
        res += 1
    if(tmp[0] >= tmp[2] and tmp[1] <= tmp[3] ):
        res += 1
print(res)

res = 0
for line in lines:
    input = line.split(",")
    tmp = []
    for bundle in input:
        numbers = bundle.split("-")
        tmp.append(int(numbers[0]))
        tmp.append(int(numbers[1]))
    if(tmp[1] < tmp[2]):
        res += 1
    if(tmp[0] > tmp[3]):
        res += 1
print(len(lines)-res)