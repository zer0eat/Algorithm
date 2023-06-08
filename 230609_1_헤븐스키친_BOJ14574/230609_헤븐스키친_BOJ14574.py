# 헤븐스키친_BOJ14574

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline
import heapq
import math

# 함수
def find(node):
    if parents[node] == node:                           # key와 value가 같다면
        return node                                     # node를 그대로 return
    parents[node] = find(parents[node])                 # 다르다면 node의 value값으로 다시 find 함수를 통해 key, value가 같은 값이 되는 숫자를 찾아 value로 저장한다
    return parents[node]                                # 새로 저장된 value의 값을 return

def union(node1, node2):
    x = find(node1)                                     # node1이 key일 때 value 값을 x에 저장하고
    y = find(node2)                                     # node2가 key일 때 value 값을 y에 저장한다
    if x == y:                                          # x와 y가 같다면
        pass                                            # pass
    else:                                               # x와 y가 다르다면
        parents[y] = x                                  # x가 value y가 key가 되고

def DFS(cur_node):
    visited2[cur_node] = 1                              # 현재 요리사를 대결표시를 하고
    for next_node in battle[cur_node]:                  # 최대 시청률 대결정보에서 현재 요리사와 대결한 정보를 반복해서
        if visited2[next_node] == 0:                    # 상대 요리사가 대결 전이라면
            DFS(next_node)                              # DFS로 상대 요리사를 탐색한 후
            print(cur_node+1, next_node+1)              # 패자 요리사와 승자 요리사를 출력한다

# input 받기
N = int(input())                                        # 요리사의 수
road = [[] for _ in range(N)]                           # 요리사의 대결 정보를 저장할 리스트 생성
cooker = []                                             # 요리사의 인기도와 실력을 저장할 리스트 생성
for i in range(N):                                      # 요리사의 수를 반복해서
    P, C = map(int, input().split())                    # P 요리실력 / C 인기도를 input 받고
    for j in range(i):                                  # cooker에 저장된 요리사를 반복해서
        P2, C2 = cooker[j]                              # 대결 상대의 P2 요리실력 / C2 인기도를 저장하고
        rating = math.floor((C + C2) / abs(P - P2))     # 두 대결의 시청률을 구해서 rating에 저장한다
        road[i].append([-rating, j, i])                 # i 요리사와 대결정보에 [시청률, 대결요리사, i요리사]를 append
        road[j].append([-rating, i, j])                 # j 요리사와 대결정보에 [시청률, 대결요리사, j요리사]를 append
    cooker.append([P, C])                               # cooker 리스트에 현재 요리사의 [실력, 인기도]를 append

parents = dict()                                        # 집합을 저장할 딕셔너리를 생성하고
for i in range(N):                                      # N명의 요리사를 반복해서
    parents[i] = i                                      # key와 value가 같은 값이 되도록 딕셔너리에 원소를 생성한다
battle = [[] for _ in range(N)]                         # 최대 시청률 대결정보를 저장할 리스트 생성

ans = 0                                                 # 최대 시청률을 저장할 변수를 생성하고
visited = [0] * N                                       # 요리사의 대결 표시를 할 리스트 생성
tmp = [[0, 0, 0]]                                       # 시작점을 넣은 tmp 리스트를 생성
cnt = 0                                                 # 대결한 요리사를 카운트할 변수를 생성
while cnt < N:                                          # 대결한 요리사가 N명 모두 될 때까지 반복해서
    cost, node1, node2 = heapq.heappop(tmp)             # 시청률, 요리사1, 요리사2를 heappop해서 저장한 후
    if visited[node1] == 0:                             # 요리사1이 아직 대결 전이라면
        union(node1, node2)                             # 요리사1과 요리사2를 union함수를 통해 대결관계를 찾는다
        ans += cost                                     # ans에 시청률을 더해주고
        cnt += 1                                        # 대결한 요리사의 수를 1 더해준다
        visited[node1] = 1                              # 요리사1의 대결 표시를 해준다
        battle[node1].append(node2)                     # 최대 시청률 대결정보 리스트에 요리사1 원소에 요리사2 append
        battle[node2].append(node1)                     # 최대 시청률 대결정보 리스트에 요리사2 원소에 요리사1 append
        for r in road[node1]:                           # 요리사1과 대결 정보를 반복해서
            if visited[r[1]] == 0:                      # 요리사1과 대결할 상대가 아직 승부하기 전이라면
                heapq.heappush(tmp, r)                  # 대결정보를 tmp에 heappush한다

print(-ans)                                             # 최대 시청률을 출력한다
visited2 = [0] * N                                      # DFS 방문표시를 할 리스트를 생성하고
DFS(0)                                                  # 첫번째 요리사 부터 DFS 탐색한다