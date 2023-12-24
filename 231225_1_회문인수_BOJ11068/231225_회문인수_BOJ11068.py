# 회문인수_BOJ11068

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
T = int(input())                            # 테스트 케이스를 input 받고
for t in range(T):                          # 테스트 케이스를 반복해서
    N = int(input())                        # 회문 판별할 정수를 input 받는다
    for i in range(2, 65):                  # 2진수부터 64진수를 반복해서
        tmp = N                             # 정수를 tmp에 저장하고
        change = []                         # i진수로 변경 후 숫자를 저장할 리스트를 생성한다
        while tmp != 0:                     # 정수가 0이 될 때까지 반복해서
            change.append(tmp % i)          # 정수를 i로 나눈 나머지를 change에 append하고
            tmp //= i                       # tmp를 i의 몫으로 저장한다
        for j in range(len(change)//2):     # i진수로 바꾼 숫자의 절반을 반복해서
            if change[j] != change[-j-1]:   # 앞에서 j번째와 뒤에서 j번째가 다르다면 회문이 아니므로
                break                       # for문을 break한다
        else:                               # 회문인 숫자를 찾았다면
            print(1)                        # 1을 출력하고
            break                           # for문을 break한다
    else:                                   # 64진수까지 회문이 없다면
        print(0)                            # 0을 출력한다