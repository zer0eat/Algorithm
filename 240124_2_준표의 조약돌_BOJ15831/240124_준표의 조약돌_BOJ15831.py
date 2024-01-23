# 준표의 조약돌_BOJ15831

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
N, B, W = map(int, input().split()) # N 조약돌의 수 / B 최대 검은색 돌의 수 / W 최소 흰색돌의 수를 input 받고
road = list(input().strip())        # 전체 조약돌을 리스트로 input 받는다
ans = 0                             # 정답을 저장할 변수를 생성하고
l = 0                               # 왼쪽을 가르킬 포인터를 생성하고
r = 0                               # 오른쪽을 가르킬 포인터를 생성한다
if road[0] == 'B':                  # 첫번째 돌이 흑돌이라면
    wN, bN = 0, 1                   # 백돌을 0 흑돌을 1로 변수를 생성하고
else:                               # 첫번째 돌이 백돌이라면
    wN, bN = 1, 0                   # 백돌을 1 흑돌을 0으로 변수를 생성한다
if bN <= B and wN >= W:             # 흑돌과 백돌의 수가 조건을 만족한다면
    ans = max(ans, r-l+1)           # ans에 더 큰 값을 저장한다
while l < N:                        # 왼쪽 포인터가 끝까지 갈때까지 반복해서
    if bN <= B and r < N-1:         # 흑돌의 수가 B개 이하이고 오른쪽 포인터가 맨 마지막이 아니라면
        r += 1                      # 오른쪽 포인터를 한칸 옮기고
        if road[r] == 'B':          # 오른쪽 포인터의 돌이 흑돌이라면
            bN += 1                 # 흑돌의 수를 1 추가하고
        else:                       # 오른쪽 포인터의 돌이 백돌이라면
            wN += 1                 # 백돌의 수를 1 추가한다
    else:                           # 흑돌의 수가 B개보다 많거나 오른쪽 포인터가 맨 마지막이라면
        if road[l] == 'B':          # 왼쪽 포인터의 돌이 흑돌이라면
            bN -= 1                 # 흑돌의 수를 1 감소하고
        else:                       # 왼쪽 포인터의 돌이 백돌이라면
            wN -= 1                 # 백돌의 수를 1 감소한 후
        l += 1                      # 왼쪽 포인터를 한 칸 이동한다
    if bN <= B and wN >= W:         # 흑돌과 백돌의 수가 조건을 만족한다면
        ans = max(ans, r-l+1)       # ans에 더 큰 값을 저장한다
print(ans)                          # 준표와 미미가 걷게 될 가장 긴 구간의 길이를 한 줄에 출력한다