import numpy as np

def NW(x, y):
    return(x-1, y+1)

def N(x, y):
    return(x, y+1)

def NE(x, y):
    return(x+1, y+1)

def E(x, y):
    return(x+1, y)

def SE(x, y):
    return(x+1, y-1)

def S(x, y):
    return(x, y-1)

def SW(x, y):
    return(x-1, y-1)

def W(x, y):
    return(x-1, y)

DIR_CHECKS = [NW, N, NE, E, SE, S, SW, W]


SYMBOLS = ['+', '-', '*', '/', '=', '@', '#', '$', '%']
NUMS = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

with open("2023\inputs\input3.txt", 'r') as f:
    lines = f.readlines()

schem = []

for line in lines:
    schem.append(list(line[:-1:]))

schem = np.array(schem)

x_max, y_max = schem.shape

total = 0

for x in range(x_max):
    for y in range(y_max):
        if(schem[x][y] in SYMBOLS):
            for d in DIR_CHECKS:
                try:
                    x2, y2 = d(x, y)
                    value = int(schem[x2][y2])
                    if(value in NUMS):
                        total += value
                except:
                    continue

print(total)