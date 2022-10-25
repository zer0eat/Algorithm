# 소수_BOJ2581

# input.txt 열기
import sys
sys.stdin = open('input.txt')

# input 받기
M = int(sys.stdin.readline())                   # M 소수를 구하는 시작 값
N = int(sys.stdin.readline())                   # N 소수를 구하는 마지막 값

ans = [0]*(N+1)                                 # 소수를 저장할 리스트 생성
for q in range(2, N+1):                         # 2부터 N까지 반복할 때
    if ans[q] == 0:                             # ans[q]가 0으로 소수나 소수가 아니라는 표시가 되어있지 않다면
        ans[q] = 1                              # q는 소수이기 때문에 ans[q]를 1로 표시한다
        for p in range(q, N+1, q):              # q부터 찾고자 하는 수까지 q의 배수로 반복해서
            if p == q:                          # q는 pass하고
                pass
            else:                               # 그 배수는
                ans[p] = 2                      # 소수가 아니므로 ans[q]는 2라고 표시한다


prime = []
for n in range(M, N+1):                         # 표시가 모두 끝났다면
    if ans[n] == 1:                             # 1로 표시된 소수만 출력한다
        prime.append(n)                         # prime에 소수를 넣은 후

if prime:                                       # prime이 빈 리스트가 아니면
    print(sum(prime))                           # 소수의 합 출력
    print(min(prime))                           # 최소 소수 출력
else:                                           # 빈 리스트라면
    print(-1)                                   # -1 출력