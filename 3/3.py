with open("3.txt") as f:
    line = f.read().strip().split("\n")
res = 0

for i in line:
    map = {}
    set1 = set()
    half = int(len(i)/2)
    for c in i[0:half]:
        if(c not in set1):
            set1.add(c)
            map[c] = 1
    for c in i[half:]:
        if(c in set1):
            if(c.islower()):
                res += ord(c) - ord("a") + 1
            elif(c.isupper()):
                res += ord(c) - ord("A") + 27
            break
print(res)


cnt = 0
ans = 0
map = {}
for l in line:
    s = set()
    for c in l:
        if (c not in map and c not in s):
            map[c] = 1
            s.add(c)
        if (c in map and c not in s):
            map[c] += 1
            s.add(c)
        
    cnt += 1

    if(cnt == 3):
        for k in map:
            if(map[k] == 3):
                if(k.islower()):
                    ans+= ord(k) - ord("a") + 1
                else:
                    ans+= ord(k) - ord("A") + 27
        map = {}
        cnt = 0
print(ans)

