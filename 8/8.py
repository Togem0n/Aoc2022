with open("8.txt") as f:
    lines = f.read().split("\n")
input = []
for line in lines:
    input.append(line)

cnt = 0
for i in range(1, len(lines)-1):
    line = lines[i]
    for j in range(1, len(line)-1):
        height = int(line[j])
        flag_l = False
        flag_r = False
        flag_b = False
        flag_t = False

        for tmp_i in range(0, len(lines)):
            if tmp_i == i: continue
            cmp_height = int(lines[tmp_i][j])
            if cmp_height >= height and tmp_i < i and flag_l == False:
                flag_l = True
            if cmp_height >= height and tmp_i > i and flag_r == False:
                flag_r = True

        for tmp_j in range(0, len(line)):
            if tmp_j == j: continue
            cmp_height = int(lines[i][tmp_j])
            if cmp_height >= height and tmp_j < j and flag_t == False:
                flag_t = True
            if cmp_height >= height and tmp_j > j and flag_b == False:
                flag_b = True
        
        if flag_l and flag_r and flag_t and flag_b:
            cnt += 1

total = len(lines) * len(lines[0])
outer = 2 * len(lines) + 2 * len(lines[0]) - 4
middle = (len(lines) - 2) * (len(lines[0]) -2)
# print(total)
# print(middle)
# print(cnt)
print(outer + middle - cnt)
print("###")
res = 0
for i in range(0, len(lines)):
    line = lines[i]
    for j in range(0, len(line)):
        height = int(lines[i][j])
        left = i
        right = len(lines) - i
        top = j
        down = len(line) - j
        cnt_l = 0
        cnt_r = 0
        cnt_t = 0
        cnt_d = 0
        if left != 0:
            for tmp_l in range(1, left + 1):
                cmp_height = int(lines[i - tmp_l][j])
                if cmp_height < height:
                    cnt_l += 1
                else:
                    cnt_l += 1
                    break
        if right != 0:
            for tmp_r in range(1, right):
                cmp_height = int(lines[i + tmp_r][j])
                if cmp_height < height:
                    cnt_r += 1
                else:
                    cnt_r += 1
                    break

        if top != 0:
            for tmp_t in range(1, top + 1):
                cmp_height = int(lines[i][j - tmp_t])
                if cmp_height < height:
                    cnt_t += 1
                else:
                    cnt_t += 1
                    break
        if down != 0:
            for tmp_d in range(1, down):
                cmp_height = int(lines[i][j + tmp_d])
                if cmp_height < height:
                    cnt_d += 1
                else:
                    cnt_d += 1
                    break
        if cnt_l == 0: cnt_l = 1
        if cnt_r == 0: cnt_r = 1
        if cnt_t == 0: cnt_t = 1
        if cnt_d == 0: cnt_d = 1

        # print(cnt_l * cnt_r * cnt_t * cnt_d)
        res = max(res, cnt_l * cnt_r * cnt_t * cnt_d)
print(res)
                