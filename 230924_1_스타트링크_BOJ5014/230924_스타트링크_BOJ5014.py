# 스타트링크_BOJ5014

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline
import heapq

# input 받기
F, S, G, U, D = map(int, input().split())       # F 최고층 / S 출발층 / G 목적층 / U 올라갈 수 있는 높이 / D 내려갈 수 있는 높이
floor = [[0, S]]                                # 출발층을 넣은 리스트 생성하고
visited = [0] * (F+1)                           # 방문표시를 할 리스트 생성한다
visited[S] = 1                                  # 출발층을 방문표시하고
while floor:                                    # floor가 빌때까지 반복해서
    cnt, now = heapq.heappop(floor)             # 버튼을 누른 횟수와 현재층을 heappop해고
    if now == G:                                # 엘레베이터로 G층으로 이동할 수 있는 경우
        print(cnt)                              # 버튼을 누른 최솟값을 출력하고
        break                                   # while문을 break한다
    if now + U <= F and visited[now+U] == 0:    # 올라가는 층이 최고층보다 같거나 낮고 방문 전이라면
        heapq.heappush(floor, [cnt+1, now+U])   # 버튼을 누른 횟수와 이동층을 heappush한다
        visited[now+U] = 1                      # 올라가는 층에 방문표시를 한다
    if now - D > 0 and visited[now-D] == 0:     # 내려가는 층이 0층보다 크거나 방문 전이라면
        heapq.heappush(floor, [cnt+1, now-D])   # 버튼을 누른 횟수와 이동층을 heappush한다
        visited[now-D] = 1                      # 내려가는 층에 방문표시를 한다
else:                                           # 엘레베이터로 이동할 수 없을 경우에는
    print('use the stairs')                     # use the stairs을 출력한다