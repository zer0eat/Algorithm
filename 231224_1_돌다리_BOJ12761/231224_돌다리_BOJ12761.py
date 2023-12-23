# 돌다리_BOJ12761

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline
import heapq

# input 받기
A, B, N, M = map(int, input().split())                  # 스카이 콩콩의 힘 A,B / N 동규의 위치 / M 주미의 위치를 input 받고
visited = [0]*100001                                    # 방문표시를할 리스트를 생성한 후
tmp = [[0, N]]                                          # 이동위치를 저장할 리스트에 동규의 위치를 넣어 생성한다
while 1:                                                # 종료될 때까지 반복해서
    cnt, now = heapq.heappop(tmp)                       # tmp에서 heappop하여 이동횟수와 위치를 저장하고
    if now == M:                                        # 주미에게 도착했다면
        print(cnt)                                      # 이동횟수를 출력하고
        quit()                                          # 종료한다
    if now < M:                                         # 주미의 위치보다 현재 위치가 더 오른쪽에 있다면
        if 0 <= now+1 <= 100000 and visited[now+1]==0:  # 한칸 오른쪽으로 이동한 위치가 이동 범위 내에 있으면서 방문 전이라면
            heapq.heappush(tmp, [cnt+1, now+1])         # tmp에 [이동횟수+1, 이동한 위치]를 heappush한 후
            visited[now+1] = 1                          # 방문표시를 한다
        if 0 <= now+A <= 100000 and visited[now+A]==0:  # A칸 오른쪽으로 이동한 위치가 이동 범위 내에 있으면서 방문 전이라면
            heapq.heappush(tmp, [cnt+1, now+A])         # tmp에 [이동횟수+1, 이동한 위치]를 heappush한 후
            visited[now+A] = 1                          # 방문표시를 한다
        if 0 <= now+B <= 100000 and visited[now+B]==0:  # B칸 오른쪽으로 이동한 위치가 이동 범위 내에 있으면서 방문 전이라면
            heapq.heappush(tmp, [cnt+1, now+B])         # tmp에 [이동횟수+1, 이동한 위치]를 heappush한 후
            visited[now+B] = 1                          # 방문표시를 한다
        if 0 <= now*A <= 100000 and visited[now*A]==0:  # 현재 위치의 A배 오른쪽으로 이동한 위치가 이동 범위 내에 있으면서 방문 전이라면
            heapq.heappush(tmp, [cnt+1, now*A])         # tmp에 [이동횟수+1, 이동한 위치]를 heappush한 후
            visited[now*A] = 1                          # 방문표시를 한다
        if 0 <= now*B <= 100000 and visited[now*B]==0:  # 현재 위치의 B배 오른쪽으로 이동한 위치가 이동 범위 내에 있으면서 방문 전이라면
            heapq.heappush(tmp, [cnt+1, now*B])         # tmp에 [이동횟수+1, 이동한 위치]를 heappush한 후
            visited[now*B] = 1                          # 방문표시를 한다
    if 0 <= now-1 <= 100000 and visited[now-1] == 0:    # 한칸 왼쪽으로 이동한 위치가 이동 범위 내에 있으면서 방문 전이라면
        heapq.heappush(tmp, [cnt+1, now-1])             # tmp에 [이동횟수+1, 이동한 위치]를 heappush한 후
        visited[now-1] = 1                              # 방문표시를 한다
    if 0 <= now-A <= 100000 and visited[now-A] == 0:    # A칸 왼쪽으로 이동한 위치가 이동 범위 내에 있으면서 방문 전이라면
        heapq.heappush(tmp, [cnt+1, now-A])             # tmp에 [이동횟수+1, 이동한 위치]를 heappush한 후
        visited[now-A] = 1                              # 방문표시를 한다
    if 0 <= now-B <= 100000 and visited[now-B] == 0:    # B칸 왼쪽으로 이동한 위치가 이동 범위 내에 있으면서 방문 전이라면
        heapq.heappush(tmp, [cnt+1, now-B])             # tmp에 [이동횟수+1, 이동한 위치]를 heappush한 후
        visited[now-B] = 1                              # 방문표시를 한다