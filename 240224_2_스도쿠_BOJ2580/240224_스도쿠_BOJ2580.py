# 스도쿠_BOJ2580

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
sudoku = [list(map(int, input().split())) for _ in range(9)]    # 채워야할 스도쿠를 input 받고
visited = [[0]*10 for _ in range(9)]                            # 가로에 1부터 9까지 있는지 확인할 리스트를 생성하고
visited2 = [[0]*10 for _ in range(9)]                           # 세로에 1부터 9까지 있는지 확인할 리스트를 생성하고
visited3 = [[0]*10 for _ in range(9)]                           # 정사각형에 1부터 9까지 있는지 확인할 리스트를 생성한다

def how(i, j):
    if 0<=i<3:                                                  # 행이 0부터 2라면
        if 0<=j<3:                                              # 열이 0부터 2라면
            return 0                                            # 0번째 정사각형이라고 return한다
        elif 3<=j<6:                                            # 행이 3부터 5라면
            return 1                                            # 1번째 정사각형이라고 return한다
        else:                                                   # 열이 6부터 8이라면
            return 2                                            # 2번째 정사각형이라고 return한다
    elif 3<=i<6:                                                # 행이 3부터 5라면
        if 0<=j<3:                                              # 열이 0부터 2라면
            return 3                                            # 3번째 정사각형이라고 return한다
        elif 3<=j<6:                                            # 행이 3부터 5라면
            return 4                                            # 4번째 정사각형이라고 return한다
        else:                                                   # 열이 6부터 8이라면
            return 5                                            # 5번째 정사각형이라고 return한다
    else:                                                       # 행이 6부터 8이라면
        if 0<=j<3:                                              # 열이 0부터 2라면
            return 6                                            # 6번째 정사각형이라고 return한다
        elif 3<=j<6:                                            # 행이 3부터 5라면
            return 7                                            # 7번째 정사각형이라고 return한다
        else:                                                   # 열이 6부터 8이라면
            return 8                                            # 8번째 정사각형이라고 return한다

for i in range(9):                                              # 행을 반복하고
    for j in range(9):                                          # 열을 반복해서
        if sudoku[i][j]:                                        # i,j에 숫자가 채워져 있다면
            visited[i][sudoku[i][j]] = 1                        # 가로에 해당숫자가 있다고 표시하고
            visited2[j][sudoku[i][j]] = 1                       # 세로에 해당숫자가 있다고 표시하고
            visited3[how(i,j)][sudoku[i][j]] = 1                # 정사각형에 해당숫자가 있다고 표시한다

def recur(depx, depy):
    if depx == 9 and depy == 0:                                 # 스도쿠의 모든 원소를 확인했다면
        for s in sudoku:                                        # 완성된 스도쿠의 행을 반복해서
            print(*s)                                           # 완성된 스도쿠를 출력하고
        quit()                                                  # 종료한다
    if sudoku[depx][depy]:                                      # depx, depy의 스도쿠가 채워 있다면
        if depy == 8:                                           # 열이 8에 위치에 있다면
            recur(depx+1, 0)                                    # 다음행 첫번째로 탐색한다
        else:                                                   # 열이 8에 위치에 없다면
            recur(depx, depy+1)                                 # 다음열로 탐색한다
    else:                                                       # depx, depy의 스도쿠가 채워져 있지 않다면
        for k in range(1, 10):                                  # 안에 넣을 숫자를 반복해서
            if visited[depx][k] or visited2[depy][k] or visited3[how(depx,depy)][k]:    # 가로 / 세로 / 정사각형에 k가 있다면
                continue                                        # continue로 넘어간다
            visited[depx][k] = True                             # 가로에 k 숫자가 들어갔다고 방문표시하고
            visited2[depy][k] = True                            # 세로에 k 숫자가 들어갔다고 방문표시하고
            visited3[how(depx, depy)][k] = True                 # 정사각형에 k 숫자가 들어갔다고 방문표시하고
            sudoku[depx][depy] = k                              # 스도쿠에 k를 적고
            if depy == 8:                                       # 열이 8에 위치에 있다면
                recur(depx + 1, 0)                              # 다음행 첫번째로 탐색한다
            else:                                               # 열이 8에 위치에 없다면
                recur(depx, depy + 1)                           # 다음열로 탐색한다
            sudoku[depx][depy] = 0                              # 스도쿠에 k를 지우고
            visited3[how(depx, depy)][k] = False                # 정사각형에 k 숫자가 들어갔다고 방문표시 해제하고
            visited2[depy][k] = False                           # 세로에 k 숫자가 들어갔다고 방문표시 해제하고
            visited[depx][k] = False                            # 가로에 k 숫자가 들어갔다고 방문표시 해제한다

recur(0, 0)                                                     # 0,0의 위치부터 스도쿠를 탐색한다