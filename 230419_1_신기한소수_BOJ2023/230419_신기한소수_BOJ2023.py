# 신기한소수_BOJ2023

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline
import math

# input 받기
N = int(input())                                        # N 자리의 수
prime = [2, 3, 5, 7]                                    # N이 1일 때 소수의 리스트를 저장
tmp = []                                                # prime보다 한자리 큰 소수를 저장할 빈 리스트 생성
cnt = 1                                                 # 자리수를 셀 변수 생성

while cnt < N:                                          # 자리수가 N이 될때
    for i in prime:                                     # prime 리스트에 담긴 숫자를 반복해서
        for j in range(1, 10, 2):                       # 끝자리가 짝수라면 소수가 될 수 없으므로 홀수만 반복한다
            A = int(str(i) + str(j))                    # prime에 담긴 숫자 뒤에  j를 붙여 한자리 늘어난 숫자를 만들고
            for q in range(2, int(math.sqrt(A))+1):     # 해당숫자의 제곱근까지 반복해서
                if A % q == 0:                          # A가 q로 나누어 떨어지면 소수가 아니므로
                    break                               # break하고
            else:                                       # 모든 숫자로 나누어 떨어지지 않는다면
                tmp.append(A)                           # 소수이므로 tmp에 append 한다
    else:                                               # prime에 담긴 숫자를 모두 반복했다면
        cnt += 1                                        # cnt에 1을 추가해서 자리수를 1 늘리고
        prime = tmp[:]                                  # prime을 tmp로 바꿔 저장한다
        tmp = []                                        # tmp는 비워준다

for i in prime:                                         # N자리의 소수를 구했다면 prime을 반복해서
    print(i)                                            # N자리 소수를 출력한다