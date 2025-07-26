# 세 개의 소수 문제_BOJ11502

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
prime = [0]*1000                        # 소수를 저장할 리스트를 생성하고
prime[0] = 1                            # 0을 소수가 아니라고 표시하고
prime[1] = 1                            # 1을 소수가 아니라고 표시하고
for n in range(2, 1000):                # 2부터 반복해서
    if prime[n] == 0:                   # 소수가 아니라는 표시가 없다면
        for m in range(n+n, 1000, n):   # 소수의 배수를 반복해서
            prime[m] = 1                # 소수가 아니라고 표시한다
ans = []                                # 소수를 저장할 리스트를 생성하고
for p in range(1000):                   # 숫자를 반복해서
    if prime[p] == 0:                   # 해당 숫자가 소수라면
        ans.append(p)                   # 리스트에 append한다
T = int(input())                        # 테스트 케이스를 input받고
for t in range(T):                      # 테스트 케이스를 반복해서
    K = int(input())                    # 숫자를 input받고
    flag = False                        # 정답을 찾은 것을 표시할 변수를 생성한다
    for a in ans:                       # 소수 리스트를 반복해서
        if flag:                        # 정답을 찾았다면
            break                       # for문을 종료한다
        for b in ans:                   # 소수 리스트를 반복해서
            if flag:                    # 정답을 찾았다면
                break                   # for문을 종료한다
            for c in ans:               # 소수 리스트를 반복해서
                if flag:                # 정답을 찾았다면
                    break               # for문을 종료한다
                if a+b+c == K:          # 세 소수의 합이 k라면
                    print(a,b,c)        # 세 소수를 출력하고
                    flag = True         # 정답을 찾았다고 표시한다
    else:                               # 정답을 찾지 못했다면
        print(0)                        # 0을 출력한다