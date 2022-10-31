# 골드바흐의추측_BOJ9020

# input.txt 열기
import sys
sys.stdin = open('input.txt')

# input 받기
T = int(sys.stdin.readline())                               # 테스트 케이스
for t in range(T):                                          # 테스트 케이스를 반복해서
    N = int(sys.stdin.readline())                           # 골드바흐 수를 input 받고
    prime = [0]*(N+1)                                       # 골드바흐 수보다 작은 소수를 표시할 리스트를 생성한다
    for a in range(2, N+1):                                 # 2부터 N까지 반복할 때
        if prime[a] == 0:                                   # prime[a]가 0으로 소수나 소수가 아니라는 표시가 되어있지 않다면
            prime[a] = 1                                    # a는 소수이기 때문에 prime[a]를 1로 표시한다
            for b in range(a, N+1, a):                      # a부터 찾고자 하는 수까지 a의 배수로 반복해서
                if b == a:                                  # a는 pass하고
                    pass
                else:                                       # 그 배수는
                    prime[b] = 2                            # 소수가 아니므로 prime[b]는 2라고 표시한다

    half1 = N//2                                            # 골드바흐 수를 반으로 나눈 수를 저장하는 변수
    half2 = N//2                                            # 골드바흐 수를 반으로 나눈 수를 저장하는 변수
    while 1:                                                # break까지 반복해서
        if prime[half1] == 1 and prime[half2] == 1:         # 둘다 소수라면
            print(half1, half2)                             # 출력하고
            break                                           # while문 break
        else:                                               # 둘 중 하나라도 소수가 아니라면
            half1 -= 1                                      # half1에서 1을 빼서
            half2 += 1                                      # half2에 더해준다