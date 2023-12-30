# 체커_BOJ1090

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
N = int(input())                                                        # 체커의 수를 input 받고
checker = []                                                            # 체커를 저장할 리스트를 생성한다
x = set()                                                               # 체커의 x 좌표를 저장할 set을 생성하고
y = set()                                                               # 체커의 y 좌표를 저장할 set을 생성한다
for n in range(N):                                                      # 체커의 수를 반복해서
    a, b = map(int, input().split())                                    # 체커의 위치를 input 받고
    checker.append([a, b])                                              # checker 리스트에 체커의 위치를 append하고
    x.add(a)                                                            # x 셋에 x 좌표를 add
    y.add(b)                                                            # y 셋에 y 좌표를 add 한다
x = list(x)                                                             # x를 리스트로 바꿔주고
y = list(y)                                                             # y를 리스트로 바꿔준 후
ans = [1e9]*N                                                           # 정답을 저장할 리스트를 생성하고
ans[0] = 0                                                              # 1개의 체커의 최소 이동수는 0이므로 0으로 저장한다
dp = [[0]*N for _ in range(len(x)*len(y))]                              # 체커별 이동거리를 저장할 dp 리스트를 생성하고
cnt = 0                                                                 # 체커를 모을 위치를 가르키는 변수를 생성하고
for i in x:                                                             # 체커를 모을 칸의 x 좌표를 반복하고
    for j in y:                                                         # 체커를 모을 칸의 y 좌표를 반복해서
        for n in range(N):                                              # 체커의 수를 반복한 후
            dp[cnt][n] = abs(checker[n][0]-i) + abs(checker[n][1]-j)    # 해당 체커가 cnt번째 위치에 모이는 경우 이동거리를 저장한다
        else:                                                           # 모든 체커의 이동거리를 구했다면
            cnt += 1                                                    # 체커를 모을 칸을 1 이동한다
for q in range(len(x)*len(y)):                                          # 체커를 모을 칸을 반복해서
    dp[q].sort()                                                        # 체커 별 이동거리를 오름차순 정렬한다
for n in range(1, N):                                                   # 1부터 체커의 수를 반복해서
    for length in dp:                                                   # 체커를 모을 칸 별 체커의 이동거리 리스트를 반복한 후
        ans[n] = min(ans[n], sum(length[:n+1]))                         # ans의 n번째 인덱스에 n+1개의 체커가 모였을 때 최소 이동거리를 저장한다
print(*ans)                                                             # k개의 체커가 같은 칸에 모이도록 체커를 이동해야 하는 최소 횟수를 출력한다