# 더하기사이클_BOJ1110

# input.txt
import sys
sys.stdin = open('input.txt')

# input 받기
N = int(input())                            # input 받은 숫자를 N에 저장
A = N                                       # A에 N과 같은 수를 저장
cnt = 0                                     # 회수를 저장할 변수

while 1:                                    # break나올 때까지 반복
    A = A%10*10 + (A//10 + A%10) % 10       # 일의자리 숫자를 10의 자리숫자로 일의자리와 십의자리 숫자의 합 중 일의 자리 숫자를 일의자리로 숫자를 조합
    cnt += 1                                # cnt를 1셈
    if A == N:                              # 처음과 같은 수가 되면 break
        break
print(cnt)
