# 이진탐색_13632

#input.txt 열기
import sys
sys.stdin = open('input.txt')

# input 받기
T = int(input()) # 테스트 케이스
for t in range(T):
    P, A, B = map(int, input().split()) # P는 전체페이지 A는 a가 찾을 페이지 B는 b가 찾을 페이지

    # 이진 탐색으로 찾기
    # A 검색에 사용할 요소
    lA = 1 # 시작할 때 가장 작은 값
    rA = P # 시작할 때 가장 큰 값
    cntA = 0 # A를 찾는데 걸린 횟수
    # B 검색에 사용할 요소
    lB = 1 # 시작할 때 가장 작은 값
    rB = P # 시작할 때 가장 큰 값
    cntB = 0 # B를 찾는데 걸린 횟수

    while A >= 0:
        cA = int((lA + rA) / 2) # A를 찾을 때 중앙값
        if A < cA:
            cntA += 1
            rA = cA
        elif A > cA:
            cntA += 1
            lA = cA
        elif A == cA:
            cntA += 1
            break

    while B >= 0:
        cB = int((lB + rB) / 2) # B를 찾을 때 중앙값
        if B < cB:
            cntB += 1
            rB = cB
        elif B > cB:
            cntB += 1
            lB = cB
        elif B == cB:
            cntB += 1
            break

    # 적게 걸린 사람 출력
    if cntA < cntB:
        print(f'#{t+1} A')
    elif cntA > cntB:
        print(f'#{t+1} B')
    elif cntA == cntB:
        print(f'#{t+1} 0')


