# 공유기 설치_BOJ2110

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
N, C = map(int, input().split())        # N 집의 개수 / C 공유기의 개수를 input 받고
wifi = [int(input()) for _ in range(N)] # 공유기를 설치할 수 있는 집을 리스트로 input 받고
wifi.sort()                             # 공유기를 설치할 수 있는 집을 오름차순으로 정렬한다
l = 1                                   # 최소거리를 저장한 변수를 생성하고
r = wifi[-1] - wifi[0]                  # 최대거리를 저장한 변수를 생성한다
ans = 0                                 # 정답을 저장할 변수를 생성하고
while l <= r:                           # l이 r과 같거나 커질 때까지 반복해서
    mid = (l+r)//2                      # 두 거리의 중점을 저장하고
    now = wifi[0]                       # 현재 위치를 저장할 변수를 생성하고
    cnt = 1                             # 공유기를 설치한 개수를 저장할 변수를 생성한다
    for i in range(1, N):               # 1번 인덱스부터 N-1까지 반복해서
        if wifi[i] >= now + mid:        # 해당 인덱스의 위치가 현재 위치에서 mid 거리만큼 떨어진 거리 밖에 있다면
            now = wifi[i]               # 현재 위치를 i인덱스의 집으로 저장하고
            cnt += 1                    # 공유기 설치 개수를 1 추가한다
    if cnt < C:                         # 공유기 설치 개수가 C보다 작다면
        r = mid-1                       # 최대거리를 줄이고
    else:                               # 공유기 설치 개수가 C와 같거나 크다면
        ans = max(ans, mid)             # ans를 mid거리로 저장하고
        l = mid+1                       # 최소거리를 늘려준다
print(ans)                              # 인접한 두 공유기 사이의 최대 거리를 출력한다