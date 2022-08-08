# 구간합_13626

#input.txt 받기
import sys
sys.stdin = open('input.txt')

# input 리스트로 받기
T = int(input())
for t in range(T):
    N, M = map(int, input().split())
    A = list(map(int, input().split()))

    #이웃한 M개의 합의 리스트
    plus = []
    for b in range(N-M+1):
        X = 0
        for c in range(b, M+b):
            X += A[c]
        plus.append(X)

    #이웃한 M개의 합 중 가장 큰 경우
    maxi = 0
    for ma in plus:
        if maxi < ma:
            maxi = ma
        else:
            pass

    #이웃한 M개의 합 중 가장 작은 경우
    mini = 1000000
    for mi in plus:
        if mini > mi:
            mini = mi
        else:
            pass

    print(f'#{t+1} {maxi-mini}')