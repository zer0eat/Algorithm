# 변신로봇_BOJ14630

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline
import heapq

# input 받기
N = int(input())                                # 변신 상태의 수
road = [[] for _ in range(N)]                   # 변신할 때 드는 비용을 저장할 리스트 생성
robot = []                                      # 변신 상태를 저장할 리스트 생성
for i in range(N):                              # 변신 상태의 수를 반복해서
    A = list(input().strip())                   # 변신 상태를 리스트로 input 받고
    for k, j in enumerate(robot):               # 변신 상태를 저장한 리스트를 반복해서
        tmp = 0                                 # 변신 비용을 저장할 변수 생성
        for x in range(len(A)):                 # 변신 상태를 반복해서
            tmp += (int(A[x]) - int(j[x]))**2   # 두 상태의 차의 제곱을 tmp에 더하고
        else:                                   # 변신 상태의 반복을 모두 마쳤다면
            road[i].append([tmp, k])            # i번째 상태에서 변신할 때 [비용, 변신상태를] append
            road[k].append([tmp, i])            # k번째 상태에서 변신할 때 [비용, 변신상태를] append
    robot.append(A)                             # robot 리스트에 현재 상태를 append
start, end = map(int, input().split())          # 변신 시작점과 끝점을 input 받는다

def dijkstra(start):
    distance = [1e9]*N                          # 최소 변신 비용을 저장할 리스트 생성
    distance[start] = 0                         # 현재 변신 상태를 0으로 저장
    tmp = [[0, start]]                          # tmp에 [비용, 현재상태]를 넣고 리스트 생성
    while tmp:                                  # tmp가 빌 때까지 반복해서
        cost, node = heapq.heappop(tmp)         # tmp에서 heappop해서 cost와 node를 저장
        if cost > distance[node]:               # heappop한 비용이 현재 node상태로 변신하는 비용보다 크다면
            continue                            # continue로 지나간다
        for r in road[node]:                    # node상태에서 변신할 수 있는 상태를 반복해서
            cost2 = cost + r[0]                 # cost2에 현재 비용과 변신 비용을 더해 저장한다
            if cost2 < distance[r[1]]:          # cost2가 r[1] 상태로 변신하는 저장된 비용보다 작다면
                distance[r[1]] = cost2          # cost2로 그 값을 갱신하고
                heapq.heappush(tmp, [cost2, r[1]])  # tmp에 [새로운 변신 비용, 변신 상태]를 heappush 한다
    return distance                             # 변신 비용을 return

print(dijkstra(start-1)[end-1])                 # 시작점에서 변신 비용을 dikstra로 찾아 end로 변신하는 비용을 출력한다
