with open("9.txt") as f:
    lines = f.read().split("\n")
input = []
H = []
T = []
H.append(0)
H.append(0)
T.append(0)
T.append(0)

cnt = 0
s = set()

def adj():
    if abs(H[0] - T[0]) <= 1 and abs(H[1] - T[1]) <= 1:
        return True
    else:
        return False
    
for line in lines:
    line = line.split(" ")
    n = int(line[1])
    move = (0, 0)
    if line[0] == 'L': move = (-1,  0)
    if line[0] == 'R': move = ( 1,  0)
    if line[0] == 'U': move = ( 0,  1)
    if line[0] == 'D': move = ( 0, -1)
    while n != 0:
        n -= 1
        H[0] += move[0]
        H[1] += move[1]
        if not adj():
            if H[1] == T[1]:
                if H[0] - T[0] > 0: T[0] += 1
                elif H[0] - T[0] < 0: T[0] -= 1
            elif H[0] == T[0]:
                if H[1] - T[1] > 0: T[1] += 1
                elif H[1] - T[1] < 0: T[1] -= 1
            else:
                if H[0] - T[0] > 0: T[0] += 1
                elif H[0] - T[0] < 0: T[0] -= 1

                if H[1] - T[1] > 0: T[1] += 1
                elif H[1] - T[1] < 0: T[1] -= 1
        s.add((T[0], T[1]))
print(len(s))

s = set()
print(len(s))
H = [[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0]]
for line in lines:
    line = line.split(" ")
    n = int(line[1])
    move = (0, 0)
    if line[0] == 'L': move = (-1,  0)
    if line[0] == 'R': move = ( 1,  0)
    if line[0] == 'U': move = ( 0,  1)
    if line[0] == 'D': move = ( 0, -1)
    while n != 0:
        n -= 1
        H[0][0] += move[0]
        H[0][1] += move[1]
        
        for i in range(1, 10):
            
            diff_x = H[i-1][0] - H[i][0]
            diff_y = H[i-1][1] - H[i][1]

            if abs(diff_x) <= 1 and abs(diff_y) <= 1: continue
            # same row
            if diff_y == 0:
                if diff_x > 0: H[i][0] += 1
                elif diff_x < 0: H[i][0] -= 1
            #same col
            elif diff_x == 0:
                if diff_y > 0: H[i][1] += 1
                elif diff_y < 0: H[i][1] -= 1
            #
            else:
                if diff_x > 0: H[i][0] += 1
                elif diff_x < 0: H[i][0] -= 1

                if diff_y > 0: H[i][1] += 1
                elif diff_y < 0: H[i][1] -= 1
        s.add((H[9][0], H[9][1]))
print(len(s))
