with open("5.txt") as f:
    lines = f.read().split("\n")

tmp1 = []
tmp2 = []

switch = False
for line in lines:
    if not switch:
        tmp1.append(line)
    else:
        tmp2.append(line)
    if line == "":
        switch = True
list = []
size = 0
for i in tmp1[-2]:
    if i.isdigit():
        size = i
size = int(size) + 1

for i in range(size):
    list.append([])
# 1 5 9 13      index = (x-1/4)+1
for line in tmp1:
    for i in range(len(line)):
        if(line[i].isalpha()):
            # print((i-1)/4+1)
            col = int((i-1)/4+1)
            list[col].append(line[i])

for line in tmp2:
    count = 0
    f = 0
    t = 0
    tmp = 0
    line=line.split(" ")
    for c in line:
        if(c.isdigit() and tmp == 0):
            count = int(c)
            tmp +=1
        elif(c.isdigit() and tmp == 1):
            f = int(c)
            tmp += 1
        elif(c.isdigit() and tmp == 2):
            t = int(c)
            tmp += 1

    while(count!=0):
        count -= 1
        ele = list[f].pop(count) #part 1 pop(0), part 2 pop(count)
        list[t].insert(0, ele)

res = ""
for line in list[1:]:
    res += line[0]
print(res)


            
