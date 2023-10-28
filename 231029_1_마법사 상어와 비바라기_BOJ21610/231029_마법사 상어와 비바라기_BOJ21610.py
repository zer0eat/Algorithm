# 마법사 상어와 비바라기_BOJ21610

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline
from collections import deque

# input 받기
N, M = map(int, input().split())                                                # N 구름을 부를 필드의 길이 / M 구름을 이동시킬 횟수를 input 받고
arr = [list(map(int, input().split())) for _ in range(N)]                       # 구름을 부를 필드를 input 받고
cloud = deque([(N-1,0), (N-1,1), (N-2,0), (N-2,1)])                             # 첫번째 구름을 생성하고
dxy = [[0, -1], [-1, -1], [-1, 0], [-1, 1], [0, 1], [1, 1], [1, 0], [1, -1]]    # 구름을 델타이동시킬 리스트를 생성한다

def move_cloud(cloud, d, s):
    global N                                # 필드의 길이를 global 변수로 선언하고
    new_cloud = deque()                     # 이동한 구름을 저장한 deque를 생성하다
    while cloud:                            # cloud가 빌 때까지 반복해서
        r, c = cloud.popleft()              # cloud에서 popleft해서 구름의 위치를 저장한 후
        x = (r + dxy[d-1][0]*s + N) % N     # 구름을 이동시킨 행의 위치를 x에 저장하고
        y = (c + dxy[d-1][1]*s + N) % N     # 구름을 이동시킨 열의 위치를 y에 저장하고
        new_cloud.append((x,y))             # 이동 시킨 구름을 deque에 append한다
    return new_cloud                        # 구름의 위치를 담은 deque를 return한다

def make_rain(new_cloud):
    for c in new_cloud:                     # 이동된 구름을 반복해서
        arr[c[0]][c[1]] += 1                # 구름의 자리에 비를 내려 물의 양을 1씩 추가한다

def amplification(new_cloud):
    for c in new_cloud:                     # 이동된 구름을 반복해서
        for q in range(1, 8, 2):            # 대각선 4방향을 반복해서
            x = c[0] + dxy[q][0]            # 대각선으로 이동된 행의 위치를 x에 저장하고
            y = c[1] + dxy[q][1]            # 대각선으로 이동된 열의 위치를 y에 저장하고
            if 0<=x<N and 0<=y<N:           # 이동된 위치가 필드 안이면서
                if arr[x][y] > 0:           # 이동된 위치에 물이 있다면
                    arr[c[0]][c[1]] += 1    # 구름이 있던자리에 물을 증폭해서 물의 양을 1 추가한다

def make_cloud(new_cloud):
    cloud = deque([])                       # 생성한 구름을 저장할 deque를 생성하고
    for i in range(N):                      # 필드의 행을 반복하고
        for j in range(N):                  # 필드의 열을 반복해서
            if arr[i][j] >= 2 and (i, j) not in new_cloud:  # 해당 칸에 물이 2이상 있고 이전에 구름이 있던 위치가 아니라면
                cloud.append((i, j))        # 구름을 생성해서 cloud에 append하고
                arr[i][j] -= 2              # 구름을 생성하기 위한 비용을 2 감소한다
    return cloud                            # 생성한 구름이 담은 deque를 return한다

for m in range(M):                          # 구름을 이동시킬 횟수를 반복해서
    d, s = map(int, input().split())        # d 구름을 이동시킬 방향 / s 구름을 이동시킬 칸수를 input 받는다
    new_cloud = move_cloud(cloud, d, s)     # 1. 구름을 이동시키고
    make_rain(new_cloud)                    # 2. 이동시킨 자리에 비를 내린 후
    amplification(new_cloud)                # 3. 구름이 있던 자리에 물을 증폭하고
    cloud = make_cloud(new_cloud)           # 4. 새로운 구름을 생성한다
ans = 0                                     # 필드에 있는 물의 합을 저장할 변수를 생성하고
for a in arr:                               # 필드의 행을 반복해서
    ans += sum(a)                           # 한 행의 물의 합을 ans에 더한 후
print(ans)                                  # 이동이 모두 끝난 후 물의 양의 합을 출력한다.