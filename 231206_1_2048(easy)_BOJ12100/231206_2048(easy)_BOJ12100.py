# 2048(easy)_BOJ12100

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline
from collections import deque

# input 받기
N = int(input())                                            # 보드의 크기를 input받고
game = [list(map(int,input().split())) for _ in range(N)]   # 보드에 놓인 블록의 정보를 input받은 후
tmp = deque([[0, game]])                                    # deque에 [이동횟수, 보드]를 넣어 생성하고
ans = 0                                                     # 가장 큰 블록을 저장할 변수를 생성한다

def move1(c, game):                                         # 왼쪽으로 이동하는 함수
    new = [[0]*N for _ in range(N)]                         # 이동 후 보드 정보를 저장할 리스트를 생성하고
    for i in range(N):                                      # 행을 반복하고
        cnt = 0                                             # 이동 후 블록의 열을 나타낼 변수를 생성하고
        visited = [0] * N                                   # 방문표시를 할 리스트를 생성한다
        for j in range(N):                                  # 열을 반복해서
            if visited[j] == 0 and game[i][j] != 0:         # j열이 방문 전이면서 블록이 있을 때
                if j == N-1:                                # i행의 마지막 블록이라면
                    new[i][cnt] = game[i][j]                # cnt열에 j열의 블록을 저장하고
                    visited[j] = 1                          # j열의 블록에 방문표시를 한 후
                    cnt += 1                                # 이동 후 블록을 가르키는 변수를 오른쪽으로 한 칸 이동한다
                else:                                       # i행의 마지막 블록이 아니라면
                    for k in range(1, N-j):                 # j열 이후의 블록을 반복해서
                        if game[i][j+k] != 0:               # j+k열의 블록이 있다면
                            if game[i][j] == game[i][j+k]:  # j열과 j+k열의 블록이 같을 때
                                new[i][cnt] = game[i][j]*2  # cnt번째 열에 합쳐진 블록을 저장하고
                                visited[j] = 1              # j열을 방문표시하고
                                visited[j+k] = 1            # 합쳐진 j+k열도 방문표시한 후
                                cnt += 1                    # 이동 후 블록을 가르키는 변수를 오른쪽으로 한 칸 이동한다
                            else:                           # j열과 j+k열의 블록이 다를 때
                                new[i][cnt] = game[i][j]    # cnt번째 열에 j열의 블록을 저장하고
                                visited[j] = 1              # j열을 방문표시하고
                                cnt += 1                    # 이동 후 블록을 가르키는 변수를 오른쪽으로 한 칸 이동한다
                            break                           # for문을 break한다
                    else:                                   # j열 이후에 블록이 없다면
                        new[i][cnt] = game[i][j]            # cnt번째 열에 j열의 블록을 저장하고
                        visited[j] = 1                      # j열을 방문표시하고
                        cnt += 1                            # 이동 후 블록을 가르키는 변수를 오른쪽으로 한 칸 이동한다
    tmp.append([c+1, new])                                  # 보드의 이동을 마쳤다면 deque에 [이동횟수+1, 이동후보드] 정보를 append한다

