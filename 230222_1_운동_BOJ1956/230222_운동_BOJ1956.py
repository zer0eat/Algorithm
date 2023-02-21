# 운동_BOJ1956

# input.txt 열기
import sys
sys.stdin = open('input.txt')

def cycle(v):                                               
    global start, ans, tmp                                  # start 시작마을 / ans cycle의 최소거리 / tmp 현재 달리고 있는 거리를 global로 선언
    if ans < tmp:                                           # ans보다 tmp가 커지면 더이상 탐색할 필요가 없으므로
        return                                              # return
    if v == start:                                          # 시작마을로 다시 돌아왔다면 cycle이 완성됐으므로
        if ans > tmp:                                       # ans보다 tmp가 작은 경우에만
            ans = tmp                                       # ans를 tmp로 바꾼 후
        return                                              # return
    for j in range(V):                                      # 마을을 반복해서
        if visited[j] == 0:                                 # 방문 전인 마을이 나왔다면
            tmp += road[v][j]                               # j마을 까지 거리를 tmp에 저장하고
            visited[j] = 1                                  # j마을을 방문표시한 뒤
            cycle(j)                                        # cycle 함수에 j를 넣고 이후 경로를 찾아본다
            tmp -= road[v][j]                               # 이후 경로의 탐색을 마쳤다면, tmp에 j마을 까지 거리를 빼고
            visited[j] = 0                                  # j마을을 방문표시를 제거해서 j마을 방문 전으로 돌아간다
   
# input 받기
V, E = map(int, sys.stdin.readline().split())               # V 마을의 수 / E 도로의 수

road = [[int(1e9)]*V for _ in range(V)]                     # 도로의 거리를 저장할 행렬을 생성

for _ in range(E):                                          # 도로의 수를 반복해서
    a, b, c = map(int, sys.stdin.readline().split())        # a 시작마을 b 도착마을 c 거리를 input 받고
    road[a-1][b-1] = c                                      # road[시작마을][도착마을]에 거리를 저장한다

ans = int(1e9)                                              # cycle을 할 수 있는 최소거리를 저장할 변수를 생성하고
for v in range(V):                                          # 마을의 수를 반복해서
    visited = [0]*V                                         # 방문한 마을인지 기록할 리스트를 생성하고
    start = v                                               # 시작점인 v를 start에 저장한다
    tmp = 0                                                 # cycle의 거리를 저장할 변수를 생성하고
    for j in range(V):                                      # 시작점인 v에서 다른 마을을 살펴보고
        if visited[j] == 0:                                 # 방문하지 않은 마을 이라면
            tmp += road[v][j]                               # j마을 까지 거리를 tmp에 저장하고
            visited[j] = 1                                  # j마을을 방문표시한 뒤
            cycle(j)                                        # cycle 함수에 j를 넣고 이후 경로를 찾아본다
            tmp -= road[v][j]                               # 이후 경로의 탐색을 마쳤다면, tmp에 j마을 까지 거리를 빼고
            visited[j] = 0                                  # j마을을 방문표시를 제거해서 j마을 방문 전으로 돌아간다

if ans == int(1e9):                                         # ans가 처음 그대로라면
    print(-1)                                               # cycle이 안되므로 -1을 출력하고
else:                                                       # ans가 변했다면
    print(ans)                                              # ans를 출력한다