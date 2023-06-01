# 촌수계산_BOJ2644

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline
import heapq

# input 받기
N = int(input())                                        # 사람의 수를 input 받고
start, end = map(int, input().split())                  # 촌수를 계산해야하는 두 사람을 input 받는다
M = int(input())                                        # 부모 관계의 수를 input 받고
road = [[] for _ in range(N)]                           # 부모 관계를 저장할 리스트를 생성하고
for _ in range(M):                                      # 부모 관계의 수를 반복해서
    a, b = map(int, input().split())                    # a,b에 부모와 자식을 input 받고
    road[a-1].append([1, b-1])                          # a에 [1촌, 연결사람]을 append
    road[b-1].append([1, a-1])                          # b에 [1촌, 연결사람]을 append

def dijkstra(start):
    tmp = [[0, start]]                                  # 시작사람을 넣은 리스트를 생성하고
    distance = [1e9] * N                                # 촌수를 계산할 리스트를 생성한다
    while tmp:                                          # tmp가 빌 때까지 반복해서
        cost, node = heapq.heappop(tmp)                 # 촌수와 연결된 사람을 heappop하고
        if cost > distance[node]:                       # 촌수가 저장된 촌수보다 크다면
            continue                                    # continue
        distance[node] = cost                           # 저장된 촌수를 현재 최소 촌수로 바꿔 저장하고 
        for r in road[node]:                            # 연결된 사람과 부모 자식관계를 반복해서
            cost2 = cost + r[0]                         # cost2에 해당 start와의 촌수를 저장한다
            if cost2 < distance[r[1]]:                  # cost2가 저장된 촌수보다 작다면
                heapq.heappush(tmp, [cost2, r[1]])      # tmp에 [촌수, 연결된 사람]을 heappush한다
    return distance                                     # while문이 끝나면 distance를 return

result = dijkstra(start-1)[end-1]                       # result에 start와 end의 촌수를 저장하고
if result == 1e9:                                       # 촌수가 갱신되지 않았다면
    print(-1)                                           # 가족이 아니므로 -1을 출력하고
else:                                                   # 촌수가 갱신되었다면
    print(result)                                       # 촌수를 출력한다