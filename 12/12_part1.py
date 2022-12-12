from heapq import *
with open("12.txt") as f:
    lines = f.read().strip().split("\n")

map = []
sx = 0
sy = 0
ex = 0
ey = 0
for i in range(len(lines)):
    map.append(lines[i])
    for j in range(len(lines[i])):
        if lines[i][j] == 'S':
            sx = i
            sy = j
        if lines[i][j] == 'E':
            ex = i
            ey = j
    # print(lines[i])
v = []
heappush(v, (0, sx, sy))
cnt = 0
visit = []
step = {}
# visit.append((sx, sy))
while len(v) != 0:
    # cnt += 1
    cnt, x, y = heappop(v)

    if (x, y) in visit: 
        continue
    visit.append( (x, y) )
    if lines[x][y] == 'E': 
        print("nmsl")
        break
    # x = tmp[0]
    # y = tmp[1]
    # print(lines[x][y])
    pre = 0
    if lines[x][y] == 'S': pre = ord('a')
    else: pre = ord(lines[x][y])
    # up
    if x - 1 >= 0:
        if lines[x-1][y] == 'E': next = ord('z')
        else: next = ord(lines[x-1][y])
        if next - pre <= 1:
            heappush(v, (cnt+ 1, x-1, y))
    # down
    if x + 1 <= len(lines) - 1:
        if lines[x+1][y] == 'E': next = ord('z')
        else: next = ord(lines[x+1][y])
        if next - pre <= 1:
            heappush(v, (cnt + 1, x+1, y))
    # left
    if y - 1 >= 0:
        if lines[x][y-1] == 'E': next = ord('z')
        else: next = ord(lines[x][y-1])
        if next - pre <= 1:
            heappush(v, (cnt+ 1, x, y-1))
    # right
    if y + 1 <= len(lines[0]) - 1:
        if lines[x][y+1] == 'E': next = ord('z')
        else: next = ord(lines[x][y+1])
        if next - pre <= 1:
            heappush(v, (cnt+ 1, x, y+1))
    
print(cnt)
    
