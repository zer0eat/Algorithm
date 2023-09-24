# 효율적인 해킹_BOJ1325

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline
from collections import deque

# input 받기
N, M = map(int, input().split())        # N 컴퓨터의 수 / M 신뢰하는 관계의 수
lst = [[] for _ in range(N)]            # 신뢰관계를 저장할 리스트를 생성하고
for _ in range(M):                      # 신뢰하는 관계의 수를 반복해서
    a, b = map(int, input().split())    # 컴퓨터 a, b를 input 받고
    lst[b-1].append(a-1)                # b-1 인덱스에 a-1을 append 해서 b를 해킹하면 a를 해킹할 수 있는 관계를 저장한다
ans = []                                # 정답을 저장할 리스트를 생성하고
maxN = 0                                # 최대 해킹 수를 저장할 변수를 생성해서
for i in range(N):                      # 컴퓨터의 번호를 반복해서
    cnt = 0                             # i번 컴퓨터를 해킹했을 때 해킹할 수 있는 컴퓨터의 수를 저장할 변수를 생성하고
    tmp = deque([i])                    # i번 컴퓨터를 deque에 넣고 생성한다
    visited = [0]*N                     # 방문표시를 할 리스트를 생성하고
    visited[i] = 1                      # i 컴퓨터를 방문표시한다
    while tmp:                          # tmp가 빌때까지 반복해서
        cnt += 1                        # 해킹 가능한 컴퓨터의 수를 1 추가하고
        num = tmp.popleft()             # tmp에서 컴퓨터를 popleft해서
        for n in lst[num]:              # num을 신뢰하는 컴퓨터를 반복해서
            if visited[n] == 0:         # 방문전이라면
                tmp.append(n)           # tmp에 신뢰하는 컴퓨터를 append하고
                visited[n] = 1          # 방문표시한다
    else:                               # tmp가 비었을 때
        if maxN < cnt:                  # maxN 보다 i번째 해킹했을 때 해킹 가능한 숫자가 더 크다면
            ans = [i+1]                 # ans에 i번째 컴퓨터 번호를 저장한 리스트로 저장한다
            maxN = cnt                  # maxN을 cnt로 저장하고
        elif maxN == cnt:               # maxN가 i번째 해킹했을 때 해킹 가능한 숫자와 같다면
            ans.append(i+1)             # ans에 i번째 컴퓨터 번호를 append 한다
print(*ans)                             # 한 번에 가장 많은 컴퓨터를 해킹할 수 있는 컴퓨터의 번호를 오름차순으로 출력한다