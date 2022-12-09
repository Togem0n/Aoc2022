data = open("9.txt").read().strip()
lines = [x for x in data.split('\n')]

def TailVisitedPositions():
    headPosition = [0,0]
    tailPosition = [0,0]
    visitedLocations = {(0,0)}

    for line in lines:
        move, count = line.split()
        count = int(count)

        possibleMoves = {'R':[1,0], 'L':[-1,0], 'D':[0,1], 'U':[0,-1]}
        for i in range(int(count)):
            headPosition[0] += possibleMoves[move][0]
            headPosition[1] += possibleMoves[move][1]

            x = tailPosition[0] - headPosition[0]
            y = tailPosition[1] - headPosition[1]

            if x == 2 and y == 0:
                tailPosition[0] -= 1
            elif x == -2 and y == 0:
                tailPosition[0] += 1
            
            elif y == 2 and x == 0:
                tailPosition[1] -= 1
            elif y == -2 and x == 0:
                tailPosition[1] += 1

            elif y == 2 and x == 1:
                tailPosition[0] -= 1
                tailPosition[1] -= 1
            elif y == -2 and x == 1:
                tailPosition[0] -= 1
                tailPosition[1] += 1

            elif y == -2 and x == -1:
                tailPosition[0] += 1
                tailPosition[1] += 1
            elif y == 2 and x == -1:
                tailPosition[0] += 1
                tailPosition[1] -= 1

            elif y == 1 and x == 2:
                tailPosition[0] -= 1
                tailPosition[1] -= 1
            elif y == -1 and x == 2:
                tailPosition[0] -= 1
                tailPosition[1] += 1

            elif y == -1 and x == -2:
                tailPosition[0] += 1
                tailPosition[1] += 1
            elif y == 1 and x == -2:
                tailPosition[0] += 1
                tailPosition[1] -= 1
            
            visitedLocations.add(tuple((tailPosition[0], tailPosition[1])))

    print("Unique visited positions: ", len(visitedLocations))

def LongerRope():
    headPosition = [[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0]]
    visitedLocations = {(0,0)}

    for line in lines:
        move, count = line.split()
        count = int(count)

        possibleMoves = {'R':[1,0], 'L':[-1,0], 'D':[0,1], 'U':[0,-1]}
        for i in range(int(count)):
            headPosition[0][0] += possibleMoves[move][0]
            headPosition[0][1] += possibleMoves[move][1]

            for j in range(1, 10):
                x = headPosition[j][0] - headPosition[j-1][0]
                y = headPosition[j][1] - headPosition[j-1][1]

                if x < -1 and y == 0:
                    headPosition[j][0] += 1
                elif x > 1 and y == 0:
                    headPosition[j][0] -= 1

                elif y < -1 and x == 0:
                    headPosition[j][1] += 1
                elif y > 1 and x == 0:
                    headPosition[j][1] -= 1

                elif y > 1 and x > 0:
                    headPosition[j][0] -= 1
                    headPosition[j][1] -= 1
                elif y < -1 and x > 0:
                    headPosition[j][0] -= 1
                    headPosition[j][1] += 1

                elif y < -1 and x < 0:
                    headPosition[j][0] += 1
                    headPosition[j][1] += 1
                elif y > 1 and x < 0:
                    headPosition[j][0] += 1
                    headPosition[j][1] -= 1

                elif y > 0 and x > 1:
                    headPosition[j][0] -= 1
                    headPosition[j][1] -= 1
                elif y < 0 and x > 1:
                    headPosition[j][0] -= 1
                    headPosition[j][1] += 1

                elif y < 0 and x < -1:
                    headPosition[j][0] += 1
                    headPosition[j][1] += 1
                elif y > 0 and x < -1:
                    headPosition[j][0] += 1
                    headPosition[j][1] -= 1

            visitedLocations.add(tuple((headPosition[9][0], headPosition[9][1])))

    print("Unique visited positions of rope of 10 knots: ", len(visitedLocations))

TailVisitedPositions()
LongerRope()