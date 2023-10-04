# 숨바꼭질 3_BOJ13549

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline
import heapq

# input 받기
N, K = map(int, input().split())                                # N 수빈이의 위치 / K 동생의 위치를 input 받고
visited = [0]*100001                                            # 방문표시를할 리스트를 생성한다
lst = [[0, N]]                                                  # 이동시간과 시작점을 넣은 리스트를 만들고
visited[N] = 1                                                  # 시작점을 방문표시한다
while lst:                                                      # lst가 빌때까지 반복해서
    cnt, num = heapq.heappop(lst)                               # 이동시간과 이동위치를 heappop해서
    if num == K:                                                # num이 K이면
        print(cnt)                                              # 이동시간을 출력하고
        break                                                   # while문을 break한다
    tmp = []                                                    # 이동한 위치를 담을 리스트를 생성하고
    if num < K and 0<=num+1<=100000 and visited[num+1] == 0:    # 이동한 곳이 K보다 작고 0과 100000 사이의 수면서 방문 전이라면
        heapq.heappush(lst, [cnt+1, num+1])                     # 이동시간과 이동위치를 heappush하고
        tmp.append(num+1)                                       # tmp에 이동한 위치를 append한다
    if 0<=num-1<=100000 and visited[num-1] == 0:                # 이동한 곳이 0과 100000 사이의 수면서 방문 전이라면
        heapq.heappush(lst, [cnt+1, num-1])                     # 이동시간과 이동위치를 heappush하고
        tmp.append(num-1)                                       # tmp에 이동한 위치를 append한다
    if num < K and 0<=num*2<=100000 and visited[num*2] == 0:    # 이동한 곳이 K보다 작고 0과 100000 사이의 수면서 방문 전이라면
        heapq.heappush(lst, [cnt, num*2])                       # 이동시간과 이동위치를 heappush하고
        tmp.append(num*2)                                       # tmp에 이동한 위치를 append한다
    for t in tmp:                                               # tmp를 반복해서
        visited[t] = 1                                          # 방문표시를 한다