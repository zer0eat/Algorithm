# 소수의연속합_BOJ1644

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
N = int(input())

tmp = [0]*(N+1)                                 # 소수를 저장할 리스트 생성
for q in range(2, N+1):                         # 2부터 N까지 반복할 때
    if tmp[q] == 0:                             # tmp[q]가 0으로 소수나 소수가 아니라는 표시가 되어있지 않다면
        tmp[q] = 1                              # q는 소수이기 때문에 tmp[q]를 1로 표시한다 
        for p in range(q, N+1, q):              # q부터 찾고자 하는 수까지 q의 배수로 반복해서
            if p == q:                          # q는 이미 표시를 했으므로
                pass                            # pass
            else:                               # 그 배수는
                tmp[p] = 2                      # 소수가 아니므로 tmp[q]는 2라고 표시한다
prime = []                                      # 소수를 저장할 리스트를 생성
for n in range(N+1):                            # 표시가 모두 끝났다면 tmp를 반복해서
    if tmp[n] == 1:                             # 1로 표시된 소수가 나오면
        prime.append(n)                         # prime에 append

L = len(prime)                                  # L prime의 길이
A = 0                                           # A 연속 소수합의 시작점
B = 0                                           # B 연속 소수합의 끝점
ans = 0                                         # 정답의 수를 저장할 변수 생성
while B <= L:                                   # 연속 소수합의 끝점이 prime의 길이 밖을 벗어날 때까지 반복해서
    sumPrime = sum(prime[A:B])                  # sumPrime에 A부터 B까지의 합을 저장한다
    if sumPrime == N:                           # sumPrime이 N이랑 같다면
        ans += 1                                # ans에 1을 추가하고
        B += 1                                  # B를 한칸 이동한다
    elif sumPrime < N:                          # sumPrime이 N보다 작다면
        B += 1                                  # 전체 합의 크기를 키워야하므로 B를 한칸 이동한다
    else:                                       # sumPrime이 N보다 크다면
        A += 1                                  # 전체 합의 크기를 줄여야하므로 A를 한칸 이동한다
print(ans)                                      # 모든 반복을 마쳤다면 소수의 연속합으로 만들 수 있는 개수를 출력한다