# 푸앙이와 종윤이_BOJ25591

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
A, B = map(int, input().split())    # 두 수를 input 받고
a = 100 - A                         # 100에서 A를 뺀수를 구하고
b = 100 - B                         # 100에서 B를 뺀수를 구하고
c = 100 - (a+b)                     # 100에서 a와b의 합을 뺀수를 구하고
d = a * b                           # a와 b의 곱을 구하고
q = d // 100                        # d를 100으로 나눈 몫을 구하고
r = d % 100                         # d를 100으로 나눈 나머지를 구한다
print(a,b,c,d,q,r)                  # 앞서 구한 6가지 출력하고
print(c+q, r)                       # c+q와 r을 출력한다