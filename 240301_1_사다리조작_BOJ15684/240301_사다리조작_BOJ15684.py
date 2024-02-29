# 사다리조작_BOJ15684

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
N, M, H = map(int, input().split())             # N 세로선의 수 / M 가로선의 개수 / H 가로선을 놓을 수 있는 행을 input 받고
sadari = [[0]*N for _ in range(H)]              # 사다리를 리스트로 만들어 준 후
for m in range(M):                              # 가로선의 수를 반복해서
    a, b = map(int, input().split())            # 가로선의 위치를 input 받고
    sadari[a-1][b-1] = 1                        # 가로선을 리스트에 표시한다
ans = 4                                         # 추가해야하는 가로선의 수를 저장할 변수를 생성한다

def line():
    for j in range(N):                          # 열을 반복해서
        p = j                                   # p에 현재 위치를 저장하고
        for i in range(H):                      # 행을 반복해서
            if sadari[i][p]:                    # i,p에 가로선이 있다면
                p += 1                          # 오른쪽으로 한칸 이동하고
            elif p != 0 and sadari[i][p-1]:     # i,p-1에 가로선이 있다면
                p -= 1                          # 왼쪽으로 한칸 이동한다
        if p != j:                              # 출발점과 도착점이 같은 열이 아니라면
            return False                        # False를 return한다
    return True                                 # 모든 열이 같은 열에 도착한다면 True를 return한다

def recur(dep, i, j):
    global ans                                  # ans를 global 변수로 선언하고
    if line():                                  # line 함수로 출발점과 도착점이 같다면
        ans = min(ans, dep)                     # ans와 추가한 사다리의 수 중 작은 값을 ans에 저장하고
        return                                  # reuturn한다
    if dep == 3 or ans <= dep:                  # 추가한 사다리가 3개이거나 ans 이상이라면
        return                                  # 이후 사다리를 추가하면 정답이 될 수 없으므로 return한다
    for x in range(i, H):                       # i부터 행을 반복해서
        if x == i:                              # i번째 행이라면
            start = j                           # j부터 가로선을 탐색하고
        else:                                   # i번째 행이아니라면
            start = 0                           # 0부터 가로선을 탐색한다
        for y in range(start, N-1):             # start부터 열을 반복해서
            if sadari[x][y]:                    # 해당 행렬에 가로선이 있다면
                continue                        # continue로 넘어가고
            if y > 0 and sadari[x][y-1]:        # 앞 열에 가로선이 있다면
                continue                        # continue로 넘어가고
            if sadari[x][y+1] == 0:             # 다음열에 가로선이 없다면
                sadari[x][y] = 1                # 가로선을 추가하고
                recur(dep + 1, x, y + 1)        # dep+1 깊이 x,y+1 부터 가로선을 탐색한다
                sadari[x][y] = 0                # 가로선을 제거한다

recur(0,0,0)                                    # 0 깊이 0,0 위치부터 가로선을 탐색한다
if ans > 3:                                     # 정답이 3 초과라면
    print(-1)                                   # -1을 출력하고
else:                                           # 정답이 3 이하라면
    print(ans)                                  # 추가해야 하는 가로선 개수의 최솟값을 출력한다