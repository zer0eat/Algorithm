# 공약수_BOJ2436

# input.txt 열기
import sys
sys.stdin = open('input.txt')
import math

# input 받기
A, B = map(int, sys.stdin.readline().split())   # A 최대공약수 / B 최소공배수

B //= A                                         # 최소공배수에서 최대공약수를 나눠주면 남은 수가 두 서로소의 곱이 된다

ans = []                                        # 두 서로소를 저장할 빈리스트를 생성하고
num = 1                                         # 서로소를 세기 위한 변수를 생성한다

while num * num <= B:                           # num이 B의 제곱근보다 작을 때 반복해서
    if B % num == 0:                            # B가 num으로 나누어 떨어질 때
        if math.gcd(num, B//num) == 1:          # num과 B//num이 서로소라면
            ans.append(num)                     # ans에 num을 append
            ans.append(B//num)                  # ansdp B//num을 append
    num += 1                                    # num을 1 증가시킨다

ans.sort()                                      # ans를 오름차순으로 정렬하고

Q = A * (ans[(len(ans) // 2) - 1])              # Q에 작은 약수를 저장하고
W = A * (ans[(len(ans) // 2)])                  # W에 큰 약수를 저장한다
print(Q, W)                                     # Q, W를 출력한다