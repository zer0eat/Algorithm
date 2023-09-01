# 연료채우기_BOJ1826

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline
import heapq

# input 받기
N = int(input())                                                        # 주유소의 개수를 input 받고
gas_station = []                                                        # 주유소의 정보를 저장할 리스트를 생성한다
for _ in range(N):                                                      # 주유소의 개수를 반복해서
    heapq.heappush(gas_station, list(map(int, input().split())))        # 주유소의 위치와 주유소에서 충전할 수 있는 에너지를 리스트로 input 받아 heappush한다
end, energy = map(int, input().split())                                 # 도착지의 위치와 시작 에너지를 input 받고
cnt = 0                                                                 # 주유소를 최소로 방문해서 도착지까지 이동할 수 있는 횟수를 저장할 변수를 생성한다
heap = []                                                               # 주유소의 충전할 수 있는 에너지를 저장할 리스트를 생성하고
while energy < end:                                                     # energy가 도착지에 도착할 만큼 있지 않다면 반복해서
    while gas_station and gas_station[0][0] <= energy:                  # 주유소 리스트가 남아 있고 주유소 리스트의 가장 가까운 위치가 현재 에너지로 방문 가능하다면
        a, b = heapq.heappop(gas_station)                               # 방문하여 위치와 충전량을 heappop하고
        heapq.heappush(heap, [-b, a])                                   # heap 리스트에 [-충전량, 거리]로 heappush한다 
    if not heap:                                                        # heap이 비어있다면
        cnt = -1                                                        # 도착하지 못했으므로 cnt에 -1을 저장하고
        break                                                           # while문을 break한다
    b, a = heapq.heappop(heap)                                          # 방문한 주유소 중 가장 큰 충전량을 갖는 주유소를 heappop해서
    energy += -b                                                        # 에너지를 충전하고
    cnt += 1                                                            # 방문횟수를 1 증가시킨다
print(cnt)                                                              # 방문횟수를 출력한다