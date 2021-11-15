# sudoku

import sys

lst = []
zero = []
for i in range(9):
    lst.append(list(map(int, sys.stdin.readline().split())))
for i in range(9):
    for j in range(9):
        if lst[i][j] == 0:
            zero.append((i, j))
cnt = len(zero)

def solve(dep):
    if dep == cnt:
        for i in lst:
            for j in i:
                sys.stdout.write(str(j)+' ')
            sys.stdout.write('\n')
        sys.exit(0)
    for i in range(1, 10):
        now_x, now_y = zero[dep][0], zero[dep][1]
        if vaild(now_x, now_y, i): # back tracking
            lst[now_x][now_y] = i
            solve(dep+1)
            lst[now_x][now_y] = 0

def vaild(x, y, a):
    if a in lst[x]: # check1
        return False
    for i in range(9): # check2
        if lst[i][y] == a:
            return False
    for i in range(3): # check3
        for j in range(3):
            if lst[(x//3)*3+i][(y//3)*3+j] == a:
                return False
    return True 

if __name__ == "__main__": 
    solve(0)
