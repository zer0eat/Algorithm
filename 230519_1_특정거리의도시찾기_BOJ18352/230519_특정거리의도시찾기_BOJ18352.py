# 특정거리의도시찾기_BOJ18352

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline
import heapq

# input 받기
N, M, K, X = map(int, input().split())              # N 도시의 수 / M 도로의 수 / K 거리정보 / X 출발 번호
road = [[] for _ in range(N)]                       # 도로의 정보를 저장할 리스트 생성
for _ in range(M):                                  # 도로의 수를 반복해서
    a, b = map(int, input().split())                # a,b 도시를 input 받고
    road[a-1].append([1, b-1])                      # a-1에 [거리, 연결도시] 정보를 append

def dijkstra(start):
    distance = [1e9] * N                            # 거리를 저장할 리스트를 생성하고
    distance[start] = 0                             # start의 거리를 0으로 저장한다
    tmp = [[0, start]]                              # tmp에 시작점을 넣고 리스트를 생성한 후
    while tmp:                                      # tmp가 빌때까지 반복한다
        cost, node = heapq.heappop(tmp)             # 거리와 연결 도시를 heappop한 후
        if cost > distance[node]:                   # cost가 저장된 거리보다 큰 경우에는
            continue                                # continue 해서 넘어가고
        for r in road[node]:                        # 연결 도시와 이어진 도로를 반복해서
            cost2 = cost + r[0]                     # cost2에 현재 거리와 도로를 지나는 거리를 더한 후
            if cost2 < distance[r[1]]:              # cost2가 도로의 도착지에 저장된 거리보다 작다면
                distance[r[1]] = cost2              # 도착지의 거리를 cost2로 바꾸고
                heapq.heappush(tmp, [cost2, r[1]])  # tmp에 [cost2, 도착지 도시]를 heappush한다
    return distance                                 # start에서 각 도시까지 거리를 return

result = dijkstra(X-1)                              # X에서 출발해서 도착하는데 드는 거리를 result에 저장하고
ans = []                                            # 답을 저장할 리스트 생성
for r in range(N):                                  # 도시의 수를 반복해서
    if result[r] == K:                              # 도시간 거리가 K와 같다면
        ans.append(r+1)                             # ans에 해당 도시를 append
if ans:                                             # ans가 비어있지 않다면
    ans.sort()                                      # 오름차순 정렬하고
    for a in ans:                                   # ans를 반복해서
        print(a)                                    # 하나씩 출력한다
else:                                               # ans가 비어있다면
    print(-1)                                       # -1을 출력한다