def move2(c, game):                                         # 오른쪽으로 이동하는 함수
    new = [[0]*N for _ in range(N)]                         # 이동 후 보드 정보를 저장할 리스트를 생성하고
    for i in range(N-1,-1,-1):                              # 행을 아래에서 위로 반복하고
        cnt = N-1                                           # 이동 후 블록의 열을 나타낼 변수를 생성하고
        visited = [0] * N                                   # 방문표시를 할 리스트를 생성한다
        for j in range(N-1,-1,-1):                          # 열을 오른쪽에서 왼쪽으로 반복해서
            if visited[j] == 0 and game[i][j] != 0:         # j열이 방문 전이면서 블록이 있을 때
                if j == 0:                                  # i행의 마지막 블록이라면
                    new[i][cnt] = game[i][j]                # cnt열에 j열의 블록을 저장하고
                    visited[j] = 1                          # j열의 블록에 방문표시를 한 후
                    cnt -= 1                                # 이동 후 블록을 가르키는 변수를 왼쪽으로 한 칸 이동한다
                else:                                       # i행의 마지막 블록이 아니라면
                    for k in range(1, j+1):                 # j열 이후의 블록을 반복해서
                        if game[i][j-k] != 0:               # j-k열의 블록이 있다면
                            if game[i][j] == game[i][j-k]:  # j열과 j-k열의 블록이 같을 때
                                new[i][cnt] = game[i][j]*2  # cnt번째 열에 합쳐진 블록을 저장하고
                                visited[j] = 1              # j열을 방문표시하고
                                visited[j-k] = 1            # 합쳐진 j-k열도 방문표시한 후
                                cnt -= 1                    # 이동 후 블록을 가르키는 변수를 왼쪽으로 한 칸 이동한다
                            else:                           # j열과 j-k열의 블록이 다를 때
                                new[i][cnt] = game[i][j]    # cnt번째 열에 j열의 블록을 저장하고
                                visited[j] = 1              # j열을 방문표시하고
                                cnt -= 1                    # 이동 후 블록을 가르키는 변수를 왼쪽으로 한 칸 이동한다
                            break                           # for문을 break한다
                    else:                                   # j열 이후에 블록이 없다면
                        new[i][cnt] = game[i][j]            # cnt번째 열에 j열의 블록을 저장하고
                        visited[j] = 1                      # j열을 방문표시하고
                        cnt -= 1                            # 이동 후 블록을 가르키는 변수를 왼쪽으로 한 칸 이동한다
    tmp.append([c+1, new])                                  # 보드의 이동을 마쳤다면 deque에 [이동횟수+1, 이동후보드] 정보를 append한다

def move3(c, game):                                         # 위쪽으로 이동하는 함수
    new = [[0]*N for _ in range(N)]                         # 이동 후 보드 정보를 저장할 리스트를 생성하고
    for j in range(N):                                      # 열을 반복하고
        cnt = 0                                             # 이동 후 블록의 행을 나타낼 변수를 생성하고
        visited = [0] * N                                   # 방문표시를 할 리스트를 생성한다
        for i in range(N):                                  # 행을 반복해서
            if visited[i] == 0 and game[i][j] != 0:         # i행이 방문 전이면서 블록이 있을 때
                if i == N-1:                                # j열의 마지막 블록이라면
                    new[cnt][j] = game[i][j]                # cnt행에 i행의 블록을 저장하고
                    visited[i] = 1                          # i행의 블록에 방문표시를 한 후
                    cnt += 1                                # 이동 후 블록을 가르키는 변수를 아래쪽으로 한 칸 이동한다
                else:                                       # j열의 마지막 블록이 아니라면
                    for k in range(1, N-i):                 # i행 이후의 블록을 반복해서
                        if game[i+k][j] != 0:               # i+k행의 블록이 있다면
                            if game[i][j] == game[i+k][j]:  # i행과 i+k행의 블록이 같을 때
                                new[cnt][j] = game[i][j]*2  # cnt번째 행에 합쳐진 블록을 저장하고
                                visited[i] = 1              # i행을 방문표시하고
                                visited[i+k] = 1            # 합쳐진 i+k행도 방문표시한 후
                                cnt += 1                    # 이동 후 블록을 가르키는 변수를 아래쪽으로 한 칸 이동한다
                            else:                           # i행과 i+k행의 블록이 다를 때
                                new[cnt][j] = game[i][j]    # cnt번째 행에 i행의 블록을 저장하고
                                visited[i] = 1              # i행을 방문표시하고
                                cnt += 1                    # 이동 후 블록을 가르키는 변수를 아래쪽으로 한 칸 이동한다
                            break                           # for문을 break한다
                    else:                                   # i행 이후에 블록이 없다면
                        new[cnt][j] = game[i][j]            # cnt번째 행에 i행의 블록을 저장하고
                        visited[i] = 1                      # i행을 방문표시하고
                        cnt += 1                            # 이동 후 블록을 가르키는 변수를 아래쪽으로 한 칸 이동한다
    tmp.append([c+1, new])                                  # 보드의 이동을 마쳤다면 deque에 [이동횟수+1, 이동후보드] 정보를 append한다

