# 부녀회장이될테야_BOJ2775

# input.txt
import sys
sys.stdin = open('input.txt')

# input 받기
T = int(input())                # 테스트케이스
for t in range(T):              # 테스트케이스 반복하기
    K = int(input())            # 층수
    N = int(input())            # 호수

    floor = []                  # 호수에 따른 거주민의 수를 저장할 리스트
    for n in range(1,N+1):      # 0층의 호수를 반복하면서
        floor.append(n)         # 각각의 호수에 살고 있는 거주민의 수를 floor에 append

    for k in range(K):          # 층수를 반복하고
        tmp = 0                 # 거주민을 저장할 변수를 생성
        for n in range(N):      # k층의 호수를 반복하면서
            tmp += floor[n]     # tmp에 n호수까지 거주민을 더한다
            floor[n] = tmp      # floor[n]에 거주민의 수를 저장한다

    print(floor[N-1])


