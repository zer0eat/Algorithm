# Median Tree_BOJ10661

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline
import heapq

# input 받기
while True:                                                     # N이 0이 될 때까지 반복해서
    N, M = map(int, input().split())                            # N 노드의 수 / M 간선의 수
    if N == 0:                                                  # N 노드의 수가 0 이면
        quit()                                                  # 종료한다
    road = [[] for _ in range(N)]                               # 간선의 정보를 저장할 리스트 생성
    for _ in range(M):                                          # 간선의 수를 반복해서
        a, b, c = map(int, input().split())                     # a,b 노드의 정보와 c 간선의 비용을 input 받고
        road[a-1].append([c, b-1])                              # a에 [비용, 도착 노드]를 append
        road[b-1].append([c, a-1])                              # b에 [비용, 도착 노드]를 append

    ans = []                                                    # 정답을 저장할 리스트 생성
    cnt = 0                                                     # 방문 노드의 수를 저장할 변수 생성
    visited = [0] * N                                           # 방문 표시를 할 리스트 생성
    tmp = [[0, 0]]                                              # 시작점을 넣고 리스트 새성
    while cnt < N:                                              # 방문지가 N개가 될때까지 반복해서
        cost, node = heapq.heappop(tmp)                         # 비용과 노드를 heappop한 후
        if visited[node] == 0:                                  # 해당 노드가 방문 전이라면
            visited[node] = 1                                   # 방문 표시를 하고
            ans.append(cost)                                    # ans에 비용을 append
            cnt += 1                                            # 방문지의 수를 1 더하고
            for r in road[node]:                                # 노드와 연결된 간선을 반복해서
                if visited[r[1]] == 0:                          # 간선의 도착지가 방문 전이라면
                    heapq.heappush(tmp, r)                      # tmp에 heappush 한다
    ans.sort()                                                  # ans를 오름차순 정렬하고
    print(ans[N//2])                                            # N//2번째 원소인 중앙값을 출력한다