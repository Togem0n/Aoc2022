with open("6.txt") as f:
    lines = f.read().split("\n")
input = lines[0]
map = {}
cnt = 0

i = 0
while(cnt != 14): #part1 cnt!=4 part2 cnt!=14
    c = input[i]
    print(c)
    if c in map:
        tmp = map[c]
        map = {}
        # map[c] = i
        i = tmp
        # print("{}{}".format(i, c))
        cnt = 0
    elif c not in map:
        map[c] = i
        cnt += 1
    i += 1
    # print(cnt)
print(i)
        
    
    