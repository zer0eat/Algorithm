# 우주신과의교감_BOJ1774

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline
import math
import heapq

# input 받기
N, M = map(int, input().split())                                                    # N 우주신의 개수 / M 통로의 개수
road = dict()                                                                       # 우주신끼리 연결하는 선과 그 비용을 저장할 딕셔너리 생성
lst = [list(map(int, input().split())) for _ in range(N)]                           # 우주신의 좌표를 list형태로 input 받아 저장

for i in range(N):                                                                  # 우주신의 수만큼 반복하고
    for j in range(i+1, N):                                                         # i 우주신 다음부터 반복해서
        length = math.sqrt((lst[i][0]-lst[j][0])**2 + (lst[i][1]-lst[j][1])**2)     # 두 우주신의 간의 거리를 구해서
        if road.get(i) == None:                                                     # i 우주신이 key인 딕셔너리가 없다면
            road[i] = [[length, j]]                                                 # key가 i이고 value가 [두 우주신의 거리, 우주신j]인 딕셔너리를 생성한다
        else:                                                                       # i 우주신이 key인 딕셔너리가 있다면
            road[i].append([length, j])                                             # key가 i인 요소의 value에 [두 우주신의 거리, 우주신j]를 append
        if road.get(j) == None:                                                     # j 우주신이 key인 딕셔너리가 없다면
            road[j] = [[length, i]]                                                 # key가 j이고 value가 [두 우주신의 거리, 우주신i]인 딕셔너리를 생성한다
        else:                                                                       # j 우주신이 key인 딕셔너리가 있다면
            road[j].append([length, i])                                             # key가 j인 요소의 value에 [두 우주신의 거리, 우주신i]를 append

for _ in range(M):                                                                  # 이미 연결된 통로를 반복해서
    a, b = map(int, input().split())                                                # 통로로 연결된 우주신을 input 받고
    road[a-1].append([0, b-1])                                                      # a-1이 key인 우주신의 value에 거리가 0이고 도착 우주신인 b-1을 append
    road[b-1].append([0, a-1])                                                      # b-1이 key인 우주신의 value에 거리가 0이고 도착 우주신인 a-1을 append

visited = [0]*N                                                                     # 방문기록을 할 리스트를 생성하고
ans = 0                                                                             # 전체 비용을 저장할 변수를 생성하고
cnt = 0                                                                             # 방문한 우주신의 수를 저장할 변수를 생성한다

line = [[0,0]]                                                                      # 최소 가중치부터 탐색을 하기 위해 리스트를 생성하고 시작점([가중치 없음, 시작점])을 넣는다
while cnt < N:                                                                      # 모든 우주신을 방문할 때까지 반복해서
    length, end = heapq.heappop(line)                                               # line 리스트에서 우주신 간의 거리가 가장 작은 수를 heappop한다
    if not visited[end]:                                                            # 도착지의 우주신이 아직 연결 전이라면
        ans += length                                                               # ans에 우주신간의 거리를 추가하고
        visited[end] = 1                                                            # end 우주신을 방문표시한 뒤
        cnt += 1                                                                    # cnt에 방문한 우주신의 수를 1 추가한다
        for r in road[end]:                                                         # 도착지의 우주신과 연결된 road를 반복해서
            if visited[r[1]] == 0:                                                  # 다음 도착지의 우주신이 방문 전이라면
                heapq.heappush(line, r)                                             # line에 heappush한다

print(format(round(ans,2), ".2f"))                                                  # 모든 우주신이 연결됐다면 반올림해서 소수점 2째자리까지 출력한다