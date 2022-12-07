with open("7.txt") as f:
    lines = f.read().split("\n")

# also tree?
map = {}
path = []
root = "/"
s = set()
cnt = 0
for i in range(len(lines)):
    line = lines[i]
    split = line.strip().split(" ")
    if "$ cd" in line:
        if split[2] == "..":
            path.pop()
        else:
            path.append(split[2])
    elif "$ ls" in line:
        j = i + 1
        cnt = 0
        while j < len(lines) and  lines[j][0] != "$":
            cnt += 1
            j += 1
    elif "dir " in line:
        continue
    else:
        # if calculate before
        if root.join(path) in s:
            continue
        size = int(split[0])
        for i in range(1, len(path)+1):
            cur_dir = root.join(path[:i])
            if cur_dir not in map:
                map[cur_dir] = size
            else:
                map[cur_dir] += size
        cnt -= 1
        if cnt == 0: s.add(root.join(path))
        
res = 0
for k, v in map.items():
    if v < 100000:
        res += v
print(res)

already_use = map[root]
# 7xxx - already + need_to_free = 3xxx
need_to_free = already_use - 70000000 + 30000000

res2 = 70000000
for k, v in map.items():
    if v >= need_to_free:
        res2 = min(res2, v)
# print(min)
print(res2)


