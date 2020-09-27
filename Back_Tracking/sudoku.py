'''
스도쿠를 푸는 알고리즘

1. 먼저 풀고자 하는 스도쿠의 숫자를 한 줄씩 입력받는다.
이때, 빈칸은 0으로 입력한다.
입력받은 숫자들은 lst에 2차원 배열의 형태로 저장된다.

2. lst를 함수 solve()에 인자로 전달한다.

3. solve()에서는 먼저 함수 find()를 호출하는데,
함수 find()는 lst[0][0]에서부터 순차 탐색하여 0의 위치를 반환한다.

4. 그다음으로 실행되는 for 루프 내에서
함수 valid()에 1~9의 수(a)를 인자로 전달하는데,
valid(lst, i, j, a)는 스도쿠의 규칙을 따르는지 확인을 해준다.
valid() 함수 내부에서는 먼저 현재 행에 a가 존재하는지 확인하고,
존재하지 않는다면 현재 열에 a가 존재하는지 확인하고,
존재하지 않는다면 a가 포함되어 있는 3x3 격자판 내에 a가 하나 더 있는지 확인한다.
이러한 과정을 거쳐 스도쿠의 규칙을 따른다는 것이 확인되면 True를 반환한다.

5. 다시 solve() 함수로 와서, 현재 위치의 수를 a로 변경한다.
그리고 solve() 함수를 재귀 호출하여 스도쿠의 규칙을 위반하는 경우가 발생한다면,
변경한 a를 다시 0으로 초기화한다.

6. 탐색을 거친 후 스도쿠의 빈칸이 모두 채워진다면,
find()에서는 -1, -1을 반환하고,
solve()에서는 True를 반환하며 함수 실행을 종료한다.

7. 해결된 스도쿠를 출력한다.

제가 작성한 이 코드는 0의 개수가 많아질수록 시간이 오래 걸린다는 단점이 있습니다(언어적인 단점도 있고요).
따라서 이 코드는 대학 학부생 수준의 코드이며, 스도쿠를 푸는 최적의 알고리즘이 아님을 알려드립니다.

- SnapFlip20 -
'''

import sys

def solve(lst, i=0, j=0):
    i, j = find(lst) # 0의 위치 탐색

    if i == -1: # 0이 없을 때(스도쿠를 풀었을 때)
        return True

    for a in range(1, 10):
        if valid(lst, i, j, a): # 스도쿠의 규칙을 따르는 지 확인
            lst[i][j] = a # 규칙을 따른다면 수 변경
            if solve(lst, i, j): # 재귀 탐색
                return True
    lst[i][j] = 0 # 규칙을 위반했을 시 다시 0으로 변경
    return False

def find(lst): # 0의 위치 탐색
    for b in range(0, 9):
        for c in range(0, 9):
            if lst[b][c] == 0:
                return b, c
    return -1, -1 # 0이 없으면

def valid(lst, i, j, a): # a가 포함된 행, 열, 격자판 내에 동일한 수가 존재하는지 확인
    row_check = all([a != lst[i][x] for x in range(9)])    
    if row_check: # 현재 행에 a가 있는가?
        col_check = all([a != lst[x][j] for x in range(9)])
        if col_check: # 현재 열에 a가 있는가?
            x_ct, y_ct = 3*(i//3), 3*(j//3) # a가 포함되어 있는 3x3 격자판 범위
            for x in range(x_ct, x_ct+3):
                for y in range(y_ct, y_ct+3):
                    if lst[x][y] == a: # 3x3 격자판 내에 a가 있으면
                        return False
            
            return True # 모든 검사를 통과했을 때   

    return False # 검사를 통과하지 못했을 때

def main():
    lst = []
    for i in range(9):
        num_row = list(map(int, sys.stdin.readline().rstrip().split()))
        lst.append(num_row)

    solve(lst)
    
    for x in range(9):
        print(*lst[x])

if __name__ == "__main__":
    main()