def move4(c, game):                                         # 아래쪽으로 이동하는 함수
    new = [[0]*N for _ in range(N)]                         # 이동 후 보드 정보를 저장할 리스트를 생성하고
    for j in range(N-1,-1,-1):                              # 열을 오른쪽에서 왼쪽으로 반복하고
        cnt = N-1                                           # 이동 후 블록의 행을 나타낼 변수를 생성하고
        visited = [0] * N                                   # 방문표시를 할 리스트를 생성한다
        for i in range(N-1,-1,-1):                          # 행을 아래에서 위로 반복해서
            if visited[i] == 0 and game[i][j] != 0:         # i행이 방문 전이면서 블록이 있을 때
                if i == 0:                                  # j열의 마지막 블록이라면
                    new[cnt][j] = game[i][j]                # cnt행에 i행의 블록을 저장하고
                    visited[i] = 1                          # i행의 블록에 방문표시를 한 후
                    cnt -= 1                                # 이동 후 블록을 가르키는 변수를 위쪽으로 한 칸 이동한다
                else:                                       # j열의 마지막 블록이 아니라면
                    for k in range(1, i+1):                 # i행 이후의 블록을 반복해서
                        if game[i-k][j] != 0:               # i-k행의 블록이 있다면
                            if game[i][j] == game[i-k][j]:  # i행과 i-k행의 블록이 같을 때
                                new[cnt][j] = game[i][j]*2  # cnt번째 행에 합쳐진 블록을 저장하고
                                visited[i] = 1              # i행을 방문표시하고
                                visited[i-k] = 1            # 합쳐진 i-k행도 방문표시한 후
                                cnt -= 1                    # 이동 후 블록을 가르키는 변수를 위쪽으로 한 칸 이동한다
                            else:                           # i행과 i-k행의 블록이 다를 때
                                new[cnt][j] = game[i][j]    # cnt번째 행에 i행의 블록을 저장하고
                                visited[i] = 1              # i행을 방문표시하고
                                cnt -= 1                    # 이동 후 블록을 가르키는 변수를 위쪽으로 한 칸 이동한다
                            break                           # for문을 break한다
                    else:                                   # i행 이후에 블록이 없다면
                        new[cnt][j] = game[i][j]            # cnt번째 행에 i행의 블록을 저장하고
                        visited[i] = 1                      # i행을 방문표시하고
                        cnt -= 1                            # 이동 후 블록을 가르키는 변수를 위쪽으로 한 칸 이동한다
    tmp.append([c+1, new])                                  # 보드의 이동을 마쳤다면 deque에 [이동횟수+1, 이동후보드] 정보를 append한다

while tmp:                                                  # tmp가 빌때가지 반복해서
    cnt, game = tmp.popleft()                               # deuqe에서 popleft해서 이동횟수와 보드를 꺼낸 후
    if cnt == 5:                                            # 이동횟수가 5회라면
        for g in game:                                      # 보드의 행을 반복해서
            ans = max(ans, max(g))                          # ans에 가장 큰 블록의 정보를 저장한다
    else:                                                   # 이동횟수가 5회 미만이라면
        move1(cnt, game)                                    # 블록을 왼쪽로 옮기는 함수를 실행하고
        move2(cnt, game)                                    # 블록을 오른쪽로 옮기는 함수를 실행하고
        move3(cnt, game)                                    # 블록을 위로 옮기는 함수를 실행하고
        move4(cnt, game)                                    # 블록을 아래로 옮기는 함수를 실행한다
else:                                                       # 5번 이동을 모두 마쳤다면
    print(ans)                                              # 가장 큰 블록의 정보를 출력한다