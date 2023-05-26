# 슬슬 가지를 먹지 않으면 죽는다_BOJ27945

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline
import heapq

# input 받기
N, M = map(int, input().split())            # N 요리학원의 수 / M 길의 수
road = [[] for _ in range(N)]               # 길의 정보를 저장할 리스트 생성

for _ in range(M):                          # 길의 수를 반복해서
    a, b, c = map(int, input().split())     # a,b 요리학원의 정보와 c 여는 날을 input 받는다
    road[a-1].append([c, b-1])              # a 학원과 연결된 길을 저장할 리스트에 [여는날짜, 연결 학원]을 append
    road[b-1].append([c, a-1])              # b 학원과 연결된 길을 저장할 리스트에 [여는날짜, 연결 학원]을 append

ans = []                                    # 정답을 저장할 리스트 생성
cnt = 0                                     # 기억하고 있을 길의 수를 저장할 변수 생성
tmp = [[0,0]]                               # 시작점을 넣은 tmp 리스트를 생성하고
visited = [0] * N                           # 방문 기록을 저장할 리스트를 생성한다
while cnt < N:                              # cnt가 N이 될 때까지 반복해서
    cost, node = heapq.heappop(tmp)         # 여는날짜와 연결 학원을 heappop하고
    if visited[node] == 0:                  # 연결 학원이 방문 전이라면
        visited[node] = 1                   # 방문표시를 한 후
        ans.append(cost)                    # ans에 여는 날짜를 append 한다
        cnt += 1                            # cnt에 기억하고 있는 길의 수를 1 추가한다
        for r in road[node]:                # 연결 학원과 연결된 길을 반복해서
            if visited[r[1]] == 0:          # 그 도착지가 방문 전이라면
                heapq.heappush(tmp, r)      # tmp에 heappush 한다

ans.sort()                                  # ans를 오름차순 정렬해서
for i in range(N):                          # N개의 학원을 반복할 때
    if i == ans[i]:                         # i와 i일에 여는 학원을 갈 수 있는 길을 기억하고 있다면
        pass                                # pass하고
    else:                                   # i와 i일에 여는 학원이 일치하지 않는다면
        print(i)                            # 최대한 살 수 있는 날을 출력하고
        break                               # break 한다
else:                                       # 모든 길을 반복했다면
    print(i+1)                              # 최대한 살 수 있는 날을 출력한다