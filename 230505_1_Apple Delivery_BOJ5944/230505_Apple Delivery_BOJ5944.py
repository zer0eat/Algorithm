# Apple Delivery_BOJ5944

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline
import heapq

# input 받기
C, P, PB, PA1, PA2 = map(int, input().split())          # C 길의 수 / P 목초지의 수 / PB 시작점 / PA1 배달지점 1 / PA2 배달지점 2
road = [[] for _ in range(P)]                           # 길의 정보를 저장할 리스트 생성
for p in range(C):                                      # 길의 수 만 큼 반복해서
    a, b, c = map(int, input().split())                 # a,b 목초지와 c 이동 비용을 input 받는다
    road[a-1].append([c, b-1])                          # a 목초지에서 이동할 수 있는 곳을 [비용, 연결 목초지]를 append
    road[b-1].append([c, a-1])                          # b 목초지에서 이동할 수 있는 곳을 [비용, 연결 목초지]를 append

def dijkstra(start):                                    
    distance = [1e9] * P                                # 목초지까지 이동 비용을 저장할 리스트 생성
    distance[start] = 0                                 # start 목초지까지 이동 비용을 0으로 저장
    tmp = [[0, start]]                                  # tmp에 [시작비용, 시작점]을 넣고 리스트 생성
    while tmp:                                          # tmp가 빌때까지 반복해서
        cost, node = heapq.heappop(tmp)                 # tmp에서 비용과 연결 목초지 정보를 heappop한다
        if cost > distance[node]:                       # cost가 현재 저장된 목초지 이동비용보다 크다면
            continue                                    # continue
        for r in road[node]:                            # 이동한 목초지에서 연결된 길를 반복해서
            cost2 = cost + r[0]                         # 현재까지 이동비용과 연결된 길의 비용을 더한값을 cost2에 저장하고
            if cost2 < distance[r[1]]:                  # cost2가 현재 저장된 비용보다 작다면
                distance[r[1]] = cost2                  # cost2를 저장비용으로 갱신한다
                heapq.heappush(tmp, [cost2, r[1]])      # tmp에 [이동비용, 길의 도착 목초지]로 heappush
    return distance                                     # distance를 return한다

A = dijkstra(PB-1)[PA1-1] + dijkstra(PA1-1)[PA2-1]      # PA1 지점을 들렸다가 PA2 지점을 가는 최소비용과
B = dijkstra(PB-1)[PA2-1] + dijkstra(PA2-1)[PA1-1]      # PA2 지점을 들렸다가 PA1 지점을 가는 최소비용을 저장한다
print(min(A,B))                                         # 두 값 중 최소비용을 출력한다