# 게리멘더링_BOJ17471

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline
from itertools import combinations
from collections import deque

# input 받기
N = int(input())                            # 구역의 개수를 input 받고
people = list(map(int, input().split()))    # 각 구역에 인구수를 리스트로 input 받는다
road = [[] for _ in range(N)]               # 연결된 구역을 저장할 리스트를 생성하고
for i in range(N):                          # N개의 구역을 반복해서
    A = list(map(int, input().split()))     # 연결된 구역의 수와 연결된 구역 번호를 input 받고
    for j in range(1, A[0] + 1):            # 연결된 구역 수를 반복해서
        road[i].append(A[j] - 1)            # i번 구역과 연결된 구역번호를 append한다

def find(g):
    tmp = deque([g[0]])                     # deque를 생성하고 g 선거구 중 한개의 구역을 넣은 후
    sumN = 0                                # 선거구의 인구수 합을 저장할 변수를 생성한다
    while tmp:                              # tmp가 빌때까지 반복해서
        A = tmp.popleft()                   # tmp에서 구역을 popleft해서
        if A in g:                          # A가 선거 안에 있다면
            sumN += people[A]               # A의 인구수를 sumN에 더하고
            g.remove(A)                     # 선거구에서 A를 뺀 후
            for i in road[A]:               # A와 연결된 구역을 반복해서
                if i in g:                  # 연결된 구역이 선거구 안에 있다면
                    tmp.append(i)           # tmp에 append한다
    else:                                   # while이 끝난 후
        if g:                               # 선거구에 남은 구역이 있다면
            return 0                        # 모든 구역을 연결할 수 없으므로 0을 return하고
        else:                               # 선거구에 남은 구역이 없다면
            return sumN                     # 모든 구역을 연결할 수 있으므로 선거구의 인구를 return한다

ans = 10000                                 # 선거구의 인구수 최소값을 저장할 변수를 생성하고
A = [_ for _ in range(N)]                   # 구역번호를 A에 넣어 저장한다
for i in range(1, N // 2 + 1):              # 1부터 전체구역의 반만큼 크기를 반복해서
    for j in combinations(A, i):            # 전체 구역을 i개의 크기로 조합을 구하고
        tmp1 = []                           # 1번 선거구를 저장할 리스트를 생성하고
        tmp2 = []                           # 2번 선거구를 저장할 리스트를 생성한다
        for k in range(N):                  # 지역구의 수만큼 반복해서
            if k not in j:                  # k가 j의 조합안에 없다면
                tmp2.append(k)              # 2번 선거구에 편입하고
            else:                           # k가 j의 조합안에 있다면
                tmp1.append(k)              # 1번 선거구에 편입한다
        g1 = find(tmp1)                     # find함수를 통해 1번 지역구의 인구수를 g1에 저장하고
        g2 = find(tmp2)                     # find함수를 통해 2번 지역구의 인구수를 g2에 저장한 후
        if g1 and g2:                       # 1번, 2번 지역구 모두 인접한 구역으로 이루어져 있다면
            ans = min(ans, abs(g1 - g2))    # ans에 두 지역구의 인구수 차와 현재 저장된 최소값 중 더 작은 값을 저장한다
if ans == 10000:                            # 저장된 인구수의 차의 최소값이 10000이라면
    print(-1)                               # 지역구를 나눌 수 없으므로 -1을 출력하고
else:                                       # 저장된 인구수의 차의 최소값이 10000이 아니라면
    print(ans)                              # 두 지역구의 인구수 차의 최소값을 출력한다