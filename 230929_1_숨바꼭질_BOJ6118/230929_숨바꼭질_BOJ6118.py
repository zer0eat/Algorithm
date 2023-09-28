# 숨바꼭질_BOJ6118

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline
import heapq

# input 받기
N, M = map(int, input().split())                # N 헛간의 개수 / M 길의 개수
road = [[] for _ in range(N)]                   # 연결된 길의 정보를 저장할 행렬을 생성하고
visited = [-1] * N                              # 방문표시를 할 리스트를 생성한다
for m in range(M):                              # 길의 개수를 반복해서
    s, e = map(int, input().split())            # 연결된 두 헛간을 input받고
    road[s-1].append(e-1)                       # s 인덱스의 리스트에 e를 append하고
    road[e-1].append(s-1)                       # e 인덱스의 리스트에 s를 append한다
lst = [[0, 0]]                                  # [시작점과 거리, 시작점]을 넣은 리스트를 생성하고
visited[0] = 0                                  # 시작점을 거리로 방문표시한다
while lst:                                      # lst가 빌때까지 반복해서
    cnt, num = heapq.heappop(lst)               # 시작지점과의 거리와 현재 헛간번호를 heappop한다
    for i in road[num]:                         # 현재 헛간과 연결된 길을 반복해서
        if visited[i] == -1:                    # 연결된 도착지가 방문 전이라면
            heapq.heappush(lst, [cnt+1, i])     # 출발지와 거리와 연결된 도착지를 lst에 heappush하고
            visited[i] = cnt+1                  # 출발지와 거리로 방문표시한다
ans, distance, same_distance = 0, 0, 0          # 숨어야하는 헛간 번호, 출발지와 거리, 같은 거리의 헛간의 수를 저장할 변수를 생성하고
for v in range(N):                              # 헛간의 개수를 반복해서
    if distance < visited[v]:                   # 현재 저장된 거리보다 더 먼 헛간이 나왔다면
        ans, distance, same_distance = v+1, visited[v], 1   # 숨어야하는 헛간 번호로 저장하고 출발지와 거리를 갱신한 후 같은거리 헛간을 1로 저장한다
    elif distance == visited[v]:                # 현재 저장된 거리와 같은 헛간이 나왔다면
        same_distance += 1                      # 같은 거리의 헛간의 수를 1 추가한다
print(ans, distance, same_distance)             # 헛간 번호, 헛간까지의 거리, 같은 거리를 갖는 헛간의 개수를 출력한다