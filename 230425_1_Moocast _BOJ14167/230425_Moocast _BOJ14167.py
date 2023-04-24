# Moocast _BOJ14167

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline
import heapq

# input 받기
N = int(input())                        # 젖소의 수
cows = []                               # 젖소의 좌표를 저장할 리스트 생성
road = [[] for _ in range(N)]           # 젖소 간의 연결비용과 연결 젖소를 저장할 리스트 생성
for i in range(N):                      # 젖소의 수를 반복해서
    x, y = map(int, input().split())    # 젖소의 위치를 x,y에 input 받는다
    for j in range(len(cows)):          # 저장된 젖소의 위치를 반복해서
        cost = (x-cows[j][0])**2 + (y-cows[j][1])**2    # 두 젖소의 거리의 제곱을 비용으로 저장하고
        road[i].append([cost, j])       # road의 i인덱스에 [비용, 연결할 젖소]를 append
        road[j].append([cost, i])       # road의 j인덱스에 [비용, 연결할 젖소]를 append
    cows.append([x, y])                 # cows 리스트에 젖소의 위치를 리스트형태로 append

ans = 0                                 # 정답을 저장할 변수 생성
tmp = [[0, 0]]                          # 리스트 안에 [비용, 출발점]을 넣고 생성
visited = [0] * N                       # 방문표시를 할 리스트 생성
cnt = 0                                 # 카운트를 할 리스트 생성
while cnt < N:                          # cnt가 N이 될 때까지 반복해서
    cost, node = heapq.heappop(tmp)     # tmp에서 heappop해서 cost와 node를 저장한다
    if visited[node] == 0:              # 연결할 node가 0이라면
        if ans < cost:                  # ans가 cost보다 작을 때
            ans = cost                  # ans에 cost를 저장하고
        visited[node] = 1               # node를 방문표시한 후
        cnt += 1                        # cnt를 1 추가한다
        for r in road[node]:            # node와 연결된 젖소들을 반복해서
            if visited[r[1]] == 0:      # 해당 젖소가 방문 전이라면
                heapq.heappush(tmp, r)  # tmp에 heapppush한다
print(ans)                              # 최소 연결 트리 중 가장 최소값을 출력한다