with open("test.txt") as f:
    line = f.read().strip().split("\n")

input = []

res = 0
score = [3, 0, 6]
cnt = 0
for i in line:
    # offset 0 1 2, me - you - offset = 0,-1,-2 map 3 0 6
    first = ord(i[2]) - 87 # 1 2 3                  6 3 0
    me = ord(i[2]) - 23 # 65 66 67                  0 6 3
    you = ord(i[0])     # 65 66 67
    offset = me - 65;   # 0  1  2
    second = 0
    if (me - you - offset) == 0:
        second = score[(0 - offset)]
    elif (me - you - offset) ==  -1:
        second = score[(1 - offset)]
    elif (me - you - offset) == -2:
        second = score[(2 - offset)]
    res += first
    res += second
    cnt += 1

print(res)

ans = 0
score2 = [3, 1, 2] # lose draw win
for i in line:
    # offset 0 1 2, me - you - offset = 0,-1,-2 map 3 0 6
    me = ord(i[2])
    first = (me - ord("X")) * 3 # 0 3 6

    second = 0
    you = ord(i[0]) # 65 66 67  0 3 6 -> 3 1 2
                                      #  1 2 3
                                       # 2 3 1
    offset = you - ord("A") # 0 1 2 
    if(me == ord("X")):
        second = score2[(0 + offset)%3]
    if(me == ord("Y")):
        second = score2[(1 + offset)%3]
    if(me == ord("Z")):
        second = score2[(2 + offset)%3]
    ans += first
    ans += second

print(ans)

