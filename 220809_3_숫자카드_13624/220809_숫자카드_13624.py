# 숫자카드_13624

#input.txt 열기
import sys
sys.stdin = open('input.txt')

#input 리스트로 받기
T = int(input())
for t in range(T):
    N = int(input())
    A = list(input())
    intA = []
    for a in A:
        intA.append(int(a))

    #카운팅 정렬
    C = [0] * 10
    for inta in intA:
        C[inta] += 1

    # 가장 많은 숫자 찾기
    bignum = 0
    numb = 0
    for c in range(len(C)):
        if numb <= C[c]:
            numb = C[c]
            bignum = c
        else:
            pass

    print(f'#{t+1} {bignum} {numb}')

