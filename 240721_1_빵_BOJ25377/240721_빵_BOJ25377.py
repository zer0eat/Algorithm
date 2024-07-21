# 빵_BOJ25377

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
N = int(input())                        # 빵가게의 수를 input 받고
ans = 1001                              # 정답을 저장할 변수를 생성한다
for n in range(N):                      # 빵가게의 수를 반복해서
    a, b = map(int, input().split())    # 빵가게까지 이동시간 a / 빵이 나오는 시간을 input 받고
if a <= b:                              # 빵이 나오기 전에 도착할 수 있다면
        ans = min(ans, b)               # ans에 빵을 살 수 있는 최소시간을 저장한다
if ans == 1001:                         # 빵을 사지 못했다면
    print(-1)                           # -1을 출력하고
else:                                   # 빵을 샀다면
    print(ans)                          # 빵을 살 수 있는 최소시간을 출력한다