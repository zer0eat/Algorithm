# 암호 키_BOJ1816

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
N = int(input())                    # 암호로 사용할 수의 개수를 input 받고
for _ in range(N):                  # 암호로 사용할 수의 개수를 반복해서
    S = int(input())                # 암호로 사용할 수를 input 받고
    for i in range(2, 1000001):     # 2부터 1000000까지 반복해서
        if S % i == 0:              # i로 나누어 떨어진다면
            print('NO')             # 소수가 아니므로 NO를 출력하고
            break                   # for문을 break한다
    else:                           # 1000000까지 나눠지는 수가 없다면
        print('YES')                # 매우 큰 소수로 YES를 출력한다