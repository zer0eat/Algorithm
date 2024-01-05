# 반복하지 않는 수_BOJ7696

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline
from collections import deque

# input 받기
dp = dict()                         # 반복 없는 숫자를 저장할 딕셔너리를 생성하고
cnt = 1                             # 반복 없는 숫자의 순서를 정할 변수를 생성한다
tmp = deque()                       # bfs 탐색을 위해 deque를 생성하고
for i in range(1, 10):              # 1부터 9까지 반복해서
    dp[cnt] = i                     # cnt번째 숫자에 i를 저장하고
    cnt += 1                        # cnt를 다음으로 넘긴 후
    tmp.append(str(i))              # tmp에 i를 append한다
while cnt < 1000001:                # cnt가 1000000까지 정해지도록 반복해서
    A = tmp.popleft()               # deque에서 맨 앞에 있는 수를 빼준 후
    for i in range(10):             # 0부터 9까지 반복해서
        if str(i) not in A:         # i가 A에 포함되지 않는다면
            dp[cnt] = A+str(i)      # cnt번째 숫자에 A+i를 저장하고
            cnt += 1                # cnt를 다음으로 넘긴 후
            tmp.append(A+str(i))    # tmp에 A+i를 append한다
while 1:                            # break가 나올때까지 반복해서
    N = int(input())                # N을 input 받고
    if N == 0:                      # N이 0이면
        break                       # break하고
    else:                           # 그렇지 않으면
        print(dp[N])                # N번째 반복없는 수를 출력한다