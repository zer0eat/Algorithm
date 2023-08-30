# 도시왕복하기2_BOJ2316

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline
from collections import deque

# input 받기
N, P = map(int, input().split())                        # N 도시의 수 / P 길의 수
city = N * 2                                            # 도시의 수를 두배로 늘려 입구와 출구의 수를 저장한다
capacity = [[0] * city for _ in range(city)]            # 노드(도시)의 유량을 저장할 리스트를 생성한다
road = [[] for _ in range(city)]                        # 도시의 연결 정보를 저장할 리스트를 생성한다

# 도시를 분할하여 들어오는 입구 in과 나가는 출구 out으로 나눈 후 연결해준다
for i in range(N):                                      # 도시의 수를 반복해서
    road[i].append(i + N)                               # 도시의 입구 i와 출구 i+N을 연결해주고
    road[i + N].append(i)                               # 도시의 출고 i+N과 입구 i를 연결해준다
    capacity[i][i + N] = 1                              # 도시의 in에서 out으로 이동하는 것을 1로 설정한다

# 길의 연결 정보를 저장한다
for _ in range(P):                                      # 길의 수를 반복해서
    a, b = map(int, input().split())                    # 연결된 도시의 정보를 input 받고
    a -= 1                                              # a 도시의 인덱스를 맞춰주기 위해 -1을 해주고
    b -= 1                                              # b 도시의 인덱스를 맞춰주기 위해 -1을 해준다
    road[a + N].append(b)                               # a 도시의 out에서 b 도시의 in으로 연결해주고
    road[b].append(a + N)                               # b 도시의 in에서 a 도시의 out으로 연결해준다
    capacity[a + N][b] = 1                              # 도시에 한번 밖에 방문하지 못하므로 용량을 1로 저장한다
    road[b + N].append(a)                               # 양방향 길이기 때문에 b 도시의 out에서 a 도시의 in으로 연결해주고
    road[a].append(b + N)                               # a 도시의 in에서 b 도시의 out으로 연결해준다
    capacity[b + N][a] = 1                              # 도시에 한번 밖에 방문하지 못하므로 용량을 1로 저장한다

flow = [[0] * city for _ in range(city)]                # 길의 유량(방문표시)를 할 리스트를 생성하고
start = N                                               # 1번에서 2번을 왕복해야하므로 출발지를 1번의 out으로 저장하고
end = 1                                                 # 도착지를 2번의 in으로 저장하다
ans = 0                                                 # 최대 왕복 횟수를 저장할 변수를 생성한다

while True:                                             # 최대 왕복 횟수를 찾을 때까지 반복해서
    prev = [-1] * city                                  # 현재 위치 이전 상태를 저장할 리스트를 생성하고
    q = deque([start])                                  # 출발 위치를 넣은 deque를 생성한다
    while q:                                            # q가 빌때까지 반복해서
        node = q.popleft()                              # 현재 위치를 q에서 popleft해서 저장한다
        if node == end:                                 # 현재 위치가 도착지라면
            break                                       # q while문을 break한다
        for next in road[node]:                         # 현재위치가 도착지가 아니라면 현재위치에서 갈 수 있는 곳을 반복해서
            if capacity[node][next] - flow[node][next] > 0: # Ture // capacity[node][next] node에서 next로 가는 경로가 있으면서 / flow[node][next] 아직 그 길을 방문하지 않았다면
                if prev[next] == -1:                    # 다음 갈 곳의 방문 기록이 없는 상태라면
                    prev[next] = node                   # 다음 갈 곳의 방문 기록에 현재 위치를 저장하고
                    q.append(next)                      # q에 다음 방문할 곳을 append 한다
    if prev[end] == -1:                                 # q가 비었는데 end에 방문하지 못했다면 더 이상 갈 수 있는 경로가 없으므로
        break                                           # True while문을 break한다

    node = end                                          # 현재 위치를 2번 출구로 저장하고
    while node != start:                                # 현재 위치가 출발지가 될때까지 반복해서
        flow[prev[node]][node] += 1                     # 현재 이전 위치 => 현재 위치로 이동한 수를 1 더해주고
        flow[node][prev[node]] -= 1                     # 현재 위치 => 현재 이전 위치로 이동한 수를 1 빼주고
        node = prev[node]                               # 현재 위치를 이전 위치로 바꿔 저장한다
    ans += 1                                            # 출발지에 도착했다면 왕복횟수를 1 증가시킨다
print(ans)                                              # 최대 왕복 횟수를 출력한다
