with open("10.txt") as f:
    lines = f.read().strip().split("\n")
cycle = 0
x = 1
res = []
res.append(x)
ans = 0
def check():
    if cycle == 20 or cycle == 60 or cycle == 100 or cycle == 140 or cycle == 180 or cycle == 220:
        return True
    else:
        return False

for line in lines:
    if line == "noop":
        cycle += 1
        if check():
            ans += x * cycle
            # print(x * cycle)
        continue
    else:
        line = line.split(" ")
        num = int(line[1])
        # print(num)
        cycle += 1
        if check():
            ans += x * cycle
            # print(x * cycle)
        cycle += 1
        if check():
            ans += x * cycle
            # print(x * cycle)
        x += num
print(ans)

x = 1
cycle = 0
ans2 = []     
for line in lines:
    if line == "noop":
        if abs(x%40-cycle%40) <= 1:
            ans2.append('#')
        else:
            ans2.append('.')
        cycle += 1
        continue
    else:
        line = line.split(" ")
        num = int(line[1])
        # print(num)
        if abs(x%40-cycle%40) <= 1:
            ans2.append('#')
        else:
            ans2.append('.')
        cycle += 1
        if abs(x%40-cycle%40) <= 1:
            ans2.append('#')
        else:
            ans2.append('.')
        cycle += 1
        x += num

for i in range(0, len(ans2)):
    if ((i) % 40  == 0): print()
    print(ans2[i], end=" ")
    