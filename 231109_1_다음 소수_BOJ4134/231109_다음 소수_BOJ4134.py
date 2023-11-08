# 다음 소수_BOJ4134

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
N = int(input())                                # 테스트 케이스의 수를 input받고
for n in range(N):                              # 테스트 케이스를 반복해서
    a = int(input())                            # 정수를 input 받고
    while 1:                                    # break가 나올때까지 반복해서
        if a < 2:                               # input 받은 정수 a가 2 미만이라면
            print(2)                            # a보다 큰 소수는 2이므로 출력하고
            break                               # while문을 break한다
        else:                                   # a가 2이상이라면
            for i in range(2, int(a**0.5)+1):   # 2부터 제곱근까지 반복해서
                if a % i == 0:                  # a를 나눴을 때 나눠진다면 a는 소수가 아니므로
                    a += 1                      # a를 다음수로 넘기고
                    break                       # for문을 break한다
            else:                               # for문을 모두 돌았다면 나눠지는 숫자가 없으므로 소수가 되므로
                print(a)                        # a보다 큰 소수를 출력하고
                break                           # while문을 break한다